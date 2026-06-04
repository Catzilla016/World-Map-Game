import tkinter as tk

from game_mode1 import *
from win_screen import *


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.geometry("1400x900")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frames = {}

        # Create all screens
        for FrameClass in (GameMode1, WinScreen):

            frame = FrameClass(container, self)

            name = FrameClass.__name__

            frame.main()

            self.frames[name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("GameMode1")

    def show_frame(self, name):

        frame = self.frames[name]

        frame.tkraise()
    
    def reset_frame(self, name):
        # Remove old game frame
        self.frames[name].destroy()

        # Create new game frame
        container = next(iter(self.frames.values())).master

        frame = GameMode1(container, self)
        self.frames[name] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        frame.main()

        self.show_frame(name)



app = App()
app.mainloop()