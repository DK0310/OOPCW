import tkinter as tk
from abc import ABC, abstractmethod

class BaseView(ABC):
    def __init__(self, parent_frame):
        self.frame = tk.Frame(parent_frame, bg="#0A0F2C")

    @abstractmethod
    def get_frame(self):
        pass

    