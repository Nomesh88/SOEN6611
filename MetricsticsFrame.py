import tkinter as tk
import re
from tkinter import ttk, scrolledtext, messagebox, filedialog
from DataGenerator import DataGenerator

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

        self.upload_button = ttk.Button(left_frame, text='Choose file')
        self.upload_button['command'] = self.choose_file
        self.upload_button.grid(column=3, row=0, **options)

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

        # Set up button event handlers
        self.mode_button['command'] = self.calculate_mode
        self.mean_button['command'] = self.calculate_mean
        self.median_button['command'] = self.calculate_median
        self.min_button['command'] = self.calculate_min
        self.max_button['command'] = self.calculate_max
        self.mad_button['command'] = self.calculate_mad
        self.std_dev_button['command'] = self.calculate_standard_deviation
        self.reset_button['command'] = self.reset_program

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

    # Choose an external file to upload dataset
    def choose_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            content = self.read_and_display_file(file_path)
            # Check if the content contains only numeric values
            if not re.match(r'^\d+(,\s*\d+)*$', content):
                messagebox.showerror("Error", "The data file contains non-numeric entries")
                return

            data_list = [int(num.strip()) for num in content.split(',')]
            if not data_list:
                messagebox.showerror("Error", "The data file is empty or contains invalid entries")

            DataGenerator.generated_data = data_list
            self.update_data_text(content)
        else:
            messagebox.showerror(title='Error', message="No file detected!")

    # read the content of selected file
    @staticmethod
    def read_and_display_file(file_path):
        try:
            with open(file_path, 'r') as file:
                content = file.read()
                return content
        except FileNotFoundError as error:
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