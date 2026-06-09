import tkinter as tk

from game_mode_normal import *
from win_screen import *
from game_mode_timed import *
from game_mode_border import *
from main_menu import *


class App(tk.Tk):

    def __init__(self):

        super().__init__()

        self.geometry("1400x900")

        container = tk.Frame(self)
        container.pack(fill="both", expand=True)

        self.frame_classes = {
            "GameMode1": GameMode1,
            "GameMode2": GameMode2,
            "GameMode3": GameMode3,
            "WinScreen": WinScreen,
            "MainMenu": MainMenu
        }

        self.frames = {}

        # Create all screens
        for FrameClass in (GameMode1, GameMode2, GameMode3, WinScreen, MainMenu):

            frame = FrameClass(container, self)

            name = FrameClass.__name__

            frame.main()

            self.frames[name] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainMenu")

    def show_frame(self, name, time=None):

        frame = self.frames[name]
        
        if name == "WinScreen" and time is not None:
            frame.set_time(time)

        frame.tkraise()
    
    def reset_frame(self, name):
        self.frames[name].destroy()

        container = next(iter(self.frames.values())).master

        FrameClass = self.frame_classes[name]

        frame = FrameClass(container, self)

        self.frames[name] = frame

        frame.grid(row=0, column=0, sticky="nsew")
        frame.main()

        self.show_frame(name)



app = App()
app.mainloop()