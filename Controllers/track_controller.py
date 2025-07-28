from database.track_db import get_track, get_all_tracks, delete_track, update_track
from database.favorite_db import add_favorite, get_all_favorites
from Views.favorite_view import FavoriteView
from tkinter import messagebox

class TrackController:
    def __init__(self, model, view, favorite_view):
        self.model = model
        self.view = view
        self.favorite_view = favorite_view

    def add_to_favorite(self):
        selection = self.view.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a track!")
            return
        idx = selection[0]
        track_id = self.view.track_id_map[idx]
        add_favorite(track_id)
        fav_tracks = get_all_favorites()
        self.favorite_view.display_favorites(fav_tracks)
        messagebox.showinfo("Success", "Track added to favorite!")

    def delete_track(self):
        selection = self.view.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a track to delete!")
            return
        idx = selection[0]
        track_id = self.view.track_id_map[idx]
        delete_track(track_id)
        self.load_tracks()
        messagebox.showinfo("Success", "Track deleted successfully!")

    def update_track(self):
        selection = self.view.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a track to update!")
            return
        idx = selection[0]
        track_id = self.view.track_id_map[idx]
        track = get_track(track_id)
        if not track:
            messagebox.showerror("Error", "Track not found!")
            return
        self.view.show_update_track_popup(track, self.load_tracks)

    def show_detail(self):
        selection = self.view.track_listbox.curselection()
        if not selection:
            self.view.display_detail("No track selected.")
            return
        idx = selection[0]
        track_id = self.view.track_id_map[idx]
        track = get_track(track_id)
        if track:
            detail = (
                f"ID: {track.get('track_id', '')}\n"
                f"Title: {track.get('track_name', track.get('track_title', ''))}\n"
                f"Artist: {track.get('artist', '')}\n"
                f"Rating: {track.get('rating', '')}\n"
                f"Play Count: {track.get('play_count', '')}"
            )
            self.view.display_detail(detail)
        else:
            self.view.display_detail("No track information found.")

    def load_tracks(self):
        tracks = get_all_tracks()
        self.view.display_tracks(tracks)