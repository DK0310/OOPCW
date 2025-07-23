import tkinter as tk

class FavoriteView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

        self.status_label = tk.Label(self.frame, text="Favorites", bg="#0A0F2C", fg="white")
        self.status_label.pack(pady=10)

        self.text_area = tk.Text(self.frame, width=50, height=10)
        self.text_area.pack(padx=10, pady=10)

    def display_favorites(self, text):
        self.text_area.delete("1.0", tk.END)
        self.text_area.insert(tk.END, text)

    def show_message(self, msg):
        self.status_label.config(text=msg)

    def get_frame(self):
        return self.frame

