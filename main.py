from Metricstics import Metricstics
from MetricsticsFrame import MetricsticsFrame
from App import App

if __name__ == "__main__":
    # Initializes the metrics calculator and the main application.
    metrics_calculator = Metricstics()
    app = App(metrics_calculator)
    app.login_window.wait_window()  # Wait for the login window to be closed
    MetricsticsFrame(app, metrics_calculator)
    app.mainloop()