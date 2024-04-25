import tkinter as tk
from tkinter import ttk,Label,Entry,Button

class Frame3(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(bg='lavender')
        self.create_widgets()

    def create_widgets(self):
        pass