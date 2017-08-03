import os
import sys
import serial
import serial.tools.list_ports

from datetime import datetime
from resources import pyqtgraph as pg
from resources.ui.mainWindow import Ui_MainWindow

from stm32serial import SerialThread

from PyQt5.QtGui import (QApplication, QKeySequence)
from PyQt5.QtWidgets import (QMainWindow, QTextEdit, QDesktopWidget,
                             QFileDialog, QMessageBox, QAction, QLabel)
from PyQt5.QtCore import (QFile, QTextStream, Qt, QFileInfo, QIODevice)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()

        self.baudrate = 9600
        self.used_port = None

        # init UI
        self.setupUi(self)
        self.initUI()
        self.serialThread = SerialThread(self.baudrate)

        # init program data
        self.current_file = ''
        self.read_file_data = []

        # connect buttons
        self.open_file_btn.clicked.connect(self.open)
        self.open_serial_com_btn.toggled.connect(self.toggle_serial)
        self.serialThread.readLineSignal.connect(self.display_data)

    def initUI(self):

        self.center()
        self.create_actions()
        self.create_menus()
        self.setWindowTitle('Avalanche Desktop')
        self.setFixedSize(self.size())
        self.statusInfoWidget = QLabel()
        self.statusBar().addWidget(self.statusInfoWidget)

    def center(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/2, (screen.height()-size.height())/2)

    def create_menus(self):
        self.fileMenu = self.menuBar().addMenu("&File")
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAsAct)
        self.fileMenu.addAction(self.exitAct)

    def toggle_serial(self):
        """
        Start/Stop serial communication and restore button state

        """
        if self.open_serial_com_btn.isChecked():
            self.get_stm32_port_name()
            self.open_serial()
        elif self.used_port is not None and not self.open_serial_com_btn.isChecked():
            self.close_serial()
        else:
            self.open_serial_com_btn.setStyleSheet("")
            self.open_serial_com_btn.setChecked(False)
            self.statusInfoWidget.setText("STM32 not found at any port, check connection")

    def get_stm32_port_name(self):
        """
        Get the serial port name which SMT32 is linked to

        """
        key_word = {'ubuntu': 'STM32', 'win': 'STMicroelectronics'}
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            tmp_val = p.__dict__.get('description', None)
            if tmp_val is not None and key_word['ubuntu'] in tmp_val.split() or key_word['windows'] in tmp_val.split():
                self.used_port = p.__dict__.get('device', None)
                self.statusInfoWidget.setText("Opening serial port {} ".format(p))
                break

    def open_serial(self):
        """
        Open serial port and start reading data

        """
        self.open_serial_com_btn.setStyleSheet("QPushButton:checked {background-color: #A3C1DA; color: red;}")
        self.open_serial_com_btn.setText('Close Serial Connection')
        self.write_to_file()
        self.serialThread.used_port = self.used_port
        self.serialThread.start()

    def display_data(self, data, save_to_file=True):
        """
        Display data and save to file if requested

        """
        __x = [t[0] for t in data]
        __y = [t[1] for t in data]
        pw.setXRange(__x[0], __x[-1])
        pw.plot(__x, __y, clear=True, pen='r')
        if save_to_file:
            for entry, d_byte in enumerate(data):
                self.text_stream << entry << ",\t" << d_byte[0] << ",\t" << d_byte[1] << "\n"

    def write_to_file(self):
        """
        Automatically save data to a .csv file

        dir_name  - get current working directory
        file_name - the current time is taken for the name of the file
        file_ext  - let this be a .csv for now

        """
        dir_name = os.getcwd()
        file_name = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
        file_ext = ".csv"

        full_name = dir_name + "-" + file_name

        if QFile(full_name + file_ext).exists():
            self.current_file = QFile(full_name + '01' + file_ext)
        else:
            self.current_file = QFile(full_name + file_ext)

        self.current_file.open(QIODevice.WriteOnly)
        self.text_stream = QTextStream(self.current_file)

    def close_serial(self):
        """
        Close serial connection and reset button state

        """
        self.serialThread.isRunning = False
        self.serialThread.quit()
        self.current_file.close()
        self.statusInfoWidget.setText("Closed serial port")
        self.open_serial_com_btn.setText('Open Serial Connection')
        self.open_serial_com_btn.setStyleSheet("")

    def open(self):
        """
        Open file

        """
        file_name, _ = QFileDialog.getOpenFileName(self)
        if file_name:
            self.load_file(file_name)

    def load_file(self, file_name):
        """
        Load a file to display in pyqtgraph
        """
        data_file = QFile(file_name)
        if not data_file.open(QFile.ReadOnly | QFile.Text):
            QMessageBox.warning(self, "Application",
                    "Cannot read file %s:\n%s." % (file_name, data_file.errorString()))
            return False

        QApplication.setOverrideCursor(Qt.WaitCursor)
        data = QTextStream(data_file)

        while not data.atEnd():
            tmp_data_line = data.readLine().split(",")
            self.read_file_data.append((float(tmp_data_line[1].lstrip("\t")),
                                        int(tmp_data_line[2].lstrip("\t"))))
        self.display_data(self.read_file_data, save_to_file=False)
        QApplication.restoreOverrideCursor()

        self.set_current_file(file_name)
        self.statusInfoWidget.setText("File {} loaded successfully".format(file_name))

    def set_current_file(self, file_name):
        """
        Set the current opened filename in the footer

        """
        self.curFile = file_name
        self.setWindowModified(False)

        if self.curFile:
            shownName = QFileInfo(file_name).fileName()
        else:
            shownName = 'untitled.txt'

        self.setWindowTitle("{}[*] - Avalanche Desktop".format(shownName))

    def save_as(self):
        pass

    def create_actions(self):
        self.exitAct = QAction("&Exit", self, shortcut="Ctrl+Q",
                               statusTip="Exit the application", triggered=self.close)
        self.openAct = QAction("&Open...", self, shortcut=QKeySequence.Open,
                               statusTip="Open an existing file", triggered=self.open)
        self.saveAsAct = QAction("Save &As...", self, shortcut=QKeySequence.SaveAs,
                               statusTip="Save the document under a new name", triggered=self.save_as)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    avalancheDesktop = MainWindow()
    avalancheDesktop.show()

    pw = pg.PlotWidget(name='SerialPortPlot')
    pw.setLabel('left', 'Value', units='V')
    pw.setLabel('bottom', 'Time', units='s')
    pw.showGrid(True, True)
    avalancheDesktop.plotWidget.addWidget(pw)
    sys.exit(app.exec_())
