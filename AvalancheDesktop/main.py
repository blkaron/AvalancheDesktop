# This is a temporary main file to test the project functionality

import os
import sys

from resources import pyqtgraph as pg
from resources.pyqtgraph.Qt import QtCore, QtGui
import numpy as np

app = QtGui.QApplication([])
win = QtGui.QMainWindow()
btn = pg.ColorButton()
win.setCentralWidget(btn)
win.show()
win.setWindowTitle('pyqtgraph example: ColorButton')

def change(btn):
    print("change", btn.color())

def done(btn):
    print("done", btn.color())


btn.sigColorChanging.connect(change)
btn.sigColorChanged.connect(done)


def main():
    pass


if __name__ == '__main__':
    QtGui.QApplication.instance().exec_()
