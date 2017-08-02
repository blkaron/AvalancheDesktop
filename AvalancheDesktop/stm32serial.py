import serial
from time import time
from PyQt5.QtCore import (QThread, pyqtSignal)


class SerialThread(QThread):

    readLineSignal = pyqtSignal(list)

    def __init__(self, baudrate=9600, used_port=None, isRunning=False):
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
            self.isRunning = True
            start_timestamp = time()
        except serial.SerialException as e:
            print(e)
            return

        data_arr = []
        while self.isRunning:
            if len(data_arr) <= self.baudrate / 10:
                data_arr.append(((time() - start_timestamp),
                                int.from_bytes(self.serial_port.read(), byteorder='big')))
            else:
                self.readLineSignal.emit(data_arr)
                data_arr = []

        self.serial_port.close()
