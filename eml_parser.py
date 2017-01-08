# -*- coding: utf-8 -*-
"""
@Author : Seon Ho Lee (IT4211)
@E-mail : rhdqor100@live.co.kr
@
"""

import sys
from PyQt4 import QtGui, QtCore
from main_form import *

class parser_window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    eml_parser = parser_window()
    eml_parser.show()
    app.exec_()