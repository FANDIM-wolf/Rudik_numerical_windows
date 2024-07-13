from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit , QMainWindow 
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout , QPushButton , QSizeGrip  ,  QTableWidgetItem 
from Main_window import Ui_MainWindow
from PyQt5 import  QtWidgets
from Linear_equation  import  Ui_Linear_equation_Window
from Rudik_numerical import linear_equations , gauss , zeidel , differential_equation , integrals ,support_tools
from SLAE_window import Ui_SLAE_Dialog
from integrals_window import Ui_Integrals
from PyQt5.QtGui import *
from PyQt5 import QtGui 
from PyQt5.QtCore import  Qt
from differentional import Ui_Differential
import numpy as np

import sympy as sp,sympy
# Display the plot in the widget
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib.pyplot as plt
class UI_Integral_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Integrals()
        
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.calculate_integral)
    def calculate_integral(self):
        
    
        function = self.ui.lineEdit.text()
        lower_limit = float(self.ui.lineEdit_2.text())
        upper_limit = float(self.ui.lineEdit_3.text())
        the_number_of_partions = int(self.ui.lineEdit_4.text())
        try:
            if self.ui.radioButton.isChecked():
                f_str = support_tools.create_function_from_expr(function)
                a = lower_limit
                b = upper_limit
                n = the_number_of_partions

                result = integrals.integral_rectangle(f_str, a, b, n)
                print(f"Approximate value of the integral 1: {result:.6f}")
                self.print_plot( lower_limit,upper_limit ,f_str ,function)
                self.ui.label_5.setText(str(result)) # print result
                
            elif self.ui.radioButton_2.isChecked():
                f_str = support_tools.create_function_from_expr(function)
                a = lower_limit
                b = upper_limit
                n = the_number_of_partions

                result = integrals.integral_trapezoids(f_str, a, b, n)
                
                print(f"Approximate value of the integral 1: {result:.6f}")
                self.ui.label_5.setText(str(result)) # print result
            elif self.ui.radioButton_3.isChecked():
                f_str = support_tools.create_function_from_expr(function)
                a = lower_limit
                b = upper_limit
                n = the_number_of_partions

                result = integrals.integral_simpson(f_str, a, b, n)
                self.ui.label_5.setText(str(result)) # print result
                print(f"Approximate value of the integral 1: {result:.6f}")
                self.print_plot( lower_limit,upper_limit ,f_str,function)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Please select a method.")
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))

    def print_plot(self , lower_limit,upper_limit ,f_str ,function):
        # Calculate the antiderivative
        x = sp.Symbol('x')
        f = sp.sympify(function)
        F = sp.integrate(f, x)
        print(f"The antiderivative is: {F}")

        # Plot the function and its antiderivative
        x_vals = np.linspace(lower_limit, upper_limit, 100)
        y_vals = [f_str(x) for x in x_vals]
        F_vals = [F.subs(x, x_val) for x_val in x_vals]

        # Create a figure and a canvas
        fig, ax = plt.subplots()
        ax.plot(x_vals, y_vals, label='Function')
        ax.plot(x_vals, F_vals, label='Antiderivative')
        ax.set_xlabel('x')
        ax.set_ylabel('y')
        ax.set_title('Function and its Antiderivative')
        ax.legend()

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        self.ui.widget.setLayout(layout)
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)
class Differential_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Differential()
        
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate_solution)
        
    def calculate_solution(self):
        """
        Calculates the solution of the differential equation and displays the results.
        """
        f_str = self.ui.lineEdit.text()
        f_func = differential_equation.create_function_from_string(f_str)

        x0 = int(self.ui.lineEdit_2.text())
        y0 = int(self.ui.lineEdit_3.text())
        x_end = int(self.ui.lineEdit_4.text())
        n = int(self.ui.lineEdit_5.text())
        

        x_values, y_values = differential_equation.euler_method(f_func, x0, y0, x_end, n)

        # Display the results in the table view
        model = QtGui.QStandardItemModel(len(x_values), 2)
        model.setHorizontalHeaderLabels(["t", "y"])
        for i, (t, y) in enumerate(zip(x_values, y_values)):
            model.setItem(i, 0, QtGui.QStandardItem(str(t)))
            model.setItem(i, 1, QtGui.QStandardItem(str(y)))
        self.ui.tableView.setModel(model)

       

        # Create a layout and add the canvas to it
        layout = QVBoxLayout()
        self.ui.widget.setLayout(layout)

        figure = plt.figure(figsize=(12, 6))
        canvas = FigureCanvas(figure)
        layout.addWidget(canvas)

        plt.plot(x_values, y_values)
        plt.xlabel("t")
        plt.ylabel("y")
        plt.title("Solution of the Differential Equation")
        canvas.draw()


class SLAE_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set the imported Ui_MainWindow as the UI
        self.ui = Ui_SLAE_Dialog()
        
        self.ui.setupUi(self)

        
   
          # Set the imported Ui_MainWindow as the UI

        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.remove_row)
        self.ui.pushButton_3.clicked.connect(self.add_column)
        self.ui.pushButton_4.clicked.connect(self.remove_column)
        self.ui.pushButton_5.clicked.connect(self.calculate_solution)
        self.ui.pushButton_6.clicked.connect(self.clear_tables)
    def add_row(self):
        """
        Adds a new row to the first table view.
        """
        model = self.ui.tableView.model()
        if model is None:
            model = QtGui.QStandardItemModel(0, 3, self)
            self.ui.tableView.setModel(model)
        row_count = model.rowCount()
        model.insertRow(row_count)

    def remove_row(self):
        model = self.ui.tableView.model()
        if model.rowCount() > 0:
            model.removeRow(model.rowCount() - 1)

    def add_column(self):
        """
        Adds a new column to the second table view.
        """
        model = self.ui.tableView.model()
        if model is None:
            model = QtGui.QStandardItemModel(3, 0, self)
            self.ui.tableView.setModel(model)
        column_count = model.columnCount()
        model.insertColumn(column_count)

    def remove_column(self):
        model = self.ui.tableView.model()
        if model.columnCount() > 0:
            model.removeColumn(model.columnCount() - 1)
    def calculate_solution(self):
        model = self.ui.tableView.model()
        A = np.zeros((model.rowCount(), model.columnCount() - 1), dtype=float)
        for i in range(model.rowCount()):
            for j in range(model.columnCount() - 1):
                item = model.item(i, j)
                if item is not None:
                    A[i][j] = float(item.text())

        b = np.zeros(model.rowCount(), dtype=float)
        for i in range(model.rowCount()):
            item = model.item(i, model.columnCount() - 1)
            if item is not None:
                b[i] = float(item.text())

        try:
            if self.ui.radioButton.isChecked():
                max_iterations = int(self.ui.lineEdit.text())
                x, n, xe = gauss.solve_system_gauss(A, b)
                self.display_solution(x)
            elif self.ui.radioButton_2.isChecked():
                max_iterations = int(self.ui.lineEdit.text())
                error = float(self.ui.lineEdit_2.text())
                x0 = np.zeros(model.rowCount())
                x = zeidel.gauss_seidel(A, b, x0, error, max_iterations)
                self.display_solution(x)
            else:
                QtWidgets.QMessageBox.warning(self, "Error", "Please select a method.")
        except ValueError as e:
            QtWidgets.QMessageBox.warning(self, "Error", str(e))
    def display_solution(self, x):
        model = QtGui.QStandardItemModel(len(x), 1)
        for i, value in enumerate(x):
            item = QtGui.QStandardItem(str(value))
            model.setItem(i, 0, item)
        self.ui.tableView_2.setModel(model)
    def clear_tables(self):
        """
        Clears both table views and the variables A, b, and x.
        """
        model1 = self.ui.tableView.model()
        model2 = self.ui.tableView_2.model()

        if model1 is not None:
            model1.clear()
            model1.setRowCount(0)
            model1.setColumnCount(0)

        if model2 is not None:
            model2.clear()
            model2.setRowCount(0)
            model2.setColumnCount(0)

        self.A = None
        self.b = None
        self.x = None
class Linear_Equation_Window(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        # Set the imported Ui_MainWindow as the UI
        self.ui = Ui_Linear_equation_Window()
        
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.calculate_table_values)
        self.ui.pushButton_2.clicked.connect(self.clear_table)
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
    def clear_table(self):
        # Clear the table
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setColumnCount(0)
class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self , parent=None):
        super().__init__()
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.open_linear_equations_window)
        self.pushButton_2.clicked.connect(self.open_SLAE)
        self.pushButton_3.clicked.connect(self.open_Integral_Window)
        self.pushButton_4.clicked.connect(self.open_differential_equations)
    def open_linear_equations_window(self):
        self.linear_window = Linear_Equation_Window()
        self.linear_window= CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.linear_window, title='Linear equation',icon_filename='dark-notepad.svg')
        self.linear_window.show()
    def open_SLAE(self):
        self.SLAE_Window = SLAE_Window()
        self.SLAE_Window= CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.SLAE_Window , title='SLAE Window',icon_filename='dark-notepad.svg')
        self.SLAE_Window.show()
    def open_differential_equations(self):
        self.differential_equation_window =  Differential_Window()
        self.differential_equation_window = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.differential_equation_window , title='Differential equation',icon_filename='dark-notepad.svg')
        self.differential_equation_window.show()
    def open_Integral_Window(self):
        self.integral_window = UI_Integral_Window()
        self.integral_window = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.integral_window , title='Integral Window',icon_filename='dark-notepad.svg')
        self.integral_window.show()

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window_widget = MainWindow()
    widget = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=main_window_widget,title='Rudik Numericals Windows', icon_filename='dark-notepad.svg')
    widget.show()
    sys.exit(app.exec_())