# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'import_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ImportOptionsWindow(object):
    def setupUi(self, ImportOptionsWindow):
        ImportOptionsWindow.setObjectName("ImportOptionsWindow")
        ImportOptionsWindow.resize(1082, 894)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            ImportOptionsWindow.sizePolicy().hasHeightForWidth()
        )
        ImportOptionsWindow.setSizePolicy(sizePolicy)
        ImportOptionsWindow.setMinimumSize(QtCore.QSize(900, 690))
        ImportOptionsWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        ImportOptionsWindow.setBaseSize(QtCore.QSize(900, 600))
        self.centralwidget = QtWidgets.QWidget(ImportOptionsWindow)
        self.centralwidget.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.MinimumExpanding,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth()
        )
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMinimumSize(QtCore.QSize(900, 600))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setBaseSize(QtCore.QSize(900, 600))
        self.centralwidget.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prevDataWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.prevDataWidget.sizePolicy().hasHeightForWidth()
        )
        self.prevDataWidget.setSizePolicy(sizePolicy)
        self.prevDataWidget.setObjectName("prevDataWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.prevDataWidget)
        self.verticalLayout.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.dataPreviewLabel = QtWidgets.QLabel(self.prevDataWidget)
        self.dataPreviewLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dataPreviewLabel.setObjectName("dataPreviewLabel")
        self.verticalLayout.addWidget(self.dataPreviewLabel)
        self.dataView = QtWidgets.QTableView(self.prevDataWidget)
        self.dataView.setObjectName("dataView")
        self.verticalLayout.addWidget(self.dataView)
        self.horizontalLayout.addWidget(self.prevDataWidget)
        self.AssignImportWidget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.AssignImportWidget.sizePolicy().hasHeightForWidth()
        )
        self.AssignImportWidget.setSizePolicy(sizePolicy)
        self.AssignImportWidget.setObjectName("AssignImportWidget")
        self.AssignImportV = QtWidgets.QVBoxLayout(self.AssignImportWidget)
        self.AssignImportV.setContentsMargins(0, 0, -1, -1)
        self.AssignImportV.setObjectName("AssignImportV")
        self.dataAssignLabel = QtWidgets.QLabel(self.AssignImportWidget)
        self.dataAssignLabel.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.dataAssignLabel.setFrameShadow(QtWidgets.QFrame.Plain)
        self.dataAssignLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.dataAssignLabel.setObjectName("dataAssignLabel")
        self.AssignImportV.addWidget(self.dataAssignLabel)
        self.AssignTable = QtWidgets.QTableWidget(self.AssignImportWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AssignTable.sizePolicy().hasHeightForWidth())
        self.AssignTable.setSizePolicy(sizePolicy)
        self.AssignTable.setObjectName("AssignTable")
        self.AssignTable.setColumnCount(0)
        self.AssignTable.setRowCount(0)
        self.AssignTable.horizontalHeader().setSortIndicatorShown(True)
        self.AssignTable.verticalHeader().setVisible(True)
        self.AssignImportV.addWidget(self.AssignTable)
        self.OptionsFrame = QtWidgets.QFrame(self.AssignImportWidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsFrame.sizePolicy().hasHeightForWidth())
        self.OptionsFrame.setSizePolicy(sizePolicy)
        self.OptionsFrame.setBaseSize(QtCore.QSize(0, 0))
        self.OptionsFrame.setFrameShape(QtWidgets.QFrame.Box)
        self.OptionsFrame.setObjectName("OptionsFrame")
        self.OptionsLayout = QtWidgets.QVBoxLayout(self.OptionsFrame)
        self.OptionsLayout.setObjectName("OptionsLayout")
        self.OptionsLabel = QtWidgets.QLabel(self.OptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.OptionsLabel.sizePolicy().hasHeightForWidth())
        self.OptionsLabel.setSizePolicy(sizePolicy)
        self.OptionsLabel.setObjectName("OptionsLabel")
        self.OptionsLayout.addWidget(self.OptionsLabel, 0, QtCore.Qt.AlignHCenter)
        self.ImportGroupBox = QtWidgets.QGroupBox(self.OptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ImportGroupBox.sizePolicy().hasHeightForWidth()
        )
        self.ImportGroupBox.setSizePolicy(sizePolicy)
        self.ImportGroupBox.setFlat(False)
        self.ImportGroupBox.setCheckable(False)
        self.ImportGroupBox.setObjectName("ImportGroupBox")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.ImportGroupBox)
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.PathlineEdit = QtWidgets.QLineEdit(self.ImportGroupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PathlineEdit.sizePolicy().hasHeightForWidth())
        self.PathlineEdit.setSizePolicy(sizePolicy)
        self.PathlineEdit.setMaxLength(32767)
        self.PathlineEdit.setClearButtonEnabled(False)
        self.PathlineEdit.setObjectName("PathlineEdit")
        self.horizontalLayout_3.addWidget(self.PathlineEdit)
        self.PathtoolButton = QtWidgets.QToolButton(self.ImportGroupBox)
        self.PathtoolButton.setObjectName("PathtoolButton")
        self.horizontalLayout_3.addWidget(self.PathtoolButton)
        self.OptionsLayout.addWidget(self.ImportGroupBox)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.formLayout.setContentsMargins(14, -1, 21, 6)
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(30)
        self.formLayout.setObjectName("formLayout")
        self.StartOnLabel = QtWidgets.QLabel(self.OptionsFrame)
        self.StartOnLabel.setObjectName("StartOnLabel")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.StartOnLabel)
        self.StartRowspinBox = QtWidgets.QSpinBox(self.OptionsFrame)
        self.StartRowspinBox.setProperty("value", 0)
        self.StartRowspinBox.setObjectName("StartRowspinBox")
        self.formLayout.setWidget(
            0, QtWidgets.QFormLayout.FieldRole, self.StartRowspinBox
        )
        self.EndOnLabel = QtWidgets.QLabel(self.OptionsFrame)
        self.EndOnLabel.setObjectName("EndOnLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.EndOnLabel)
        self.EndRowspinBox = QtWidgets.QSpinBox(self.OptionsFrame)
        self.EndRowspinBox.setMinimum(-1)
        self.EndRowspinBox.setMaximum(2147483647)
        self.EndRowspinBox.setProperty("value", 100)
        self.EndRowspinBox.setObjectName("EndRowspinBox")
        self.formLayout.setWidget(
            1, QtWidgets.QFormLayout.FieldRole, self.EndRowspinBox
        )
        self.SeparatoLabel = QtWidgets.QLabel(self.OptionsFrame)
        self.SeparatoLabel.setObjectName("SeparatoLabel")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.LabelRole, self.SeparatoLabel
        )
        self.SeparatorcomboBox = QtWidgets.QComboBox(self.OptionsFrame)
        self.SeparatorcomboBox.setEditable(True)
        # self.SeparatorcomboBox.setPlaceholderText("")
        self.SeparatorcomboBox.setObjectName("SeparatorcomboBox")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.SeparatorcomboBox.addItem("")
        self.formLayout.setWidget(
            2, QtWidgets.QFormLayout.FieldRole, self.SeparatorcomboBox
        )
        self.OptionsLayout.addLayout(self.formLayout)
        self.gridWidget = QtWidgets.QWidget(self.OptionsFrame)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gridWidget.sizePolicy().hasHeightForWidth())
        self.gridWidget.setSizePolicy(sizePolicy)
        self.gridWidget.setObjectName("gridWidget")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.gridWidget)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.PreviewButton = QtWidgets.QPushButton(self.gridWidget)
        self.PreviewButton.setObjectName("PreviewButton")
        self.horizontalLayout_4.addWidget(self.PreviewButton)
        self.ConfirmBox = QtWidgets.QDialogButtonBox(self.gridWidget)
        self.ConfirmBox.setOrientation(QtCore.Qt.Horizontal)
        self.ConfirmBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Close | QtWidgets.QDialogButtonBox.Ok
        )
        self.ConfirmBox.setCenterButtons(True)
        self.ConfirmBox.setObjectName("ConfirmBox")
        self.horizontalLayout_4.addWidget(self.ConfirmBox)
        self.OptionsLayout.addWidget(self.gridWidget, 0, QtCore.Qt.AlignHCenter)
        self.AssignImportV.addWidget(self.OptionsFrame)
        self.horizontalLayout.addWidget(self.AssignImportWidget)
        ImportOptionsWindow.setCentralWidget(self.centralwidget)
        self.actionImport = QtWidgets.QAction(ImportOptionsWindow)
        self.actionImport.setObjectName("actionImport")

        self.retranslateUi(ImportOptionsWindow)
        QtCore.QMetaObject.connectSlotsByName(ImportOptionsWindow)

    def retranslateUi(self, ImportOptionsWindow):
        _translate = QtCore.QCoreApplication.translate
        ImportOptionsWindow.setWindowTitle(
            _translate("ImportOptionsWindow", "Import options")
        )
        self.dataPreviewLabel.setText(
            _translate("ImportOptionsWindow", "Preview data table")
        )
        self.dataAssignLabel.setText(
            _translate("ImportOptionsWindow", "Assign data table")
        )
        self.OptionsLabel.setText(_translate("ImportOptionsWindow", "Import options"))
        self.PathlineEdit.setPlaceholderText(
            _translate("ImportOptionsWindow", "file path...")
        )
        self.PathtoolButton.setText(_translate("ImportOptionsWindow", "..."))
        self.StartOnLabel.setText(_translate("ImportOptionsWindow", "Start from line"))
        self.EndOnLabel.setText(_translate("ImportOptionsWindow", "End on line"))
        self.SeparatoLabel.setText(_translate("ImportOptionsWindow", "Separator"))
        self.SeparatorcomboBox.setCurrentText(
            _translate("ImportOptionsWindow", "<space>")
        )
        self.SeparatorcomboBox.setItemText(
            0, _translate("ImportOptionsWindow", "<space>")
        )
        self.SeparatorcomboBox.setItemText(
            1, _translate("ImportOptionsWindow", "<comma>")
        )
        self.SeparatorcomboBox.setItemText(
            2, _translate("ImportOptionsWindow", "<semi-col>")
        )
        self.SeparatorcomboBox.setItemText(
            3, _translate("ImportOptionsWindow", "<tab>")
        )
        self.PreviewButton.setText(_translate("ImportOptionsWindow", "Preview"))
        self.actionImport.setText(_translate("ImportOptionsWindow", "Import"))
