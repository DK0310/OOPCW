import tkinter as tk
from tkinter import messagebox

class FavoriteView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.status_label = tk.Label(self.frame, text="Favorites", bg="#0A0F2C", fg="white")
        self.status_label.pack(pady=10)

        self.fav_listbox = tk.Listbox(self.frame, width=50, height=10)
        self.fav_listbox.pack(padx=10, pady=10)

        btn_frame = tk.Frame(self.frame, bg="#0A0F2C")
        btn_frame.pack(pady=(0, 10))
        self.clear_track_btn = tk.Button(btn_frame, text="Clear Track")
        self.clear_track_btn.pack(side=tk.LEFT, padx=10)
        self.clear_all_btn = tk.Button(btn_frame, text="Clear All Tracks")
        self.clear_all_btn.pack(side=tk.LEFT, padx=10)

    def display_favorites(self, fav_tracks):
        self.fav_listbox.delete(0, tk.END)
        for track in fav_tracks:
            self.fav_listbox.insert(tk.END, f"{track.track_id}. {track.track_title} - {track.artist}")

    def show_message(self, msg):
        messagebox.showinfo("Info", msg)

    def get_frame(self):
        return self.frame

    def get_listbox(self):
        return self.fav_listbox

