# -*- coding: utf-8 -*-
"""
@Author : Seon Ho Lee (IT4211)
@E-mail : rhdqor100@live.co.kr
@Description : Handling and parsing large amounts of eml files
"""

import multiprocessing
import sys
import glob
from PyQt4 import QtGui, QtCore
from main_form import *
import whois_search
import parsing_engine
import res_db


class parser_window(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.actionOpen.triggered.connect(self.browse_folder)
        self.ui.IPSearch_Button.clicked.connect(self.ip_search)
        self.ui.parsing_pushButton.clicked.connect(self.eml_parsing)
        self.ui.dbpath_pushButton.clicked.connect(self.db_save_path)
        self.rowPosition = self.ui.parse_res_tableWidget.rowCount()
        self.ui.parse_res_tableWidget.insertRow(self.rowPosition)
        self.header = self.ui.parse_res_tableWidget.horizontalHeader()
        #self.header.setResizeMode(0, QtGui.QHeaderView.Stretch)
        self.header.setResizeMode(1, QtGui.QHeaderView.ResizeToContents)
        self.header.setResizeMode(2, QtGui.QHeaderView.ResizeToContents)
        self.header.setResizeMode(3, QtGui.QHeaderView.ResizeToContents)

    def browse_folder(self):
        self.directory = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.pathdisplay_lineEdit.setText(self.directory)

    def db_save_path(self):
        self.savepath = QtGui.QFileDialog.getExistingDirectory(self, "Select Directory")
        self.ui.dbpath_lineEdit.setText(self.savepath)

    def ip_search(self):
        ip_addr = self.ui.IPinput_lineEdit.text()
        # 실제 정확한 ip address를 입력했는지 검증할 것! 정규표현식 등 ..
        result = whois_search.get_ip_info(str(ip_addr))
        self.ui.Whois_res_TextEdit.setText(result)

    def eml_parsing(self):
        try:
            emlDir = str(self.directory) + "\\"
            # multi processing !!
            corePool = multiprocessing.Pool(processes=4)
            # GUI를 통해서 폴더 명이 들어오면, 그 폴더명은 emldir 이라는 변수에 저장
            # 그리고 그 폴더 내에 있는 목록을 얻어 와야한다.
            self.listOfFiles = glob.glob(emlDir + "*.eml")
            # 파일이 정말 많을 때
            # for i in glob.iglob("*.eml"):
            # 4개를 돌아가면서 넣어주기?
            if len(self.listOfFiles) > 3:
                corePool.map(self.eml_file_handling, (0,1,2,3))

            elif len(self.listOfFiles) == 1:
                # Test case
                self.eml_file_handling(0)
            else:
                print "[err] Too few files.", len(self.listOfFiles), self.listOfFiles
        except AttributeError:
            self.warning_message("Please specify the path to the eml file.")

    def eml_file_handling(self, no):
        for i in range(0, len(self.listOfFiles), 4):
            thefile = self.listOfFiles[i + no]
        # db 저장할 경로 입력 받기
        try:
            db_path = str(self.savepath)
            result_db = res_db.sqlite_db(db_path, no)
        except AttributeError:
            self.warning_message("Specify the path to save the db file.")
            return

        if thefile.endswith('.eml'):
            try:
                fp = open(thefile, "r")
                fileContents = fp.read()
                parsedData = parsing_engine.parsing(fileContents)
                parsedData.ip_addr_parsing()  # 송신자 IP 주소 파싱
                parsedData.send_date_parsing()  # 송신 날짜 파싱
                parsedData.recv_date_parsing()  # 수신 날짜 파싱
                parsedData.subject_parsing()  # 제목 파싱
                parsedData.content_parsing()  # 본문 파싱
                parsedData.debug_print()

                self.ui.parse_res_tableWidget.setItem(self.rowPosition, 0, QtGui.QTableWidgetItem(str(parsedData.subject)))
                self.ui.parse_res_tableWidget.setItem(self.rowPosition, 1, QtGui.QTableWidgetItem(str(parsedData.ip_addr)))
                self.ui.parse_res_tableWidget.setItem(self.rowPosition, 2, QtGui.QTableWidgetItem(str(parsedData.send_date)))
                self.ui.parse_res_tableWidget.setItem(self.rowPosition, 3, QtGui.QTableWidgetItem(str(parsedData.recv_date)))
                #self.ui.parse_res_tableWidget.setItem(self.rowPosition, 4, QTableWidgetItem=parsedData.)

                fp.close()

            except IOError as e:
                print "[err] File IO error", e

        elif thefile.endswith('.pst'):
            # .pst 변환 과정
            pass

    def warning_message(self, msg):
        print "[debug]  ", msg
        wmsg = QtGui.QMessageBox()
        wmsg.setIcon(QtGui.QMessageBox.Warning)
        wmsg.setText(msg)
        wmsg.setWindowTitle("Eml_parser")
        wmsg.setStandardButtons(QtGui.QMessageBox.Ok)
        ret = wmsg.exec_()



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    eml_parser = parser_window()
    eml_parser.show()
    app.exec_()

