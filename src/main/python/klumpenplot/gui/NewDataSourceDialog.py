from klumpenplot.gui.NewDataSourceDialogUI import Ui_NewDataSourceDialog
import PyQt5.QtWidgets as W

class NewDataSourceDialog(W.QDialog, Ui_NewDataSourceDialog):
    def __init__(self, handler, parent=None):
        super(NewDataSourceDialog, self).__init__(parent)
        self.setupUi(self)

        self.txtNewDataSourceName.textChanged.connect(self.textChangeEvent)
        self.txtFilePath.textChanged.connect(self.textChangeEvent)


    def textChangeEvent(self):
        if (len(self.txtNewDataSourceName.text()) > 0) & (len(self.txtFilePath.text()) > 0):
            self.btnOpen.setEnabled(True)
        else:
            self.btnOpen.setEnabled(False)