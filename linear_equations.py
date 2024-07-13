import sys
from Linear_equation  import  Ui_Linear_equation_Window
from Rudik_numerical import linear_equations
from PyQt5.QtCore import QPoint
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QHBoxLayout
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QWidget , QSizeGrip ,  QMainWindow ,  QTableWidgetItem
from PyQt5.QtCore import Qt, QFile, QIODevice
from PyQt5.uic import loadUi
from PyQt5 import  QtWidgets
class Linear_Equation_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set the imported Ui_MainWindow as the UI
        self.ui = Ui_Linear_equation_Window()
        
        self.ui.setupUi(self)

        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)
        self.pressing = False
        self.size_grip = QSizeGrip(self)
        self.size_grip.setGeometry(self.width() - 20, self.height() - 20, 20, 20)
        self.ui.pushButton.clicked.connect(self.calculate_table_values)
    def resizeEvent(self, event):
        self.size_grip.setGeometry(self.width() - 20, self.height() - 20, 20, 20)
    def calculate_table_values(self):
        func_str = self.ui.lineEdit.text()
        expr = linear_equations.string_to_expr(func_str)

        # compute_derivative f(x)
        f_prime = expr.diff()

        #Create function from string
        f_func = linear_equations.create_function_from_expr(expr)

        # Create function from string derivative
        f_prime_func = linear_equations.create_function_from_derivative(f_prime)
        # Compute root using Newton-Raphson method
        x0 = 0.5
        tol = 1e-6
        max_iter = 10
        x_array = linear_equations.newton_method(f_func, f_prime_func, x0, tol, max_iter, return_x_array=True)
        self.ui.tableWidget.setRowCount(1)
        self.ui.tableWidget.setColumnCount(len(x_array))


        
        
        for i, value in enumerate(x_array):
            item = QTableWidgetItem(str(value))
            self.ui.tableWidget.setItem(0, i, item)


if __name__ == "__main__":
    app = QApplication([])
    window = Linear_Equation_Window()
    window.show()
    app.exec()