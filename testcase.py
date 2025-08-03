import unittest
from Models.track import Track

class TestAddTrackA(unittest.TestCase):
    def setUp(self):
        self.track1 = Track(1, "Song A", "Artist X")
        self.track2 = Track(2, "Song B", "Artist Y")

    def test_create_track(self):
        self.assertEqual(self.track1.track_title, "Song A")
        self.assertEqual(self.track2.artist, "Artist Y")

if __name__ == '__main__':
    unittest.main()