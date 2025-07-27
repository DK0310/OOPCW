import tkinter as tk
from tkinter import filedialog, messagebox
from database.favorite_db import add_favorite
from database.track_db import get_all_tracks, get_track, create_track

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
        self.btn_add_fav.grid(row=0, column=0, padx=10, pady=10)

        # Thêm nút Add Track
        self.btn_add_track = tk.Button(self.frame, text="Add Track", command=self.show_add_track_popup)
        self.btn_add_track.grid(row=2, column=0, padx=10, pady=10, sticky="w")

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
            detail = f"Track: {track['track_name']}\nArtist: {track['artist']}\nPlay count: {track['play_count']}\nID: {track['track_id']}\nRating: {track['rating']}"
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

    def show_add_track_popup(self):
        popup = tk.Toplevel(self.frame)
        popup.title("Add New Track")

        tk.Label(popup, text="Track Name:").grid(row=0, column=0, sticky="e")
        entry_name = tk.Entry(popup)
        entry_name.grid(row=0, column=1)

        tk.Label(popup, text="Artist:").grid(row=1, column=0, sticky="e")
        entry_artist = tk.Entry(popup)
        entry_artist.grid(row=1, column=1)

        tk.Label(popup, text="Rating:").grid(row=2, column=0, sticky="e")
        entry_rating = tk.Entry(popup)
        entry_rating.grid(row=2, column=1)

        tk.Label(popup, text="Image Path:").grid(row=3, column=0, sticky="e")
        entry_image = tk.Entry(popup)
        entry_image.grid(row=3, column=1)
        btn_browse_img = tk.Button(popup, text="Browse", command=lambda: entry_image.insert(0, filedialog.askopenfilename(filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])) )
        btn_browse_img.grid(row=3, column=2)

        tk.Label(popup, text="MP3 Path:").grid(row=4, column=0, sticky="e")
        entry_mp3 = tk.Entry(popup)
        entry_mp3.grid(row=4, column=1)
        btn_browse_mp3 = tk.Button(popup, text="Browse", command=lambda: entry_mp3.insert(0, filedialog.askopenfilename(filetypes=[("MP3 files", "*.mp3")])) )
        btn_browse_mp3.grid(row=4, column=2)

        def add_track_to_db():
            name = entry_name.get()
            artist = entry_artist.get()
            try:
                rating = float(entry_rating.get())
            except ValueError:
                rating = 0
            image_path = entry_image.get()
            mp3_path = entry_mp3.get()
            play_count = 0

            if not name or not artist or not mp3_path:
                messagebox.showerror("Error", "Track name, artist, and mp3 file are required!")
                return

            # Gọi hàm tạo track trong database
            create_track(track_name=name, artist=artist, play_count=0, rating=rating, mp3_path=mp3_path, image_path=image_path)
            messagebox.showinfo("Success", "Track added successfully!")
            popup.destroy()
            self.load_tracks()

        btn_add = tk.Button(popup, text="Add Track", command=add_track_to_db)
        btn_add.grid(row=5, column=0, columnspan=3, pady=10)




