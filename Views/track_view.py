import tkinter as tk
from database.favorite_db import add_favorite
from database.track_db import get_all_tracks, get_track

class TrackView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.track_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.track_listbox.grid(row=1, column=0, padx=10, pady=10)
        self.track_listbox.bind("<<ListboxSelect>>", self.on_track_select)

        self.track_txt = tk.Text(self.frame, width=30, height=6, wrap="none")
        self.track_txt.grid(row=1, column=1, sticky="NW", padx=10, pady=10)


        self.btn_detail = tk.Button(self.frame, text="Show Detail", state="disabled", command=self.show_detail)
        self.btn_detail.grid(row=0, column=1, padx=10, pady=10)

        self.btn_add_fav = tk.Button(self.frame, text="Add to Favorite", state="disabled")
        self.btn_add_fav.grid(row=0, column=2, padx=10, pady=10)

        self.track_id_map = []  # Lưu track_id tương ứng với từng dòng trong listbox

    def on_track_select(self, event):
        selection = self.track_listbox.curselection()
        if selection:
            self.btn_detail.config(state="normal")
            self.btn_add_fav.config(state="normal")
        else:
            self.btn_detail.config(state="disabled")
            self.btn_add_fav.config(state="disabled")

    def load_tracks(self):
        self.track_listbox.delete(0, tk.END)
        self.track_id_map = []
        tracks = get_all_tracks()
        for track in tracks:
            display_text = f"{track['track_name']} - {track['artist']} (Rating: {track.get('rating', 0)})"
            self.track_listbox.insert(tk.END, display_text)
            self.track_id_map.append(track['track_id'])

    def show_detail(self):
        selection = self.track_listbox.curselection()
        if not selection:
            return
        idx = selection[0]
        track_id = self.track_id_map[idx]
        track = get_track(track_id)
        
        if track:
            rating = track.get('rating', 0)
            #detail = f"Track: {track['track_name']}\nArtist: {track['artist']}\nPlay count: {track['play_count']}\nID: {track['track_id']}\nRating: {rating}"
            
            self.display_detail(detail)
        else:
            self.display_detail("No track information found.")

    def set_add_fav_callback(self, callback):
        self.btn_add_fav.config(command=callback)

    def get_frame(self):
        return self.frame

    def get_listbox(self):
        return self.track_listbox

    def display_detail(self, text):
        self.track_txt.delete("1.0", tk.END)
        self.track_txt.insert(tk.END, text)


    

 