import tkinter as tk
import random
import math
from tkinter import ttk, scrolledtext
from tkinter.messagebox import showerror

# DataGenerator class is responsible for generating random data.
class DataGenerator:
    def generate_data(self, f):
        try:
            if f >= 1000:
                return [random.randint(0, 1000) for _ in range(f)]
            else:
                return "Range must be at least 1000."
        except ValueError:
            return "Invalid input. Please enter a number."

# Metricstics class handles various statistical calculations without using built-in functions.
class Metricstics:
    def calculate_min(self, data):
        if not data:
            return 0
        min_value = data[0]
        for num in data:
            if num < min_value:
                min_value = num
        return min_value

    def calculate_max(self, data):
        if not data:
            return 0
        max_value = data[0]
        for num in data:
            if num > max_value:
                max_value = num
        return max_value

    def calculate_mean(self, data):
        if not data:
            return 0
        total = 0
        for num in data:
            total += num
        return total / len(data)

    def calculate_median(self, data):
        if not data:
            return 0
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid] + sorted_data[mid - 1]) / 2
        else:
            return sorted_data[mid]

    def calculate_mode(self, data):
        if not data:
            return 0
        count_dict = {}
        for num in data:
            if num in count_dict:
                count_dict[num] += 1
            else:
                count_dict[num] = 1

        max_count = max(count_dict.values())
        mode_values = [num for num, count in count_dict.items() if count == max_count]

        if len(mode_values) == 1:
            return mode_values[0]
        else:
            return mode_values

    def calculate_mad(self, data):
        if not data:
            return 0
        mean = self.calculate_mean(data)
        total = 0
        for num in data:
            total += self.absolute(num - mean)
        return total / len(data)

    def calculate_standard_deviation(self, data):
        if not data:
            return 0
        mean = self.calculate_mean(data)
        variance = 0
        for num in data:
            variance += (num - mean) ** 2
        return math.sqrt(variance / (len(data) - 1))

    def absolute(self, num):
        if num < 0:
            return -num
        return num

# MetricsticsFrame class represents the main UI for the application.
class MetricsticsFrame(ttk.Frame):
    def __init__(self, container, data_generator, metrics_calculator):
        super().__init__(container)
        self.data_generator = data_generator
        self.metrics_calculator = metrics_calculator

        # UI setup
        options = {'padx': 5, 'pady': 5}

        # Left frame for data generation
        left_frame = ttk.Frame(self)
        left_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.range_of_data_label = ttk.Label(left_frame, text='Range of data')
        self.range_of_data_label.grid(column=0, row=0, sticky=tk.W, **options)

        self.data_range = tk.StringVar()
        self.data_range_entry = ttk.Entry(left_frame, textvariable=self.data_range)
        self.data_range_entry.grid(column=1, row=0, **options)
        self.data_range_entry.focus()

        self.generate_button = ttk.Button(left_frame, text='Generate Data')
        self.generate_button['command'] = self.generate_data
        self.generate_button.grid(column=2, row=0, **options)

        self.data_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=30, height=10)
        self.data_text.grid(row=1, column=0, columnspan=3, rowspan=3, **options)

        # Right frame for calculations and results
        right_frame = ttk.Frame(self)
        right_frame.grid(row=0, column=1, sticky=tk.NSEW)

        button_frame = ttk.Frame(right_frame)
        button_frame.grid(row=0, column=0, sticky=tk.NSEW)

        self.mode_button = ttk.Button(button_frame, text='Mode')
        self.mode_button.grid(column=0, row=0, sticky=tk.W, **options)

        self.mean_button = ttk.Button(button_frame, text='Mean (μ)')
        self.mean_button.grid(column=0, row=1, sticky=tk.W, **options)

        self.median_button = ttk.Button(button_frame, text='Median')
        self.median_button.grid(column=0, row=2, sticky=tk.W, **options)

        self.min_button = ttk.Button(button_frame, text='Min')
        self.min_button.grid(column=0, row=3, sticky=tk.W, **options)

        self.max_button = ttk.Button(button_frame, text='Max')
        self.max_button.grid(column=0, row=4, sticky=tk.W, **options)

        self.mad_button = ttk.Button(button_frame, text='Mean Absolute Deviation (MAD)')
        self.mad_button.grid(column=0, row=5, sticky=tk.W, **options)

        self.std_dev_button = ttk.Button(button_frame, text='Standard Deviation (σ)')
        self.std_dev_button.grid(column=0, row=6, sticky=tk.W, **options)

        self.result_text = scrolledtext.ScrolledText(right_frame, wrap=tk.WORD, width=30, height=3)  # Smaller text box
        self.result_text.grid(row=1, column=0, columnspan=1, rowspan=3, **options)

        # Set up button event handlers
        self.mode_button['command'] = self.calculate_mode
        self.mean_button['command'] = self.calculate_mean
        self.median_button['command'] = self.calculate_median
        self.min_button['command'] = self.calculate_min
        self.max_button['command'] = self.calculate_max
        self.mad_button['command'] = self.calculate_mad
        self.std_dev_button['command'] = self.calculate_standard_deviation

        self.grid(padx=20, pady=20, sticky=tk.NSEW)

    def calculate_mode(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_mode(data)
            self.update_result_text(f"Mode: {result}")
        else:
            self.update_result_text(data)

    def calculate_mean(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_mean(data)
            self.update_result_text(f"Mean (μ): {result}")
        else:
            self.update_result_text(data)

    def calculate_median(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_median(data)
            self.update_result_text(f"Median: {result}")
        else:
            self.update_result_text(data)
                
    def calculate_median(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_median(data)
            self.update_result_text(f"Median: {result}")
        else:
            self.update_result_text(data)

    def calculate_min(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_min(data)
            self.update_result_text(f"Min: {result}")
        else:
            self.update_result_text(data)

    def calculate_max(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_max(data)
            self.update_result_text(f"Max: {result}")
        else:
            self.update_result_text(data)

    def calculate_mad(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_mad(data)
            self.update_result_text(f"Mean Absolute Deviation (MAD): {result}")
        else:
            self.update_result_text(data)

    def calculate_standard_deviation(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            result = self.metrics_calculator.calculate_standard_deviation(data)
            self.update_result_text(f"Standard Deviation (σ): {result}")
        else:
            self.update_result_text(data)

    def generate_data(self):
        data = self.data_generator.generate_data(int(self.data_range.get()))
        if isinstance(data, list):
            self.update_data_text("Generated Data:\n" + ", ".join(map(str, data))
        )
        else:
            self.update_data_text(data)

    def update_data_text(self, text):
        self.data_text.delete(1.0, tk.END)
        self.data_text.insert(tk.END, text)

    def update_result_text(self, text):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, text)

# App class represents the main application window.
class App(tk.Tk):
    def __init__(self, data_generator, metrics_calculator):
        super().__init__()
        self.title('METRICSTICS')
        self.geometry('700x350')  # Adjusted window width
        self.resizable(False, False)
        self.data_generator = data_generator
        self.metrics_calculator = metrics_calculator

if __name__ == "__main__":
    data_generator = DataGenerator()
    metrics_calculator = Metricstics()
    app = App(data_generator, metrics_calculator)
    MetricsticsFrame(app, data_generator, metrics_calculator)
    app.mainloop()
