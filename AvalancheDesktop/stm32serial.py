import serial
from time import time, gmtime, strftime
from PyQt5.QtCore import (QThread, pyqtSignal)


class SerialThread(QThread):
    """
    A separate thread to handle communication with STM32 virtual com port
    for reading data and issuing start/stop commands
    """
    readLineSignal = pyqtSignal(list)

    def __init__(self, baudrate=9600, used_port=None, isRunning=False, acquisition_time=1000):
        super().__init__()

        self.baudrate = baudrate
        self.used_port = used_port
        self.isRunning = isRunning
        self.acquisition_time = acquisition_time
        self.serial_port = None

    def run(self):
        try:
            if self.serial_port is not None:
                self.serial_port.close()
            self.serial_port = serial.Serial(port=self.used_port,
                                             baudrate=self.baudrate)
            self.isRunning = True

            # Start of acquisiton time
            self.serial_port.write((83).to_bytes(1, byteorder='big'))
            self.serial_port.write((self.acquisition_time).to_bytes(2, byteorder='big'))  # should make a check here, otherwise an error may occur

            start_timestamp = time()
        except serial.SerialException as e:
            print(e)
            return

        data_arr = []
        while self.isRunning:
            if len(data_arr) <= self.baudrate / 10:
                data_arr.append((strftime("%H:%M:%S", gmtime()), (time() - start_timestamp),
                                 int.from_bytes(self.serial_port.read(), byteorder='big'),
                                 ))
            else:
                self.readLineSignal.emit(data_arr)
                data_arr = []

        self.serial_port.close()




