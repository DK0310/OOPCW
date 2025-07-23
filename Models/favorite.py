class Favorite:
    def __init__(self):
        self.favorite_tracks = []

    def add_favorite(self, track):
        if track not in self.favorite_tracks:
            self.favorite_tracks.append(track)

    def remove_favorite(self, track):
        if track in self.favorite_tracks:
            self.favorite_tracks.remove(track)

    def get_favorite_track(self):
        return self.favorite_tracks