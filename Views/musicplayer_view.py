import tkinter as tk
import io
from PIL import Image, ImageTk
from database.track_db import get_track
from .BaseView import BaseView

class MusicPlayerView(BaseView):
    def __init__(self, parent_frame):
        self.base_view = BaseView(parent_frame)
        super().__init__(parent_frame)
        

        self.left_frame = tk.Frame(self.frame, bg="#222")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.track_listbox = tk.Listbox(self.left_frame, width=30, height=20)
        self.track_listbox.pack(padx=10, pady=10)
        self.track_listbox.bind("<<ListboxSelect>>", self.on_select_track)

        self.right_frame = tk.Frame(self.frame, bg="#1A1F3C")
        self.right_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.cover_label = tk.Label(self.right_frame, bg="#1A1F3C")
        self.cover_label.pack(pady=(20, 10))

        self.info_label = tk.Label(self.right_frame, text="", font=("Arial", 16), fg="white", bg="#1A1F3C")
        self.info_label.pack(pady=(0, 20))

        self.controls_frame = tk.Frame(self.right_frame, bg="#1A1F3C")
        self.controls_frame.pack(pady=10)

        self.play_btn = tk.Button(self.controls_frame, text="Play")
        self.play_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.pause_btn = tk.Button(self.controls_frame, text="Pause")
        self.pause_btn.pack(side=tk.LEFT, padx=5, pady=5)

        self.time_label = tk.Label(self.right_frame, text="00:00 / 00:00", font=("Arial", 12), fg="white", bg="#1A1F3C")
        self.time_label.pack(pady=(0, 10))

    def on_select_track(self, _):
        selection = self.track_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        if hasattr(self, "tracks") and idx < len(self.tracks):
            self.show_track_info(self.tracks[idx])

    def set_track_list(self, tracks):
        self.tracks = tracks
        self.track_listbox.delete(0, tk.END)
        for track in tracks:
            name = track['track_name'] if isinstance(track, dict) else track.track_title
            artist = track['artist'] if isinstance(track, dict) else track.artist
            self.track_listbox.insert(tk.END, f"{name} - {artist}")

    def show_track_info(self, track):
        db_img = get_track(track['track_id']) 
        img_data = db_img['image_file'] if db_img else None
        try:
            if isinstance(img_data, bytes):
                img = Image.open(io.BytesIO(img_data))
            else:
                raise Exception("No image data")
            img = img.resize((300, 200))
            photo = ImageTk.PhotoImage(img)
            self.cover_label.config(image=photo, text="")
            self.cover_label.image = photo
        except Exception:
            self.cover_label.config(image="", text="No Image", fg="white")

        name = track['track_name'] if isinstance(track, dict) else track.track_title
        artist = track['artist'] if isinstance(track, dict) else track.artist
        self.info_label.config(text=f"{name}\n{artist}")

    def get_frame(self):
        return self.frame

    def print(self, message):
        print(message)
    
    def update_time(self, current_ms, total_ms):
        def format_time(ms):
            s = int(ms // 1000)
            return f"{s//60:02}:{s%60:02}"
        self.time_label.config(text=f"{format_time(current_ms)} / {format_time(total_ms)}")