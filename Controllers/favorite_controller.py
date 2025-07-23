class FavoriteController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def remove_favorite(self, track):
        self.model.remove_favorite(track)

    def play_track(self, track):
        # Simulate track playback
        print(f"Now playing: {track.track_title} by {track.artist}")