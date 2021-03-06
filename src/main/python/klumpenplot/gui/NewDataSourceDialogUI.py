# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dev\ui\NewDataSourceDialog.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_NewDataSourceDialog(object):
    def setupUi(self, NewDataSourceDialog):
        NewDataSourceDialog.setObjectName("NewDataSourceDialog")
        NewDataSourceDialog.resize(400, 283)
        self.verticalLayout = QtWidgets.QVBoxLayout(NewDataSourceDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.cbDataSourceType = QtWidgets.QComboBox(NewDataSourceDialog)
        self.cbDataSourceType.setObjectName("cbDataSourceType")
        self.cbDataSourceType.addItem("")
        self.cbDataSourceType.addItem("")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.cbDataSourceType)
        self.label = QtWidgets.QLabel(NewDataSourceDialog)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_3 = QtWidgets.QLabel(NewDataSourceDialog)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txtNewDataSourceName = QtWidgets.QLineEdit(NewDataSourceDialog)
        self.txtNewDataSourceName.setObjectName("txtNewDataSourceName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtNewDataSourceName)
        self.verticalLayout.addLayout(self.formLayout)
        self.stackedWidget = QtWidgets.QStackedWidget(NewDataSourceDialog)
        self.stackedWidget.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.stackedWidget.setFrameShadow(QtWidgets.QFrame.Plain)
        self.stackedWidget.setObjectName("stackedWidget")
        self.CSVInput = QtWidgets.QWidget()
        self.CSVInput.setObjectName("CSVInput")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.CSVInput)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(self.CSVInput)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox_2)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.txtFilePath = QtWidgets.QLineEdit(self.groupBox_2)
        self.txtFilePath.setObjectName("txtFilePath")
        self.gridLayout_2.addWidget(self.txtFilePath, 0, 1, 1, 1)
        self.btnSelectFile = QtWidgets.QPushButton(self.groupBox_2)
        self.btnSelectFile.setObjectName("btnSelectFile")
        self.gridLayout_2.addWidget(self.btnSelectFile, 0, 2, 1, 1)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.stackedWidget.addWidget(self.CSVInput)
        self.SQLiteInput = QtWidgets.QWidget()
        self.SQLiteInput.setObjectName("SQLiteInput")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.SQLiteInput)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.SQLiteInput)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout_2.addWidget(self.groupBox)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.stackedWidget.addWidget(self.SQLiteInput)
        self.verticalLayout.addWidget(self.stackedWidget)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btnOpen = QtWidgets.QPushButton(NewDataSourceDialog)
        self.btnOpen.setEnabled(False)
        self.btnOpen.setObjectName("btnOpen")
        self.horizontalLayout.addWidget(self.btnOpen)
        self.btnCancel = QtWidgets.QPushButton(NewDataSourceDialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(NewDataSourceDialog)
        self.stackedWidget.setCurrentIndex(0)
        self.btnOpen.clicked.connect(NewDataSourceDialog.accept)
        self.btnCancel.clicked.connect(NewDataSourceDialog.reject)
        self.cbDataSourceType.currentIndexChanged['int'].connect(self.stackedWidget.setCurrentIndex)
        QtCore.QMetaObject.connectSlotsByName(NewDataSourceDialog)

    def retranslateUi(self, NewDataSourceDialog):
        _translate = QtCore.QCoreApplication.translate
        NewDataSourceDialog.setWindowTitle(_translate("NewDataSourceDialog", "New Data Source"))
        self.cbDataSourceType.setItemText(0, _translate("NewDataSourceDialog", "CSV File"))
        self.cbDataSourceType.setItemText(1, _translate("NewDataSourceDialog", "SQLite File"))
        self.label.setText(_translate("NewDataSourceDialog", "Input Type"))
        self.label_3.setText(_translate("NewDataSourceDialog", "Name"))
        self.groupBox_2.setTitle(_translate("NewDataSourceDialog", "CSV File Input"))
        self.label_2.setText(_translate("NewDataSourceDialog", "File Path"))
        self.btnSelectFile.setText(_translate("NewDataSourceDialog", "Select"))
        self.groupBox.setTitle(_translate("NewDataSourceDialog", "SQLite Input"))
        self.btnOpen.setText(_translate("NewDataSourceDialog", "Open"))
        self.btnCancel.setText(_translate("NewDataSourceDialog", "Cancel"))

