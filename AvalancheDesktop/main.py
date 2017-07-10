import os
import sys

from resources import pyqtgraph as pg
from PyQt5.QtGui import (QApplication, QKeySequence)
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QDesktopWidget,
                             QFileDialog, QMessageBox, QAction)
from PyQt5.QtCore import (QFile, QTextStream, Qt, QFileInfo)

from resources.ui.mainWindow import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        # init UI
        self.setupUi(self)
        self.initUI()

        # init functionality
        self.currentFile = ''
        self.textEdit = QTextEdit()

        # connect buttons
        self.open_file_btn.clicked.connect(self.open)

    def initUI(self):

        self.center()
        self.createActions()
        self.createMenus()
        self.setWindowTitle('Avalanche Desktop')
        self.setFixedSize(self.size())

    def center(self):
        screen = QDesktopWidget().screenGeometry()
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
            fileName, _ = QFileDialog.getOpenFileName(self)
            if fileName:
                self.loadFile(fileName)

    def maybeSave(self):
        if self.textEdit.document().isModified():
            ret = QMessageBox.warning(self, "Application",
                    "The document has been modified.\nDo you want to save "
                    "your changes?",
                    QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)

            if ret == QMessageBox.Save:
                return self.save()

            if ret == QMessageBox.Cancel:
                return False

        return True

    def loadFile(self, fileName):
        file = QFile(fileName)
        if not file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (fileName, file.errorString()))
            return

        inf = QTextStream(file)
        QApplication.setOverrideCursor(Qt.WaitCursor)
        self.textEdit.setPlainText(inf.readAll())
        QApplication.restoreOverrideCursor()

        self.setCurrentFile(fileName)
        self.statusBar().showMessage("File loaded", 2000)

    def setCurrentFile(self, fileName):
        self.curFile = fileName
        self.textEdit.document().setModified(False)
        self.setWindowModified(False)

        if self.curFile:
            shownName = self.strippedName(self.curFile)
        else:
            shownName = 'untitled.txt'

        self.setWindowTitle("%s[*] - Application" % shownName)

    def strippedName(self, fullFileName):
        return QFileInfo(fullFileName).fileName()

    def save():
        pass

    def saveAs():
        pass

    def createActions(self):
        self.exitAct = QAction("&Exit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application", triggered=self.close)
        self.newAct = QAction("&New", self, shortcut=QKeySequence.New,
                               statusTip="Create a new file", triggered=self.newFile)
        self.openAct = QAction("&Open...", self, shortcut=QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.open)
        self.saveAct = QAction("&Save", self, shortcut=QKeySequence.Save,
                               statusTip="Save the document to disk", triggered=self.save)
        self.saveAsAct = QAction("Save &As...", self, shortcut=QKeySequence.SaveAs,
                               statusTip="Save the document under a new name", triggered=self.saveAs)
        self.aboutQtAct = QAction("About &Qt", self, statusTip="Show the Qt library's About box",
                               triggered=QApplication.instance().aboutQt)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    avalancheDesktop = MainWindow()
    avalancheDesktop.show()

    pw = pg.PlotWidget(name='SerialPortPlot')
    pw.setLabel('left', 'Value', units='V')
    pw.setLabel('bottom', 'Time', units='s')
    avalancheDesktop.plotWidget.addWidget(pw)
    sys.exit(app.exec_())
