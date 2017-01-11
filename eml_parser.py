# -*- coding: utf-8 -*-
"""
@Author : Seon Ho Lee (IT4211)
@E-mail : rhdqor100@live.co.kr
@Description : Handling and parsing large amounts of eml files
"""

import multiprocessing
import sys
from PyQt4 import QtGui, QtCore
from main_form import *
import whois_search

class parser_window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

    def ip_search(self):
        ip_addr = self.ui.IPinput_lineEdit.text()
        # 실제 정확한 ip address를 입력했는지 검증할 것! 정규표현식 등 ..
        whois_search.get_ip_info(ip_addr)




if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    eml_parser = parser_window()
    eml_parser.show()
    app.exec_()

    # multi processing !!
    corePool = multiprocessing.Pool(processes=4)

