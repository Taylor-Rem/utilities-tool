import sys
from front_end import main
from tools.browser import Browser
from PyQt5.QtWidgets import QApplication

# Main execution
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = main.HelloWorldApp()
    window.show()
    browser = Browser()
    sys.exit(app.exec_())
