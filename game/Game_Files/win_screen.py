import tkinter as tk

class WinScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.configure(bg="#dff6ff")

        self.title = tk.Label(
            self,
            text="🏆 Congratulations!",
            font=("Arial", 36, "bold"),
            bg="#dff6ff"
        )

        self.subtitle = tk.Label(
            self,
            text="You found all 197 countries!",
            font=("Arial", 20),
            bg="#dff6ff"
        )
        

        self.stats_label = tk.Label(
            self,
            text="",
            font=("Arial", 16),
            bg="#dff6ff"
        )
        

        self.play_again = tk.Button(
            self,
            text="Play Again",
            font=("Arial", 16),
            width=20,
            command=self.play_again_func
        )
        

        self.menu_button = tk.Button(
            self,
            text="Main Menu",
            font=("Arial", 16),
            width=20,
            command=lambda: app.show_frame("MainMenu")
        )
        

    def main(self):
        self.title.pack(pady=(80, 20))
        self.subtitle.pack(pady=10)
        self.stats_label.pack(pady=20)
        self.play_again.pack(pady=10)
        self.menu_button.pack(pady=10)

    def play_again_func(self):
        self.app.reset_frame("GameMode1")
        