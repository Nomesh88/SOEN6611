import tkinter as tk
import random
import math
from tkinter import ttk, scrolledtext, messagebox

# DataGenerator class is responsible for generating random data.
class DataGenerator:
    generated_data = None

    @staticmethod
    def generate_data(self):
        # Generates random data within the specified range.
        try:
            f = int(self.data_range.get())
            if f >= 1000:
                DataGenerator.generated_data = [random.randint(0, 1000) for _ in range(f)]
                return DataGenerator.generated_data
            else:
                return "Range must be at least 1000. Enter positive numbers."
        except ValueError as error:
            messagebox.showerror("Error", "Please enter a valid number of range")

# Metricstics class handles various statistical calculations without using built-in functions.
class Metricstics:
    def calculate_min(self, data):
        # Calculates the minimum value in the given data.
        if not data:
            return 0
        min_value = data[0]
        for num in data:
            if num < min_value:
                min_value = num
        return min_value

    def calculate_max(self, data):
        # Calculates the maximum value in the given data.
        if not data:
            return 0
        max_value = data[0]
        for num in data:
            if num > max_value:
                max_value = num
        return max_value

    def calculate_mean(self, data):
        # Calculates the mean (average) of the given data.
        if not data:
            return 0
        total = 0
        for num in data:
            total += num
        return total / len(data)

    def calculate_median(self, data):
        # Calculates the median of the given data.
        if not data:
            return 0
        sorted_data = sorted(data)
        mid = len(sorted_data) // 2
        if len(sorted_data) % 2 == 0:
            return (sorted_data[mid] + sorted_data[mid - 1]) / 2
        else:
            return sorted_data[mid]

    def calculate_mode(self, data):
        # Calculates the mode(s) of the given data.
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
        # Calculates the Mean Absolute Deviation (MAD) of the given data.
        if not data:
            return 0
        mean = self.calculate_mean(data)
        total = 0
        for num in data:
            total += self.absolute(num - mean)
        return total / len(data)

    def calculate_standard_deviation(self, data):
        # Calculates the standard deviation of the given data.
        if not data:
            return 0
        mean = self.calculate_mean(data)
        variance = 0
        for num in data:
            variance += (num - mean) ** 2
        return math.sqrt(variance / (len(data) - 1))

    def absolute(self, num):
        # Returns the absolute value of a number.
        if num < 0:
            return -num
        return num

# MetricsticsFrame class represents the main UI for the application.
class MetricsticsFrame(ttk.Frame):
    def __init__(self, container, metrics_calculator):
        super().__init__(container)
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

        self.data_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD, width=30, height=20)
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

        # Reset button
        self.reset_button = ttk.Button(button_frame, text='Reset')
        self.reset_button.grid(column=0, row=8, sticky=tk.W, **options)

        #self.clear_button = ttk.Button(button_frame, text='Clear text')
        #self.clear_button.grid(column=0, row=7, sticky=tk.W, **options)

        # Set up button event handlers
        self.mode_button['command'] = self.calculate_mode
        self.mean_button['command'] = self.calculate_mean
        self.median_button['command'] = self.calculate_median
        self.min_button['command'] = self.calculate_min
        self.max_button['command'] = self.calculate_max
        self.mad_button['command'] = self.calculate_mad
        self.std_dev_button['command'] = self.calculate_standard_deviation
        self.reset_button['command'] = self.reset_program
        #self.clear_button['command'] = self.clear_text

        self.grid(padx=20, pady=20, sticky=tk.NSEW)
        
        
        

    def reset_program(self):
        # Resets the program by clearing data and result text.
        self.clear_text()
        # Clear generated data in DataGenerator
        DataGenerator.generated_data = None

    def clear_text(self):
        # Clears the text in both data and result text boxes.
        self.update_data_text("")
        self.update_result_text("")

    def calculate_mode(self):
        # Calculates and displays the mode of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_mode(data)
                self.update_result_text(f"Mode: {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_mean(self):
        # Calculates and displays the mean of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_mean(data)
                self.update_result_text(f"Mean (μ): {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_median(self):
        # Calculates and displays the median of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_median(data)
                self.update_result_text(f"Median: {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_min(self):
        # Calculates and displays the minimum vale of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_min(data)
                self.update_result_text(f"Min: {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_max(self):
        # Calculates and displays the maximum value of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_max(data)
                self.update_result_text(f"Max: {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_mad(self):
        # Calculates and displays the MAD of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_mad(data)
                self.update_result_text(f"Mean Absolute Deviation (MAD): {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_standard_deviation(self):
        # Calculates and displays the SD of the generated data.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = self.metrics_calculator.calculate_standard_deviation(data)
                self.update_result_text(f"Standard Deviation (σ): {result}")
            else:
                self.update_result_text(data)
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def generate_data(self):
        # Generates random data and updates the data text box.
        data = DataGenerator.generate_data(self)
        if isinstance(data, list):
            self.update_data_text("Generated Data:\n" + ", ".join(map(str, data))
        )
        else:
            self.update_data_text(data)

    def update_data_text(self, text):
        # Updates the data text box with the given text.
        try:
            self.data_text.delete(1.0, tk.END)
            self.data_text.insert(tk.END, text)
        except Exception as error:
            print(error)
    def update_result_text(self, text):
        # Updates the result text box with the given text.
        try:
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, text)
        except Exception as error:
            print(error)

    def calculate_statistic(self, operation, operation_name):
        # Calculates and displays the result of a given statistical operation.
        try:
            data = DataGenerator.generated_data
            if isinstance(data, list):
                result = operation(data)
                self.update_result_text(f"{operation_name}: {result}")
            else:
                self.update_result_text("Generate Data to calculate")
        except ValueError as error:
            messagebox.showerror(title='Error', message=error)

    def calculate_mode(self):
        # Wrapper function for calculating and displaying the mode.
        self.calculate_statistic(self.metrics_calculator.calculate_mode, "Mode")

    def calculate_mean(self):
        # Wrapper function for calculating and displaying the mean.
        self.calculate_statistic(self.metrics_calculator.calculate_mean, "Mean (μ)")

    def calculate_median(self):
        # Wrapper function for calculating and displaying the median.
        self.calculate_statistic(self.metrics_calculator.calculate_median, "Median")

    def calculate_min(self):
        # Wrapper function for calculating and displaying the minimum value.
        self.calculate_statistic(self.metrics_calculator.calculate_min, "Min")

    def calculate_max(self):
        # Wrapper function for calculating and displaying the maximum value.
        self.calculate_statistic(self.metrics_calculator.calculate_max, "Max")

    def calculate_mad(self):
        # Wrapper function for calculating and displaying the MAD.
        self.calculate_statistic(self.metrics_calculator.calculate_mad, "Mean Absolute Deviation (MAD)")

    def calculate_standard_deviation(self):
        # Wrapper function for calculating and displaying the SD.
        self.calculate_statistic(self.metrics_calculator.calculate_standard_deviation, "Standard Deviation (σ)")

# App class represents the main application window.
class App(tk.Tk):
    def __init__(self, metrics_calculator):
        # Initializes the main application window.
        super().__init__()
        self.title('METRICSTICS')
        self.geometry('700x400')  
        self.resizable(False, False)
        self.metrics_calculator = metrics_calculator

if __name__ == "__main__":
    # Initializes the metrics calculator and the main application.
    metrics_calculator = Metricstics()
    app = App(metrics_calculator)
    MetricsticsFrame(app, metrics_calculator)
    app.mainloop()
