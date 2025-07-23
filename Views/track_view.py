import tkinter as tk

class TrackView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.track_listbox = tk.Listbox(self.frame, width=50, height=15)
        self.track_listbox.grid(row=1, column=0, padx=10, pady=10)
        self.track_listbox.bind("<<ListboxSelect>>", self.on_track_select)

        self.track_txt = tk.Text(self.frame, width=30, height=6, wrap="none")
        self.track_txt.grid(row=1, column=1, sticky="NW", padx=10, pady=10)

        self.btn_show = tk.Button(self.frame, text="Show Tracks")
        self.btn_show.grid(row=0, column=0, padx=10, pady=10)

        self.btn_detail = tk.Button(self.frame, text="Show Detail", state="disabled")
        self.btn_detail.grid(row=0, column=1, padx=10, pady=10)

        self.btn_add_fav = tk.Button(self.frame, text="Add to Favorite", state="disabled")
        self.btn_add_fav.grid(row=0, column=2, padx=10, pady=10)

    def on_track_select(self, event):
        selection = self.track_listbox.curselection()
        if selection:
            self.btn_detail.config(state="normal")
            self.btn_add_fav.config(state="normal")
        else:
            self.btn_detail.config(state="disabled")
            self.btn_add_fav.config(state="disabled")

    def set_add_fav_callback(self, callback):
        self.btn_add_fav.config(command=callback)

    def get_frame(self):
        return self.frame

    def get_listbox(self):
        return self.track_listbox

    def display_detail(self, text):
        self.track_txt.delete("1.0", tk.END)
        self.track_txt.insert(tk.END, text)

    

 