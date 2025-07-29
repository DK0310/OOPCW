from database.favorite_db import get_all_favorites
class Favorite:
    def __init__(self):
        self.favorite_tracks = get_all_favorites()

    def get_favorite_tracks(self):
        return self.favorite_tracks
