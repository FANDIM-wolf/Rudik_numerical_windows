from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QTextEdit , QMainWindow 
from pyqt_custom_titlebar_setter import CustomTitlebarSetter
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout , QPushButton , QSizeGrip  ,  QTableWidgetItem 
from Main_window import Ui_MainWindow
from PyQt5 import  QtWidgets
from Linear_equation  import  Ui_Linear_equation_Window
from Rudik_numerical import linear_equations , gauss , zeidel
from SLAE_window import Ui_SLAE_Dialog
from PyQt5.QtGui import *
from PyQt5 import QtGui 
from PyQt5.QtCore import  Qt

import numpy as np
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
    def open_linear_equations_window(self):
        self.linear_window = Linear_Equation_Window()
        self.linear_window= CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.linear_window, title='Linear equation',icon_filename='dark-notepad.svg')
        self.linear_window.show()
    def open_SLAE(self):
        self.SLAE_Window = SLAE_Window()
        self.SLAE_Window= CustomTitlebarSetter.getCustomTitleBarWindow(main_window=self.SLAE_Window , title='SLAE Window',icon_filename='dark-notepad.svg')
        self.SLAE_Window.show()
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    main_window_widget = MainWindow()
    widget = CustomTitlebarSetter.getCustomTitleBarWindow(main_window=main_window_widget,title='Rudik Numericals Windows', icon_filename='dark-notepad.svg')
    widget.show()
    sys.exit(app.exec_())