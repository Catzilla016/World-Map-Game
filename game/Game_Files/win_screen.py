import tkinter as tk

class WinScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)

        self.app = app

        self.configure(bg="#dff6ff")
        
        self.time = 0

        self.title = tk.Label(
            self,
            text="🏆 Congratulations!",
            font=("Arial", 36, "bold"),
            bg="#dff6ff"
        )

        self.subtitle = tk.Label(
            self,
            text="You Won!",
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
        self.time_label = tk.Label(
            self,
            text="",
            font=("Arial", 16),
            bg="#dff6ff"
        )
        

    def main(self):
        self.title.pack(pady=(80, 20))
        self.subtitle.pack(pady=10)
        self.stats_label.pack(pady=20)
        self.play_again.pack(pady=10)
        self.menu_button.pack(pady=10)
        self.time_label.pack(pady=10)
        
        if self.time != 0:
            minutes = self.time // 60
            seconds = self.time % 60
            
            self.time_label.config(
                text=f"{minutes}:{seconds:02d}"
            )

    def play_again_func(self):
        if self.time !=0 :
            self.app.reset_frame("GameMode2")
        else:
            self.app.reset_frame("GameMode1")
    
    def set_time(self, time):
        self.time = time

        minutes = time // 60
        seconds = time % 60

        self.time_label.config(
            text=f"Time: {minutes}:{seconds:02d}"
        )