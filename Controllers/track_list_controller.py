class TrackListController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def add_track_to_list(self, track):
        self.model.add_track(track)
        self.view.show_message("Track added to playlist")

    def remove_track_from_list(self, track_id):
        self.model.remove_track(track_id)
        self.view.show_message(f"Track {track_id} removed from playlist")

    def print_tracks(self):
        tracks = self.model.get_all_tracks()
        self.view.display_track_list(tracks)

    def clear_playlist(self):
        self.model.clear_playlist()
        self.view.show_message("Playlist cleared")