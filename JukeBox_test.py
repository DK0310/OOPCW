import unittest
from Models.track import Track
from Models.track_list import TrackList
from Models.favorite import Favorite
from Models.musicplayer import MusicPlayer

class TestTrack(unittest.TestCase):
    def setUp(self):
        self.track1 = Track(1, "Song A", "Artist X")
        self.track2 = Track(2, "Song B", "Artist Y")

    def test_update_track(self):
        self.track1.track_title = "Song A Updated"
        self.track1.artist = "Artist Z"
        self.assertEqual(self.track1.track_title, "Song A Updated")
        self.assertEqual(self.track1.artist, "Artist Z")

    def test_show_detail(self):
        detail = f"Track: {self.track1.track_title}, Artist: {self.track1.artist}"
        self.assertEqual(detail, "Track: Song A, Artist: Artist X")

    def test_create_track(self):
        self.assertEqual(self.track1.track_title, "Song A")
        self.assertEqual(self.track2.artist, "Artist Y")

class TestPlaylist(unittest.TestCase):
    def setUp(self):
        self.track1 = Track(1, "Song A", "Artist X")
        self.track2 = Track(2, "Song B", "Artist Y")
        self.playlist = TrackList(1, [self.track1])

    def test_add_track(self):
        self.playlist.tracks.append(self.track2)
        self.assertIn(self.track2, self.playlist.tracks)

    
    def test_clear_playlist(self):
        self.playlist.tracks.append(self.track2)
        self.playlist.tracks.clear()
        self.assertEqual(len(self.playlist.tracks), 0)

    
class TestFavorite(unittest.TestCase):
    def setUp(self):
        self.track1 = Track(1, "Song A", "Artist X")
        self.track2 = Track(2, "Song B", "Artist Y")
        self.favorite = Favorite()

    def test_add_favorite(self):
        self.favorite.favorite_tracks.append(self.track1)
        self.assertIn(self.track1, self.favorite.favorite_tracks)
        self.favorite.favorite_tracks.append(self.track1)
        self.assertEqual(self.favorite.favorite_tracks.count(self.track1), 2)

    def test_clear_favorite(self):
        self.favorite.favorite_tracks.append(self.track1)
        self.favorite.favorite_tracks.append(self.track2)
        self.favorite.favorite_tracks.clear()
        self.assertEqual(len(self.favorite.favorite_tracks), 0)

class TestMusicPlayer(unittest.TestCase):
    def setUp(self):
        self.track1 = Track(1, "Song A", "Artist X")
        self.musicplayer = MusicPlayer()

    def test_play_stop_music(self):
        self.musicplayer.play_track(self.track1)
        self.assertEqual(self.musicplayer.current_track, self.track1)
        self.musicplayer.stop_track()
        self.assertIsNone(self.musicplayer.current_track)

if __name__ == '__main__':
    unittest.main()