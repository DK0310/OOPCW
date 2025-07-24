from .track import Track

class TrackList:
    # Lưu trữ tất cả các playlist tạm thời
    all_playlists = []
    _next_id = 1

    def __init__(self, track_list_id: int, title: str, tracks: list[Track] = None):
        self.track_list_id = track_list_id
        self.title = title
        self.tracks: list[Track] = tracks if tracks is not None else []

    def get_tracks(self):
        return self.tracks

    @classmethod
    def add_playlist(cls, title: str):
        playlist = TrackList(cls._next_id, title)
        cls.all_playlists.append(playlist)
        cls._next_id += 1
        return playlist

    @classmethod
    def get_all_playlists(cls):
        return cls.all_playlists

    @classmethod
    def clear_all_playlists(cls):
        cls.all_playlists = []
        cls._next_id = 1

