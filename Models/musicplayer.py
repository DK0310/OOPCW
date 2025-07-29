import pygame
import vlc
import os
import tempfile
from database.track_db import get_track, increase_play_count


class MusicPlayer:
    def __init__(self):
        self.current_track = None
        self.track_list = []
        if not pygame.mixer.get_init():
            pygame.mixer.init()
        os.add_dll_directory(r"C:\Program Files\VideoLAN\VLC")  
    
    def play_track(self, track):
        self.current_track = track
        if hasattr(self, 'vlc_player') and self.vlc_player.is_playing():
            self.vlc_player.stop()
        increase_play_count(track['track_id'])
        db_track = get_track(track['track_id'])
        mp3_data = db_track.get('mp3_file', None)
        if not mp3_data:
            print("No mp3 data found for this track.")
            return

        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_file:
           temp_file.write(mp3_data)
           temp_path = temp_file.name

    
        self.vlc_player = vlc.MediaPlayer(temp_path)
        
        self.vlc_player.play()
        

    def stop_track(self):
        if hasattr(self, 'vlc_player'):
            self.vlc_player.stop()
            self.current_track = None
        else:
            pass
        

    def get_current_track(self):
        return self.current_track

    def set_track_list(self, tracks):
        self.track_list = tracks


