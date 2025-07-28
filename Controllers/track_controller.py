from database.track_db import get_track, get_all_tracks
from database.favorite_db import is_favorite, add_favorite
from tkinter import messagebox
class TrackController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def show_detail(self):
        selection = self.track_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        track_id = self.track_id_map[idx]
        track = get_track(track_id)
        if track:
            rating = track.get('rating', 0)
            detail = f"Track: {track['track_name']}\nArtist: {track['artist']}\nPlay count: {track['play_count']}\nID: {track['track_id']}\nRating: {track['rating']}"
            self.display_detail(detail)
        else:
            self.display_detail("No track information found.")

    def auto_add_favorite(self):
        tracks = get_all_tracks()
        for track in tracks:
            if track.get('play_count', 0) >= 5:
                if not is_favorite(track['track_id']):
                    add_favorite(track['track_id'])
    
    def add_to_favorite(self):
        selection = self.track_listbox.curselection()
        if not selection:
            messagebox.showerror("Error", "Please select a track!")
            return
        idx = selection[0]
        track_id = self.track_id_map[idx]
        add_favorite(track_id)
        messagebox.showinfo("Success", "Track added to favorite!")

    
    def show_detail(self, track):
        if isinstance(track, dict):
            detail = (
                f"ID: {track.get('track_id', '')}\n"
                f"Title: {track.get('track_name', track.get('track_title', ''))}\n"
                f"Artist: {track.get('artist', '')}\n"
                f"Rating: {track.get('rating', '')}\n"
                f"Play Count: {track.get('play_count', '')}"
            )
        else:
            detail = (
                f"ID: {track.track_id}\n"
                f"Title: {track.track_title}\n"
                f"Artist: {track.artist}\n"
                f"Rating: {track.rating}\n"
                f"Play Count: {track.play_count}"
            )
        self.view.display_detail(detail)
