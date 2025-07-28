import tkinter as tk
from tkinter import ttk

from Models.track import Track
from Models.track_list import TrackList
from Models.favorite import Favorite
from Models.musicplayer import MusicPlayer

from Views.track_view import TrackView
from Views.track_list_view import TrackListView
from Views.favorite_view import FavoriteView
from Views.musicplayer_view import MusicPlayerView

from Controllers.track_controller import TrackController
from Controllers.track_list_controller import TrackListController
from Controllers.favorite_controller import FavoriteController
from Controllers.musicplayer_controller import MusicPlayerController

import font_manager as fonts
from database.track_db import get_all_tracks
from database.tracklist_db import get_all_tracklists
from database.favorite_db import get_all_favorites


class JukeboxApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jukebox Simulation")
        self.root.geometry("900x650")
        self.root.configure(bg="#0A0F2C")

        fonts.configure()

        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True)

        # Tabs
        self.view_frame = tk.Frame(self.notebook, bg="#0A0F2C")
        self.playlist_frame = tk.Frame(self.notebook, bg="#0A0F2C")
        self.favorite_frame = tk.Frame(self.notebook, bg="#0A0F2C")
        self.musicplayer_frame = tk.Frame(self.notebook, bg="#0A0F2C")

        self.notebook.add(self.view_frame, text="View Tracks")
        self.notebook.add(self.playlist_frame, text="Playlist")
        self.notebook.add(self.favorite_frame, text="Favorite")
        self.notebook.add(self.musicplayer_frame, text="Music Player")

        # Lấy dữ liệu track từ database
        self.default_tracks = get_all_tracks()
        self.track_list = get_all_tracklists()  
        self.favorite = Favorite()  
        self.musicplayer = None  

        # Views
        self.track_view = TrackView(self.view_frame)
        self.track_list_view = TrackListView(self.playlist_frame)
        self.favorite_view = FavoriteView(self.favorite_frame)
        self.musicplayer_view = MusicPlayerView(self.musicplayer_frame)

        # Controllers
        self.track_controller = TrackController(None, self.track_view)
        self.track_list_controller = TrackListController(self.track_list, self.track_list_view)
        self.favorite_controller = FavoriteController(self.favorite, self.favorite_view)
        self.musicplayer_controller = MusicPlayerController(self.musicplayer, self.musicplayer_view)

        # Layout each view
        self.track_view.get_frame().pack(fill="both", expand=True)
        self.track_list_view.get_frame().pack(fill="both", expand=True)
        self.favorite_view.get_frame().pack(fill="both", expand=True)
        self.musicplayer_view.get_frame().pack(fill="both", expand=True)

        # Bind buttons in track view
        self.track_view.btn_detail.config(command=self.show_selected_detail)
        self.track_view.btn_add_fav.config(command=self.add_to_favorite_callback)

        # Bind button in playlist view
        self.track_list_view.create_playlist_btn.config(command=self.create_playlist_callback)
        self.track_list_view.add_track_btn.config(command=self.add_track_popup_callback)
        self.track_list_view.playlist_listbox.bind('<<ListboxSelect>>', self.on_playlist_select)
        self.track_list_view.clear_playlists_btn.config(command=self.clear_playlists_callback)

        # Bind buttons in favorite view
        self.favorite_view.clear_track_btn.config(command=self.clear_selected_favorite_callback)
        self.favorite_view.clear_all_btn.config(command=self.clear_all_favorites_callback)

        # Hiển thị track ngay khi khởi động
        self.display_tracks()
        self.show_all_playlists()
        self.display_favorites()

    def display_tracks(self):
        self.track_view.get_listbox().delete(0, tk.END)
        for track in self.default_tracks:
            self.track_view.get_listbox().insert(
                tk.END, f"{track['track_id']}. {track['track_name']} - {track['artist']} (Rating: {track['rating']})"
            )

    def display_favorites(self):
        fav_tracks = get_all_favorites()
        self.favorite_view.display_favorites(fav_tracks)

    def show_all_playlists(self):
        self.track_list_controller.update_playlist_listbox()
        from database.tracklist_db import get_all_tracklists
        playlists = get_all_tracklists()
        if playlists:
            self.track_list_controller.update_tracks_listbox_by_id(playlists[0]['tracklist_id'])


    def show_selected_detail(self):
        selected_index = self.track_view.get_listbox().curselection()
        if selected_index:
            index = selected_index[0]
            selected_track = self.default_tracks[index]
            self.track_controller.show_detail(selected_track)
        else:
            self.track_view.show_message("Please select a track first.")

    def create_playlist_callback(self):
        title = self.track_list_view.playlist_name_entry.get()
        self.track_list_controller.create_playlist(title)
        self.track_list_view.playlist_name_entry.delete(0, 'end')

    def add_track_popup_callback(self):
        # Lấy index playlist đang chọn
        playlist_index = self.track_list_view.playlist_listbox.curselection()
        if not playlist_index:
            self.track_list_view.show_message("Please select a playlist first!")
            return
        playlist_index = playlist_index[0]
        all_tracks = self.default_tracks
        self.track_list_controller.show_add_track_popup(all_tracks, playlist_index)

    def on_playlist_select(self, event):
        selection = self.track_list_view.playlist_listbox.curselection()
        if not selection:
            self.track_list_view.tracks_listbox.delete(0, 'end')
            return
        playlist_index = selection[0]
        from database.tracklist_db import get_all_tracklists
        playlists = get_all_tracklists()
        if 0 <= playlist_index < len(playlists):
            playlist_id = playlists[playlist_index]['tracklist_id']
            self.track_list_controller.update_tracks_listbox_by_id(playlist_id)
        else:
            self.track_list_view.tracks_listbox.delete(0, 'end')

    def clear_playlists_callback(self):
        self.track_list_controller.clear_all_playlists()

    def clear_selected_favorite_callback(self):
        selection = self.favorite_view.get_fav_listbox().curselection()
        if not selection:
            self.favorite_view.show_message("Please select a track to remove!")
            return
        index = selection[0]
        self.favorite_controller.remove_selected_favorite(index)

    def clear_all_favorites_callback(self):
        self.favorite_controller.clear_all_favorites()
        self.display_favorites()

    def add_to_favorite_callback(self):
        selection = self.track_view.get_listbox().curselection()
        if not selection:
            self.track_view.show_message("Please select a track to add to favorite!")
            return
        index = selection[0]
        track = self.default_tracks[index]
        self.favorite_controller.add_to_favorite(track)

if __name__ == "__main__":
    root = tk.Tk()
    app = JukeboxApp(root)
    root.mainloop()
