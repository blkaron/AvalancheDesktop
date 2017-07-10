# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1024, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 161, 531))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.open_file_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_file_btn.setEnabled(True)
        self.open_file_btn.setMinimumSize(QtCore.QSize(0, 44))
        self.open_file_btn.setDefault(False)
        self.open_file_btn.setObjectName("open_file_btn")
        self.verticalLayout.addWidget(self.open_file_btn)
        self.open_serial_com_btn = QtWidgets.QPushButton(self.verticalLayoutWidget)
        self.open_serial_com_btn.setMinimumSize(QtCore.QSize(0, 44))
        self.open_serial_com_btn.setObjectName("open_serial_com_btn")
        self.verticalLayout.addWidget(self.open_serial_com_btn)
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 10, 841, 531))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.frame)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 821, 511))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.plotWidget = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.plotWidget.setContentsMargins(0, 0, 0, 0)
        self.plotWidget.setObjectName("plotWidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 19))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.open_file_btn.setToolTip(_translate("MainWindow", "Open file for visualization"))
        self.open_file_btn.setText(_translate("MainWindow", "Open File"))
        self.open_serial_com_btn.setToolTip(_translate("MainWindow", "Open serial connection for real time visualization"))
        self.open_serial_com_btn.setText(_translate("MainWindow", "Open Serial Connection"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

