import radon
from radon.complexity import cc_visit, sorted_results
import LoginWindow,Metricstics,MetricsticsFrame,App
import inspect

# Function to calculate WMC for a class
def calculate_wmc(class_instance):
    # Get class name
    class_name = class_instance.__name__

    # Get the code of the class
    class_code = inspect.getsource(class_instance)

    # Analyze the code and get the results
    results = cc_visit(class_code)
    complexities = [result.complexity for result in results]

    # Calculate WMC
    wmc = sum(complexities)

    return wmc

# Example usage:
my_class_instance = App
wmc_value = calculate_wmc(my_class_instance)
print("Weighted Method Per Class (WMC) for MyClass:", wmc_value)
