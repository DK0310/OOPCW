class FavoriteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def remove_favorite(self, track):
        self.model.remove_favorite(track)

    def display_favorites(self):
        fav_tracks = self.model.get_favorite_track()
        self.view.display_favorites(fav_tracks)

    def clear_selected_favorite(self, index):
        fav_tracks = self.model.get_favorite_track()
        if 0 <= index < len(fav_tracks):
            track = fav_tracks[index]
            self.model.remove_favorite(track)
            self.display_favorites()
            self.view.show_message(f"Removed: {track.track_title}")
        else:
            self.view.show_message("Please select a track to remove!")

    def clear_all_favorites(self):
        self.model.clear_all_favorites()
        self.display_favorites()
        self.view.show_message("All favorite tracks cleared!")

    