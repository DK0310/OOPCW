from database.favorite_db import remove_favorite, clear_all_favorites, get_all_favorites

class FavoriteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def remove_selected_favorite(self, track_id):
        remove_favorite(track_id)
        self.model.favorite_tracks = get_all_favorites()
        self.view.display_favorites(self.model.favorite_tracks)
        self.view.show_message("Track removed from favorite.")

    def clear_all_favorites(self):
        clear_all_favorites()
        self.view.show_message("All favorite tracks cleared.")
