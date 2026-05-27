import tkinter as tk

from game_mode1 import *
from win_screen import *


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.geometry("1400x800")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Create all screens
        for FrameClass in (MainMenu, GameMode1, WinScreen):

            frame = FrameClass(container, self)

            name = FrameClass.__name__

            self.frames[name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, name):

        frame = self.frames[name]

        frame.tkraise()


app = App()
app.mainloop()