#!/usr/bin/python

# simple.py

import sys
from PyQt4 import QtGui

app = QtGui.QApplication(sys.argv)

widget = QtGui.QWidget()
widget.resize(550, 350)
widget.setWindowTitle('text')

widget.show()


sys.exit(app.exec_())

