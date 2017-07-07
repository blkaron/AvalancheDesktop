import os
import sys

from resources import pyqtgraph as pg
from resources.pyqtgraph.Qt import QtWidgets, QtCore, QtGui
from resources.ui.mainWindow import Ui_MainWindow
import numpy as np


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.setupUi(self)
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

    def open(self):
        if self.maybeSave():
            fileName, _ = QtWidgets.QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)

    def save():
        pass

    def saveAs():
        pass

    def createActions(self):
        self.exitAct = QtWidgets.QAction("&Exit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application", triggered=self.close)
        self.newAct = QtWidgets.QAction("&New", self, shortcut=QtGui.QKeySequence.New,
                               statusTip="Create a new file", triggered=self.newFile)
        self.openAct = QtWidgets.QAction("&Open...", self, shortcut=QtGui.QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.open)
        self.saveAct = QtWidgets.QAction("&Save", self, shortcut=QtGui.QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.save)
        self.saveAsAct = QtWidgets.QAction("Save &As...", self, shortcut=QtGui.QKeySequence.SaveAs,
                               statusTip="Save the document under a new name", triggered=self.saveAs)
        self.aboutQtAct = QtWidgets.QAction("About &Qt", self, statusTip="Show the Qt library's About box",
                               triggered=QtGui.QApplication.instance().aboutQt)

    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QtWidgets.QMessageBox.warning(self, "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    QtWidgets.QMessageBox.Save | QtWidgets.QMessageBox.Discard | QtWidgets.QMessageBox.Cancel)

            if ret == QtWidgets.QMessageBox.Save:
                return self.save()

            if ret == QtWidgets.QMessageBox.Cancel:
                return False

        return True


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    avalancheDesktop = MainWindow()
    avalancheDesktop.show()

    #cw = QtGui.QWidget()
    #avalancheDesktop.setCentralWidget(cw)
    #cw2 = QtGui.QWidget()
    #l = QtGui.QHBoxLayout()
    #cw.setLayout(l)

    #pw = pg.PlotWidget(name='Plot1')  ## giving the plots names allows us to link their axes together
    #l.addWidget(pw)
    sys.exit(app.exec_())
