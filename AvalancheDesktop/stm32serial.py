import serial
from PyQt5.QtCore import (QThread, pyqtSignal)


class SerialThread(QThread):

    readLineSignal = pyqtSignal(bytes)

    def __init__(self, baudrate=9600, used_port=None, isRunning=True):
        super().__init__()

        self.baudrate = baudrate
        self.used_port = used_port
        self.isRunning = isRunning

        self.serial_port = None

    def run(self):
        try:
            if self.serial_port is not None:
                self.serial_port.close()
            self.serial_port = serial.Serial(port=self.used_port,
                                             baudrate=self.baudrate)
        except serial.SerialException as e:
            print(e)
            return

        while self.isRunning:
            data = self.serial_port.read()
            self.readLineSignal.emit(data)

        self.serial_port.close()
