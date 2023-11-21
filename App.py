import tkinter as tk
from LoginWindow import LoginWindow

# App class represents the main application window.
class App(tk.Tk):
    def __init__(self, metrics_calculator):
        super().__init__()
        self.title('METRICSTICS')
        self.geometry('850x400')
        self.resizable(False, False)
        self.metrics_calculator = metrics_calculator
        self.login_window = LoginWindow(self, self)
        self.withdraw()  # Hide the main window initially

    def show_main_window(self):
        self.deiconify()  # Show the main window
        self.login_window.destroy()  # Close the login window