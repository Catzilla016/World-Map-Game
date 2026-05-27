import tkinter as tk

class WinScreen(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        self.back_button = tk.Button(
            self,
            text="Back",
            command=lambda: app.show_frame("MainMenu")
        )
    
    def main(self):
        self.back_button.pack()

        self.root.mainloop()
