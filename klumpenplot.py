import sys
import time

import PyQt5.QtWidgets as W
import PyQt5.QtGui as G
import PyQt5.QtSql as S
import PyQt5.QtCore as C
import PyQt5.Qt as Q

from gui.MCRouteUI import Ui_MainWindow

class MCRouteMainWindow(W.QMainWindow, Ui_MainWindow):
    def __init__(self, app, parent=None):
        super(MCRouteMainWindow, self).__init__(parent)
        self.app = app
        self.setupUi(self)
        self.statusbar.showMessage("Welcome to MCRoute")

if __name__ == "__main__":
    app = W.QApplication(sys.argv)
    mw = MCRouteMainWindow(app)
    raleway = G.QFont("Raleway", 10)
    app.setFont(raleway)

    # Create and display the splash screen
    splash_pix = G.QPixmap('resources/images/mcroute-splash.png')
    splash = W.QSplashScreen(splash_pix, C.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    # splash.show()
    app.processEvents()

    icon = G.QIcon()
    icon.addPixmap(G.QPixmap("resources/images/favicon.ico"), G.QIcon.Normal, G.QIcon.Off)
    mw.setWindowIcon(icon)
    mw.showMaximized()
    splash.finish(mw)
    sys.exit(app.exec_())