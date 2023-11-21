import tkinter as tk
from tkinter import ttk, messagebox

# LoginWindow class
class LoginWindow(tk.Toplevel):
    def __init__(self, parent, app_instance):
        super().__init__(parent)
        self.title("Login")
        self.geometry("300x150")

        self.app = app_instance

        self.username_label = ttk.Label(self, text="Username:")
        self.username_label.grid(row=0, column=0, padx=10, pady=10)

        self.username_entry = ttk.Entry(self)
        self.username_entry.grid(row=0, column=1, padx=10, pady=10)

        self.password_label = ttk.Label(self, text="Password:")
        self.password_label.grid(row=1, column=0, padx=10, pady=10)

        self.password_entry = ttk.Entry(self, show="*")
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)

        self.login_button = ttk.Button(self, text="Login", command=self.login)
        self.login_button.grid(row=2, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Hardcoded credentials
        credentials = {"admin": "admin", "teacher": "teacher", "student": "student"}

        if username in credentials and credentials[username] == password:
            self.destroy()  # Close the login window
            self.app.show_main_window()  # Show the main application window
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")