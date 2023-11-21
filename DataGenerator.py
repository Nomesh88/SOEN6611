import random
from tkinter import messagebox

# DataGenerator class to generate random numbers
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