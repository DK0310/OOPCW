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

# --- Khởi tạo Tkinter và các biến toàn cục ---
root = tk.Tk()
root.title("Jukebox Simulation")
root.geometry("900x650")
root.configure(bg="#0A0F2C")

fonts.configure()

notebook = ttk.Notebook(root)
notebook.pack(fill='both', expand=True)

# Tabs
view_frame = tk.Frame(notebook, bg="#0A0F2C")
playlist_frame = tk.Frame(notebook, bg="#0A0F2C")
favorite_frame = tk.Frame(notebook, bg="#0A0F2C")
musicplayer_frame = tk.Frame(notebook, bg="#0A0F2C")

notebook.add(view_frame, text="View Tracks")
notebook.add(playlist_frame, text="Playlist")
notebook.add(favorite_frame, text="Favorite")
notebook.add(musicplayer_frame, text="Music Player")

# Lấy dữ liệu track từ database
tracks = get_all_tracks()
track_list = get_all_tracklists()
favorite_model = Favorite()
musicplayer = MusicPlayer()

# Views
track_view = TrackView(view_frame)
track_list_view = TrackListView(playlist_frame)
favorite_view = FavoriteView(favorite_frame)
musicplayer_view = MusicPlayerView(musicplayer_frame)

# Controllers
track_controller = TrackController(None, track_view, favorite_view)
track_list_controller = TrackListController(track_list, track_list_view)
favorite_controller = FavoriteController(favorite_model, favorite_view)
musicplayer_controller = MusicPlayerController(musicplayer, musicplayer_view)

# Layout each view
track_view.get_frame().pack(fill="both", expand=True)
track_list_view.get_frame().pack(fill="both", expand=True)
favorite_view.get_frame().pack(fill="both", expand=True)
musicplayer_view.get_frame().pack(fill="both", expand=True)

# --- Callback functions ---
def display_tracks():
    global tracks
    tracks = get_all_tracks()
    track_view.get_listbox().delete(0, tk.END)
    track_view.track_id_map = []
    for track in tracks:
        track_view.get_listbox().insert(
            tk.END, f"{track['track_id']}. {track['track_name']} - {track['artist']})"
        )
        track_view.track_id_map.append(track['track_id'])

def display_favorites():
    fav_tracks = get_all_favorites()
    favorite_view.display_favorites(fav_tracks)

def display_musicplayer():
    musicplayer.set_track_list(tracks)
    musicplayer_view.set_track_list(tracks) 

def show_all_playlists():
    track_list_controller.update_playlist_listbox()
    playlists = get_all_tracklists()
    if playlists:
        track_list_controller.update_tracks_listbox_by_id(playlists[0]['tracklist_id'])

def show_selected_detail():
    track_controller.show_detail()

def create_playlist_callback():
    title = track_list_view.playlist_name_entry.get()
    track_list_controller.create_playlist(title)
    track_list_view.playlist_name_entry.delete(0, 'end')

def add_track_popup_callback():
    all_tracks = get_all_tracks()
    playlist_index = track_list_view.playlist_listbox.curselection()
    if not playlist_index:
        track_list_view.show_message("Please select a playlist first!")
        return
    playlist_index = playlist_index[0]
    track_list_controller.show_add_track_popup(all_tracks, playlist_index)

def on_playlist_select(event):
    selection = track_list_view.playlist_listbox.curselection()
    if not selection:
        track_list_view.tracks_listbox.delete(0, 'end')
        return
    playlist_index = selection[0]
    playlists = get_all_tracklists()
    if 0 <= playlist_index < len(playlists):
        playlist_id = playlists[playlist_index]['tracklist_id']
        track_list_controller.update_tracks_listbox_by_id(playlist_id)
    else:
        track_list_view.tracks_listbox.delete(0, 'end')

def clear_playlists_callback():
    track_list_controller.clear_all_playlists()

def clear_selected_favorite_callback():
    selection = favorite_view.get_fav_listbox().curselection()
    if not selection:
        favorite_view.show_message("Please select a track to remove!")
        return
    index = selection[0]
    favorite_controller.remove_selected_favorite(index)

def clear_all_favorites_callback():
    favorite_controller.clear_all_favorites()
    display_favorites()

def add_to_favorite_callback():
    track_controller.add_to_favorite()

def delete_track_callback():
    track_controller.delete_track()

def update_track_callback():
    track_controller.update_track()

def play_track_callback():
    selection = musicplayer_view.track_listbox.curselection()
    if not selection:
        musicplayer_view.print("Please select a track to play.")
        return
    idx = selection[0]
    track = musicplayer.track_list[idx]
    musicplayer_controller.play(track)

def stop_track_callback():
    musicplayer_controller.stop()

# --- Bind buttons ---
track_view.btn_detail.config(command=show_selected_detail)
track_view.btn_add_fav.config(command=add_to_favorite_callback)
track_view.btn_del_track.config(command=delete_track_callback)
track_view.uptrack_btn.config(command=update_track_callback)

track_list_view.create_playlist_btn.config(command=create_playlist_callback)
track_list_view.add_track_btn.config(command=add_track_popup_callback)
track_list_view.playlist_listbox.bind('<<ListboxSelect>>', on_playlist_select)
track_list_view.clear_playlists_btn.config(command=clear_playlists_callback)

favorite_view.clear_track_btn.config(command=clear_selected_favorite_callback)
favorite_view.clear_all_btn.config(command=clear_all_favorites_callback)

musicplayer_view.play_btn.config(command=play_track_callback)
musicplayer_view.pause_btn.config(command=stop_track_callback)

# --- Hiển thị dữ liệu khi khởi động ---
display_tracks()
show_all_playlists()
display_favorites()
display_musicplayer()

root.mainloop()
