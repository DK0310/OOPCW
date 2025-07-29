from .track import Track

class TrackList:
    def __init__(self, track_list_id: int, title: str, tracks: list[Track] = None):
        self.track_list_id = track_list_id
        self.title = title
        self.tracks: list[Track] = tracks if tracks is not None else []

    def get_tracks(self):
        return self.tracks


