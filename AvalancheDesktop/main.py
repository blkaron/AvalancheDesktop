import os
import sys

from resources import pyqtgraph as pg
from resources.pyqtgraph.Qt import QtWidgets, QtCore, QtGui
import numpy as np


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.initUI()

    def initUI(self):

        self.resize(1024, 768)
        self.center()
        self.createActions()
        self.createMenus()
        self.setWindowTitle('Avalanche Desktop')

    def center(self):
        screen = QtWidgets.QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def createMenus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addAction(self.aboutQtAct)
        self.fileMenu.addAction(self.exitAct)

    def newFile():
        pass

    def Open():
        pass

    def Save():
        pass

    def saveAs():
        pass

    def createActions(self):
        self.exitAct = QtWidgets.QAction("E&xit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application", triggered=self.close)
        self.newAct = QtWidgets.QAction("&New", self, shortcut=QtGui.QKeySequence.New,
                               statusTip="Create a new file", triggered=self.newFile)
        self.openAct = QtWidgets.QAction("&Open...", self, shortcut=QtGui.QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.Open)
        self.saveAct = QtWidgets.QAction("&Save", self, shortcut=QtGui.QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.Save)
        self.saveAsAct = QtWidgets.QAction("Save &As...", self, shortcut=QtGui.QKeySequence.SaveAs,
                               statusTip="Save the document under a new name", triggered=self.saveAs)
        self.aboutQtAct = QtWidgets.QAction("About &Qt", self, statusTip="Show the Qt library's About box",
                               triggered=QtGui.QApplication.instance().aboutQt)


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    avalancheDesktop = MainWindow()
    avalancheDesktop.show()
    sys.exit(app.exec_())
