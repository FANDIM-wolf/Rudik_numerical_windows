import numpy as np
from scipy.integrate import quad, cumtrapz
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QVBoxLayout, QApplication, QWidget
import sys

class UI_Integral_Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle("Integral Visualization")
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.print_plot(0, np.pi, lambda x: np.tan(x), 'tan(x)', 100)

    def print_plot(self, lower_limit, upper_limit, f_str, function, iteration):
        # Calculate the antiderivative using cumulative trapezoidal integration
        x_vals = np.linspace(lower_limit, upper_limit, iteration)
        y_vals = [f_str(x) for x in x_vals]
        F_vals = cumtrapz(y_vals, x_vals, initial=0)

        # Plot the function and its antiderivative
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='Function')
        ax.plot(x_vals, F_vals, label='Antiderivative')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Function and its Antiderivative')
        ax.legend()

        # Create a layout and add the canvas to it
        canvas = FigureCanvas(fig)
        self.layout.addWidget(canvas)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UI_Integral_Window()
    window.show()
    sys.exit(app.exec_())