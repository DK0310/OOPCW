class Track:
    def __init__(self, track_id, track_title, artist, track_rating=0, play_count=0, mp3_path="", image_path=""):
        self.track_id = track_id
        self.track_title = track_title
        self.artist = artist
        self.track_rating = track_rating
        self.play_count = play_count
        self.mp3_path = mp3_path
        self.image_path = image_path

    def increment_play_count(self):
        self.play_count += 1

    def set_rating(self, rating):
        self.track_rating = rating

    @staticmethod
    def get_default_tracks():
        return [
            Track(1, "Imagine", "John Lennon", 5),
            Track(2, "Bohemian Rhapsody", "Queen", 4.8),
            Track(3, "Billie Jean", "Michael Jackson", 4.7),
        ]
