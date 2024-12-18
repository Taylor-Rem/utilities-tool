from PyQt5.QtWidgets import  QWidget, QPushButton, QVBoxLayout

class HelloWorldApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set up the window
        self.setWindowTitle("Hello World App")
        self.setGeometry(100, 100, 300, 200)

        self.create_button('Press Here', self.print_hello_world)

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def create_button(self, title, function):
        self.button = QPushButton(title, self)
        self.button.clicked.connect(function)

    def print_hello_world(self):
        print("Hello World")