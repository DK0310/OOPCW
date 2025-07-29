import tkinter as tk
from tkinter import messagebox

class TrackListView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.playlist_label = tk.Label(self.frame, text="Playlists", bg="#0A0F2C", fg="white")
        self.playlist_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.playlist_listbox = tk.Listbox(self.frame, width=40, height=8)
        self.playlist_listbox.pack(padx=10, pady=(0, 5))

        
        self.button_frame = tk.Frame(self.frame, bg="#0A0F2C")
        self.button_frame.pack(padx=10, pady=(0, 10), anchor="w")
        self.playlist_name_entry = tk.Entry(self.button_frame, width=20)
        self.playlist_name_entry.pack(side=tk.LEFT, padx=(0, 10))
        self.create_playlist_btn = tk.Button(self.button_frame, text="Create Playlist")
        self.create_playlist_btn.pack(side=tk.LEFT, padx=(0, 10))
        self.add_track_btn = tk.Button(self.button_frame, text="Add Track")
        self.add_track_btn.pack(side=tk.LEFT)
        self.clear_playlists_btn = tk.Button(self.button_frame, text="Clear Playlists")
        self.clear_playlists_btn.pack(side=tk.LEFT, padx=(10, 0))

        
        self.tracks_label = tk.Label(self.frame, text="Tracks in Playlist", bg="#0A0F2C", fg="white")
        self.tracks_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.tracks_listbox = tk.Listbox(self.frame, width=60, height=8)
        self.tracks_listbox.pack(padx=10, pady=(0, 10))

        
        self.add_track_frame = tk.Frame(self.frame, bg="#1A1F3C", bd=2, relief=tk.RIDGE)
        self.add_track_label = tk.Label(self.add_track_frame, text="All Tracks", bg="#1A1F3C", fg="white")
        self.add_track_label.pack(padx=10, pady=(10, 0), anchor="w")
        self.all_tracks_listbox = tk.Listbox(self.add_track_frame, width=60, height=8)
        self.all_tracks_listbox.pack(padx=10, pady=(0, 5))
        self.add_to_playlist_btn = tk.Button(self.add_track_frame, text="Add to Playlist")
        self.add_to_playlist_btn.pack(padx=10, pady=(0, 10))
        self.add_track_frame.pack_forget()  

    def get_frame(self):
        return self.frame

    def show_message(self, msg):
        messagebox.showinfo("Info", msg)

    def display_detail(self, detail):
        self.tracks_listbox.delete(0, tk.END)
        self.tracks_listbox.insert(tk.END, detail)

    def show_add_track_popup(self, all_tracks, add_callback):
        popup = tk.Toplevel(self.frame)
        popup.title("Add Track to Playlist")
        popup.geometry("700x400")
        popup.configure(bg="#1A1F3C")

        label = tk.Label(popup, text="Select a track to add", bg="#1A1F3C", fg="white")
        label.pack(pady=(10, 0))

        content_frame = tk.Frame(popup, bg="#1A1F3C")
        content_frame.pack(padx=10, pady=10, fill="both", expand=True)

        listbox = tk.Listbox(content_frame, width=40, height=10)
        for track in all_tracks:
            listbox.insert(
                tk.END,
                f"{track['track_id'] if isinstance(track, dict) else track.track_id}. "
                f"{track['track_name'] if isinstance(track, dict) else track.track_title} - "
                f"{track['artist'] if isinstance(track, dict) else track.artist}"
            )
        listbox.pack(side=tk.LEFT, fill="y")

        add_btn = tk.Button(popup, text="Add to Playlist", command=lambda: add_callback(all_tracks[listbox.curselection()[0]] if listbox.curselection() else None))
        add_btn.pack(pady=(0, 15))



