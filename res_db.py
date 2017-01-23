#-*- coding: utf-8 -*-

import os
import sqlite3

class res_db():

    def __init__(self, path):
        self.create_sqlite(path)

    def create_sqlite(self, path):
        sqlname = path + "result.db"
        con = sqlite3.connect(sqlname)  # database create
        con.text_factory = str()
        cursor = con.cursor()

        sql = "CREATE TABLE result(" \
              "IP Address text, " \
              "send_date text, " \
              "recv_date text, " \
              "subject text, " \
              "body text, " \
              "file_name text, " \
              "hash text)"
        cursor.execute(sql)

    def ins_sqlite(self, path, ):
        sqlname = path + "result.db"
        con = sqlite3.connect(sqlname)  # database create
        con.text_factory = str()
        cursor = con.cursor()

        cursor.execute("INSERT INTO result VALUES(?,?,?,?,?,?,?)",
                       (self.ip_addr, self.sdate, self.rdate, self.subject, self.body, self.file_name, self.hash))
        con.commit()
        con.close()