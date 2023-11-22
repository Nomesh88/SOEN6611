from radon.raw import analyze
from prettytable import PrettyTable

# Function to calculate physical SLOC and logical SLOC for a class
def calculate_sloc(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()

    # Calculate physical SLOC
    physical_sloc = analyze(source_code).loc

    # Calculate logical SLOC using the cc_visit function
    logical_sloc = analyze(source_code).lloc

    return physical_sloc, logical_sloc

# Class file paths
class_files = [
    'DataGenerator.py',
    'LoginWindow.py',
    'Metricstics.py',
    'MetricsticsFrame.py',
    'App.py','main.py'
]

# Initialize a PrettyTable to display the results
table = PrettyTable()
table.field_names = ["Class", "Physical SLOC", "Logical SLOC"]

# Calculate and display results for each class
total_physical_sloc = 0
total_logical_sloc = 0

for class_file in class_files:
    physical_sloc, logical_sloc = calculate_sloc(class_file)
    total_physical_sloc += physical_sloc
    total_logical_sloc += logical_sloc

    table.add_row([class_file, physical_sloc, logical_sloc])

# Add a separator line
table.add_row(["-" * 15, "-" * 15, "-" * 15])
# Add a row for totals
table.add_row(["Total", total_physical_sloc, total_logical_sloc])

# Print the table
print(table)
