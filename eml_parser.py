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
from eml_file_handler import eml_file_handling


class parser_window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.browse_folder)

    def browse_folder(self):
        self.directory = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")

    def ip_search(self):
        ip_addr = self.ui.IPinput_lineEdit.text()
        # 실제 정확한 ip address를 입력했는지 검증할 것! 정규표현식 등 ..
        whois_search.get_ip_info(ip_addr)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    eml_parser = parser_window()
    eml_parser.show()
    app.exec_()


    print eml_parser.directory
    # multi processing !!
    corePool = multiprocessing.Pool(processes=1)

    # GUI를 통해서 폴더 명이 들어오면, 그 폴더명은 emldir 이라는 변수에 저장
    # 그리고 그 폴더 내에 있는 목록을 얻어 와야한다.
    # listOfFiles = os.listdir(emldir) ? glob ?
    #
    result = corePool.map(eml_file_handling, ("test.eml"))
    #res = eml_file_handling("test.eml")

