import tkinter as tk

class MusicPlayerView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.status_label = tk.Label(self.frame, text="Now Playing", bg="#0A0F2C", fg="white")
        self.status_label.pack(pady=10)

        self.track_display = tk.Text(self.frame, width=50, height=6)
        self.track_display.pack(padx=10, pady=10)

    def display_now_playing(self, track_info):
        self.track_display.delete("1.0", tk.END)
        self.track_display.insert(tk.END, track_info)

    def show_message(self, msg):
        self.status_label.config(text=msg)

    def get_frame(self):
        return self.frame