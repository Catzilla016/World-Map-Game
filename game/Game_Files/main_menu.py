import tkinter as tk


class MainMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app
        self.app.title("Country Guessr")

        self.configure(bg="#1e1e1e")  # dark background

        self.WIDTH = 1400
        self.HEIGHT = 800

        # Center container
        self.container = tk.Frame(self, bg="#1e1e1e")
        self.container.place(relx=0.5, rely=0.5, anchor="center")

        button_style = {
            "width": 20,
            "height": 2,
            "font": ("Arial", 14),
            "bg": "#2d2d2d",
            "fg": "white",
            "activebackground": "#444",
            "activeforeground": "white",
            "bd": 0,
            "cursor": "hand2"
        }

        self.title_label = tk.Label(
            self.container,
            text="Country Guessr",
            font=("Arial", 28, "bold"),
            bg="#1e1e1e",
            fg="white"
        )

        self.game_mode_normal_button = tk.Button(
            self.container,
            text="Normal Mode",
            command=self.game_mode_normal_func,
            **button_style
        )

        self.game_mode_normal_timed = tk.Button(
            self.container,
            text="Timed Mode",
            command=self.game_mode_timed_func,
            **button_style
        )

        self.game_mode_border = tk.Button(
            self.container,
            text="Border Mystery",
            command=self.game_mode_border_func,
            **button_style
        )
        
        
    def main(self):
        self.title_label.pack(pady=(0, 30))
        self.game_mode_normal_button.pack(pady=10)
        self.game_mode_normal_timed.pack(pady=10)
        self.game_mode_border.pack(pady=10)
        

    def game_mode_normal_func(self):
        self.app.reset_frame("GameMode1")
        self.app.show_frame("GameMode1")

    def game_mode_timed_func(self):
        self.app.reset_frame("GameMode2")
        self.app.show_frame("GameMode2")

    def game_mode_border_func(self):
        self.app.reset_frame("GameMode3")
        self.app.show_frame("GameMode3")