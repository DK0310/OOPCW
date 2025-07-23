class MusicPlayer:
    def __init__(self, tracks):
        self.tracks = tracks
        self.current_index = 0

    def get_current_track(self):
        return self.tracks[self.current_index] if self.tracks else None

