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

        # Models and default data
        self.default_tracks = Track.get_default_tracks()
        self.track_list = TrackList(1, "My Playlist", self.default_tracks.copy())
        self.favorite = Favorite()
        self.musicplayer = MusicPlayer(self.default_tracks)

        # Views
        self.track_view = TrackView(self.view_frame)
        self.track_list_view = TrackListView(self.playlist_frame)
        self.favorite_view = FavoriteView(self.favorite_frame)
        self.musicplayer_view = MusicPlayerView(self.musicplayer_frame)

        # Controllers
        self.track_controller = TrackController(self.default_tracks[0], self.track_view)
        self.track_list_controller = TrackListController(self.track_list, self.track_list_view)
        self.favorite_controller = FavoriteController(self.favorite, self.favorite_view)
        self.musicplayer_controller = MusicPlayerController(self.musicplayer, self.musicplayer_view)

        # Layout each view
        self.track_view.get_frame().pack(fill="both", expand=True)
        self.track_list_view.get_frame().pack(fill="both", expand=True)
        self.favorite_view.get_frame().pack(fill="both", expand=True)
        self.musicplayer_view.get_frame().pack(fill="both", expand=True)

        # Bind buttons in track view
        self.track_view.btn_show.config(command=self.display_tracks)
        self.track_view.btn_detail.config(command=self.show_selected_detail)
        self.track_view.btn_add_fav.config(command=lambda: self.track_controller.add_to_favorite(self.track_list.get_tracks()[self.track_view.get_listbox().curselection()[0]]))

    def display_tracks(self):
        self.track_view.get_listbox().delete(0, tk.END)
        for track in self.track_list.get_tracks():
            self.track_view.get_listbox().insert(tk.END, f"{track.track_id}. {track.track_title} - {track.artist}")

    def show_selected_detail(self):
        selected_index = self.track_view.get_listbox().curselection()
        if selected_index:
            index = selected_index[0]
            selected_track = self.track_list.get_tracks()[index]
            self.track_controller.show_detail(selected_track)
        else:
            self.track_view.show_message("Please select a track first.")

if __name__ == "__main__":
    root = tk.Tk()
    app = JukeboxApp(root)
    root.mainloop()
