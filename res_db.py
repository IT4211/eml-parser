#-*- coding: utf-8 -*-

import sqlite3

class sqlite_db():

    def __init__(self, path):
        self.create_sqlite(path)

    def create_sqlite(self, path):
        self.sqlname = path + "result.db"
        con = sqlite3.connect(self.sqlname)  # database create
        con.text_factory = str()
        cursor = con.cursor()

        sql = "CREATE TABLE result(" \
              "ip_address text, " \
              "send_date text, " \
              "recv_date text, " \
              "subject text, " \
              "contents text, " \
              "attach_file text, " \
              "hash text)"
        cursor.execute(sql)

    def ins_sqlite(self, ):
        con = sqlite3.connect(self.sqlname)  # database create
        con.text_factory = str()
        cursor = con.cursor()

        cursor.execute("INSERT INTO result VALUES(?,?,?,?,?,?,?)",
                       (self.ip_addr, self.sdate, self.rdate, self.subject, self.body, self.file_name, self.hash))
        con.commit()
        con.close()