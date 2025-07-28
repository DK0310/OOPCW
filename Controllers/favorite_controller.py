from database.favorite_db import add_favorite, remove_favorite, clear_all_favorites, get_all_favorites
from Models.favorite import Favorite

class FavoriteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_favorites_listbox(self):
        self.view.fav_listbox.delete(0, 'end')
        for track in get_all_favorites():
            self.view.fav_listbox.insert('end', track['track_name'])

    def add_to_favorite(self, track):
        self.model.add_favorite(track)
        track_id = track['track_id'] if isinstance(track, dict) else track.track_id
        add_favorite(track_id)
        self.view.display_favorites(self.model.favorite_tracks)
        self.view.show_message("Track added to favorite!")

    def remove_selected_favorite(self, idx):
        idx = self.view.get_fav_listbox().curselection()
        if not idx:
            self.view.show_message("Please select a track to remove!")
            return
        track = self.model.favorite_tracks[idx[0]]
        self.model.remove_favorite(track)
        track_id = track['track_id'] if isinstance(track, dict) else track.track_id
        remove_favorite(track_id)
        self.view.display_favorites(self.model.favorite_tracks)
        self.view.show_message("Track removed from favorite.")

    def clear_all_favorites(self):
        clear_all_favorites()
        self.update_favorites_listbox()
        self.view.fav_listbox.delete(0, 'end')
        self.view.display_favorites(self.model.favorite_tracks)
        self.view.show_message("All favorite tracks cleared.")
