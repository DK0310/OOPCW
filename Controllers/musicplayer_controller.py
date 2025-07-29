class MusicPlayerController:
    def __init__(self, model, view):
        self.model = model
        self.view = view

    def play(self, track):
        self.model.play_track(track)
        if track:
            if isinstance(track, dict):
                title = track.get('track_name', '')
                artist = track.get('artist', '')
            else:
                title = getattr(track, 'track_name', '')
                artist = getattr(track, 'artist', '')
            self.view.print(f"Playing: {title} by {artist}")
        else:
            self.view.print("No track selected to play.")

    def stop(self):
        self.model.stop_track()
        self.view.print("Stopped.")