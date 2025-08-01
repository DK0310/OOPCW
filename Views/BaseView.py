import tkinter as tk

class BaseView:
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")