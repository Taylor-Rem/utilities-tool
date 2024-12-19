from PyQt5.QtWidgets import  QWidget, QPushButton, QVBoxLayout
from jobs.abt_import import AbtImport

class App(QWidget):
    def __init__(self, job_manager):
        super().__init__()
        self.job_manager = job_manager
        self.initUI()
        

    def initUI(self):
        # Set up the window
        self.setWindowTitle("Hello World App")
        self.setGeometry(100, 100, 300, 200)

        self.create_button('ABT Import', lambda: self.job_manager.run_jobs('abt_import'))

        # Set up layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)

    def create_button(self, title, function):
        self.button = QPushButton(title, self)
        self.button.clicked.connect(function)

    def closeEvent(self, event):
        self.job_manager.browser.close()
        super().closeEvent(event)
