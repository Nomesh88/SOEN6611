import tkinter as tk
import random
import math
from tkinter import ttk
from tkinter.messagebox import showerror

class Metricstics:
    generated_data = None

    @staticmethod
    def abs(num):
        if num < 0:
            return -num
        return num

    @staticmethod
    def generate_data(f):
        try:
            range_value = f
            if range_value >= 1000:
                Metricstics.generated_data = [random.randint(0, 1000) for _ in range(f)]
                return Metricstics.generated_data
            else:
                return ("Range must be at least 1000.")
        except ValueError:
            return ("Invalid input. Please enter a number.")
class MetricsticsFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        # field options
        options = {'padx': 2, 'pady': 2}

        # range of data label
        self.range_of_data_label = ttk.Label(self, text='Range of data')
        self.range_of_data_label.grid(column=0, row=0, sticky=tk.W, **options)

        # data range
        self.data_range = tk.StringVar()
        self.data_range_entry = ttk.Entry(self, textvariable=self.data_range)
        self.data_range_entry.grid(column=1, row=0, **options)
        self.data_range_entry.focus()

        # button Generate Data
        self.generate_button = ttk.Button(self, text='Generate Data')
        self.generate_button['command'] = self.generate
        self.generate_button.grid(column=2, row=0, sticky=tk.W, **options)

        # result label
        self.text_widget = tk.Text(self, height=15, width=80)
        self.text_widget.grid(row=2, columnspan=50, **options)

        # button Min
        self.min_button = ttk.Button(self, text='Min')
        self.min_button['command'] = self.min
        self.min_button.grid(column=0, row=3, sticky=tk.SW, **options)

        # button Max
        self.max_button = ttk.Button(self, text='Max')
        self.max_button['command'] = self.max
        self.max_button.grid(column=1, row=3, sticky=tk.SW, **options)

        # button Median
        self.median_button = ttk.Button(self, text='Med')
        self.median_button['command'] = self.median
        self.median_button.grid(column=2, row=3, sticky=tk.SW, **options)

        # button μ
        self.median_button = ttk.Button(self, text='μ')
        self.median_button['command'] = self.arithmeticMean
        self.median_button.grid(column=3, row=3, sticky=tk.SW, **options)

        # button MAD
        self.mad_button = ttk.Button(self, text='MAD')
        self.mad_button['command'] = self.meanAbsoluteDeviation
        self.mad_button.grid(column=4, row=3, sticky=tk.SW, **options)

        # button σ
        self.standard_deviation_button = ttk.Button(self, text='σ')
        self.standard_deviation_button['command'] = self.standardDeviation
        self.standard_deviation_button.grid(column=5, row=3, sticky=tk.SW, **options)

        # Min data label
        self.min_data_label = ttk.Label(self, text='')
        self.min_data_label.grid(column=0, row=4, sticky=tk.W, **options)

        # Max data label
        self.max_data_label = ttk.Label(self, text='')
        self.max_data_label.grid(column=1, row=4, sticky=tk.W, **options)

        # Median data label
        self.median_data_label = ttk.Label(self, text='')
        self.median_data_label.grid(column=2, row=4, sticky=tk.W, **options)

        # ArithmeticMean data label
        self.arithmeticMean_data_label = ttk.Label(self, text='')
        self.arithmeticMean_data_label.grid(column=3, row=4, sticky=tk.W, **options)

        # meanAbsoluteDeviation data label
        self.meanAbsoluteDeviation_data_label = ttk.Label(self, text='')
        self.meanAbsoluteDeviation_data_label.grid(column=4, row=4, sticky=tk.W, **options)

        # standardDeviation data label
        self.standardDeviation_data_label = ttk.Label(self, text='')
        self.standardDeviation_data_label.grid(column=5, row=4, sticky=tk.W, **options)

        # add padding to the frame and show it
        self.grid(padx=20, pady=20, sticky=tk.NSEW)

    def standardDeviation(self):
        try:
            data = Metricstics.generated_data
            if data:
                mean = int(self.arithmeticMean())
                variance = 0
                for num in data:
                    variance += (num - mean) ** 2
                result = math.sqrt(variance / (len(data) - 1))
                new_text = 'σ: ' + str(round(result, 3))
                self.standardDeviation_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)
    def meanAbsoluteDeviation(self):
        try:
            data = Metricstics.generated_data
            if data:
                mean = int(self.arithmeticMean())
                total = 0
                for num in data:
                    total += Metricstics.abs(num - mean)
                result = str(total / len(data))
                new_text = 'MAD: ' + str(result)
                self.meanAbsoluteDeviation_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)

    def arithmeticMean(self):
        try:
            data = Metricstics.generated_data
            total = 0
            if data:
                for num in data:
                    total += num
                result = str(total / len(data))
                new_text = 'μ: ' + str(result)
                self.arithmeticMean_data_label.config(text=new_text)

                return total / len(data)

        except ValueError as error:
            showerror(title='Error', message=error)
    def median(self):
        try:
            data = Metricstics.generated_data
            if data:
                mid = len(data)//2
                if len(data) % 2 == 0:
                    result = str((data[mid] + data[mid-1])/2)
                else:
                    result = str(data[mid])
                new_text = 'Median: ' + str(result)
                self.median_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)

    def min(self):
        try:
            data = Metricstics.generated_data
            if data:  # Ensure c is not an empty list
                min_value = float('inf')
                for value in data:
                    if value < min_value:
                        min_value = value
                new_text = 'Min: ' + str(min_value)
                self.min_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)

    def max(self):
        try:
            data = Metricstics.generated_data
            if data:  # Ensure c is not an empty list
                max_value = float('-inf')
                for value in data:
                    if value > max_value:
                        max_value = value
                new_text = 'Max: ' + str(max_value)
                self.max_data_label.config(text=new_text)

        except ValueError as error:
            showerror(title='Error', message=error)

    def generate(self):
        """  Handle button Generate event
        """
        try:
            f = int(self.data_range.get())
            data = Metricstics.generate_data(f)

            self.text_widget.delete(1.0, tk.END)
            if isinstance(data, list):
                self.text_widget.insert(tk.END, ", ".join(map(str, data)))
            else:
                self.text_widget.insert(tk.END, data)

        except ValueError as error:
            showerror(title='Error', message=error)

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('METRICSTICS')
        self.geometry('800x350')
        self.resizable(False, False)

if __name__ == "__main__":
    app = App()
    MetricsticsFrame(app)
    app.mainloop()