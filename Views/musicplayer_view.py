import tkinter as tk
from PIL import Image, ImageTk


class MusicPlayerView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#1A1F3C")

        self.left_frame = tk.Frame(self.frame, bg="#222")
        self.left_frame.pack(side=tk.LEFT, fill=tk.Y)

        self.track_listbox = tk.Listbox(self.left_frame, width=30, height=20)
        self.track_listbox.pack(padx=10, pady=10)

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

        self.stop_btn = tk.Button(self.controls_frame, text="Stop")
        self.stop_btn.pack(side=tk.LEFT, padx=5, pady=5)


    def set_track_list(self, tracks):
        self.track_listbox.delete(0, tk.END)
        for track in tracks:
            name = track['track_name'] if isinstance(track, dict) else track.track_title
            artist = track['artist'] if isinstance(track, dict) else track.artist
            self.track_listbox.insert(tk.END, f"{name} - {artist}")

    def show_track_info(self, track):
        img_path = track['image_path'] if isinstance(track, dict) else track.image_path
        try:
            img = Image.open(img_path)
            img = img.resize((200, 200))
            photo = ImageTk.PhotoImage(img)
            self.cover_label.config(image=photo)
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