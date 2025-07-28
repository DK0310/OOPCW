from database.favorite_db import remove_favorite, clear_all_favorites, get_all_favorites

class FavoriteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def update_favorites_listbox(self):
        self.view.fav_listbox.delete(0, 'end')
        for track in get_all_favorites():
            self.view.fav_listbox.insert('end', track['track_name'])

    def remove_selected_favorite(self, idx):
        fav_tracks = get_all_favorites()
        if not fav_tracks or idx < 0 or idx >= len(fav_tracks):
            self.view.show_message("Please select a valid track to remove!")
            return
        track = fav_tracks[idx]
        track_id = track['track_id'] if isinstance(track, dict) else track.track_id
        remove_favorite(track_id)
        # Cập nhật lại giao diện
        self.view.display_favorites(get_all_favorites())
        self.view.show_message("Track removed from favorite.")

    def clear_all_favorites(self):
        clear_all_favorites()
        self.update_favorites_listbox()
        self.view.fav_listbox.delete(0, 'end')
        self.view.display_favorites(self.model.favorite_tracks)
        self.view.show_message("All favorite tracks cleared.")
