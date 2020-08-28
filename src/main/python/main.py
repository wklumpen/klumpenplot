from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QFont

from klumpenplot.gui.KlumpenplotUI import Ui_MainWindow
import sys

class KlumpenplotMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KlumpenplotMainWindow, self).__init__(parent)
        self.setupUi(self)

if __name__ == '__main__':
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext

    # Load font
    raleway = QFont("Raleway", 10)

    # Load main window
    window = KlumpenplotMainWindow()
    window.setFont(raleway)

    window.showMaximized()

    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)