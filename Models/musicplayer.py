import pygame
import os
from pydub import AudioSegment
import io
import base64
from database.track_db import get_track

class MusicPlayer:
    def __init__(self):
        self.current_track = None
        self.track_list = []
        if not pygame.mixer.get_init():
            pygame.mixer.init()

    
    def play_track(self, track):
        self.current_track = track
        db_track = get_track(track['track_id'])
        mp3_data = db_track.get('mp3_file', None)
        mp3_data = base64.b64decode(mp3_data)
        if not mp3_data:
            print("No mp3 data found for this track.")
            return

    
        mp3_stream = io.BytesIO(mp3_data)
        audio = AudioSegment.from_file(mp3_stream, format="mp3")
        wav_stream = io.BytesIO()
        audio.export(wav_stream, format="wav")
        wav_stream.seek(0)

    
        pygame.mixer.music.load(wav_stream)
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play()

    def stop_track(self):
        pygame.mixer.music.stop()
        self.current_track = None

    def get_current_track(self):
        return self.current_track

    def set_track_list(self, tracks):
        self.track_list = tracks


