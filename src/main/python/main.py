import sys

from fbs_runtime.application_context.PyQt5 import ApplicationContext
from PyQt5.QtWidgets import QMainWindow, QTreeWidgetItem
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt as CQt

from klumpenplot.gui.KlumpenplotUI import Ui_MainWindow
from klumpenplot.gui.NewDataSourceDialog import NewDataSourceDialog

# Local Core Inputs
from klumpenplot.core.project import Project

class KlumpenplotMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(KlumpenplotMainWindow, self).__init__(parent)
        self.setupUi(self)

        # Core Items #
        self.project = Project()

        # == Dialogs == #
        self.newDataSourceDialog = NewDataSourceDialog(self)

        # == Actions and Triggers == #
        # Menu and Toolbar Actions
        self.actionNewDataSource.triggered.connect(self.newDataSourceDialog.show)

        # Dialog Actions
        self.newDataSourceDialog.accepted.connect(self.newDataSourceDialogAccepted)

    def newDataSourceDialogAccepted(self):
        # First, we get the type
        sourceType = self.newDataSourceDialog.cbDataSourceType.currentText()
        print(sourceType)
        name = self.newDataSourceDialog.txtNewDataSourceName.text()
        number = self.project.dataSourceIndex
        self.project.newDataSource(number, name)
        self.updateProjectLibrary()
    
    def updateProjectLibrary(self):
        self.twProject.clear()
        for dataSourceKey, dataSource in self.project.dataSources.items():
            dataSourceItem = QTreeWidgetItem(self.twProject)
            if dataSource == self.project.currentDataSource:
                dataSourceItem.setFont(0, QFont("Raleway", 10, QFont.Bold))
            dataSourceItem.setText(0, f"({dataSourceKey}) {dataSource.name}") 
            dataSourceItem.setData(0, CQt.UserRole, dataSourceKey)

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