import tkinter as tk

class TrackListView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.output_text = tk.Text(self.frame, width=60, height=15)
        self.output_text.pack(padx=10, pady=10)

    def display_track_list(self, text):
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, text)

    def get_frame(self):
        return self.frame
