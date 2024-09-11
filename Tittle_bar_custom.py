from PyQt6 import QtCore, QtGui, QtWidgets   
from PyQt6.QtCore import Qt , QSize
from PyQt6.QtWidgets import QVBoxLayout , QLabel , QMenuBar , QStatusBar  , QPushButton , QWidget , QHBoxLayout , QSizePolicy
class MyBar(QWidget):
    def __init__(self, ):
        super(MyBar, self).__init__()
        self.layout = QHBoxLayout()
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.title = QLabel("Rudik Numerical")
        

        btn_size = 35

        self.btn_close = QPushButton("x")
        self.btn_close.clicked.connect(self.btn_close_clicked)
        self.btn_close.setFixedSize(btn_size, btn_size)
        self.btn_close.setStyleSheet("background-color: red;")

        self.btn_min = QPushButton("-")
        self.btn_min.clicked.connect(self.btn_min_clicked)
        self.btn_min.setFixedSize(btn_size, btn_size)
        self.btn_min.setStyleSheet("background-color: gray;")

        self.btn_max = QPushButton("+")
        self.btn_max.clicked.connect(self.btn_max_clicked)
        self.btn_max.setFixedSize(btn_size, btn_size)
        self.btn_max.setStyleSheet("background-color: gray;")

        self.title.setFixedHeight(35)
        self.title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.title)
        self.layout.addWidget(self.btn_min)
        self.layout.addWidget(self.btn_max)
        self.layout.addWidget(self.btn_close)

        self.title.setStyleSheet(
            """
            background-color: black;
            color: white;
        """
        )
        self.setLayout(self.layout)


    def resizeEvent(self, QResizeEvent):
        super(MyBar, self).resizeEvent(QResizeEvent)
        self.title.setFixedWidth(self.window().width())

    def mousePressEvent(self, event):
        self.start = self.mapToGlobal(event.pos())
        self.pressing = True

    def mouseMoveEvent(self, event):
        #print(event.pos())
        self.end = self.mapToGlobal(event.pos())
        delta = self.end - self.start
        self.window().setGeometry(
            self.mapToGlobal(delta).x(),
            self.mapToGlobal(delta).y(),
            self.window().width(),
            self.window().height(),
        )
        self.start = self.end

    def mouseReleaseEvent(self, QMouseEvent):
        self.pressing = False

    def btn_close_clicked(self):
        self.window().close()

    def btn_max_clicked(self):
        #toggle between fullscreen and normal size
        if self.window().isFullScreen():
            self.window().showNormal()
        else:
            self.window().showFullScreen()
        #self.window().showMaximized()

    def btn_min_clicked(self):
        self.window().showMinimized()

class TitleBar(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.my_bar = MyBar()
        self.my_bar.setParent(self.main_window)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.my_bar)
        
# Add the TitleBar widget to the main window
#        self.title_bar = TitleBar(MainWindow)
#        MainWindow.setMenuWidget(self.title_bar)