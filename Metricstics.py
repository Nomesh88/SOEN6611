import tkinter as tk
import random
from tkinter import ttk
from tkinter.messagebox import showerror

class Metricstics:
    @staticmethod
    def generate_data(f):
        try:
            range_value = f
            if range_value >= 1000:
                return [random.randint(0, 1000) for _ in range(f)]
            else:
                return ("Range must be at least 1000.")
        except ValueError:
            return ("Invalid input. Please enter a number.")
class ConverterFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 5, 'pady': 5}

        # temperature label
        self.range_of_data_label = ttk.Label(self, text='Range of data')
        self.range_of_data_label.grid(column=0, row=0, sticky=tk.W, **options)

        # temperature entry
        self.data_range = tk.StringVar()
        self.data_range_entry = ttk.Entry(self, textvariable=self.data_range)
        self.data_range_entry.grid(column=1, row=0, **options)
        self.data_range_entry.focus()

        self.generate_button = ttk.Button(self, text='Generate Data')
        self.generate_button['command'] = self.generate
        self.generate_button.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.text_widget = tk.Text(self, height=10, width=70)
        self.text_widget.grid(row=2, columnspan=50, **options)

        # button Min
        self.min_button = ttk.Button(self, text='Min')
        self.min_button['command'] = self.min
        self.min_button.grid(column=0, row=3, sticky=tk.SW, **options)

        # button Max
        self.max_button = ttk.Button(self, text='Max')
        self.max_button['command'] = self.max
        self.max_button.grid(column=1, row=3, sticky=tk.SW, **options)

        # Min data label
        self.min_data_label = ttk.Label(self, text='')
        self.min_data_label.grid(column=0, row=4, sticky=tk.W, **options)

        # Max data label
        self.max_data_label = ttk.Label(self, text='')
        self.max_data_label.grid(column=1, row=4, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def min(self):
        try:
            f = int(self.data_range.get())
            c = Metricstics.generate_data(f)
            if c:  # Ensure c is not an empty list
                min_value = min(c)
                new_text = 'Min: ' + str(min_value)
                self.min_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)

    def max(self):
        try:
            f = int(self.data_range.get())
            c = Metricstics.generate_data(f)
            if c:  # Ensure c is not an empty list
                max_value = max(c)
                new_text = 'Max: ' + str(max_value)
                self.max_data_label.config(text=new_text)
        except ValueError as error:
            showerror(title='Error', message=error)

    def generate(self):
        """  Handle button click event
        """
        try:
            f = int(self.data_range.get())
            c = Metricstics.generate_data(f)

            self.text_widget.delete(1.0, tk.END)
            if isinstance(c, list):
                self.text_widget.insert(tk.END, " ".join(map(str, c)))
            else:
                self.text_widget.insert(tk.END, c)

        except ValueError as error:
            showerror(title='Error', message=error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('METRICSTICS')
        self.geometry('700x280')
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    ConverterFrame(app)
    app.mainloop()