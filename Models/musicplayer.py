from database.track_db import get_all_tracks

class MusicPlayer:
    def __init__(self):
        # Lấy danh sách track từ track_db
        self.tracks = get_all_tracks()

    def get_tracks(self):
        return self.tracks

