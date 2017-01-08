#-*- coding: utf-8 -*-

import os
import sqlite3

def create_sqlite(path):
    sqlname = path + "result.db"
    con = sqlite3.connect(sqlname)  # database create
    con.text_factory = str()
    cursor = con.cursor()

    sql = "CREATE TABLE result(" \
          "IP Address text, " \
          "send_date text, " \
          "recv_date text, " \
          "title text, " \
          "body text, " \
          "file_name text, " \
          "hash text)"
    cursor.execute(sql)


def ins_sqlite(self, path):
    sqlname = path + "result.db"
    con = sqlite3.connect(sqlname)  # database create
    con.text_factory = str()
    cursor = con.cursor()

    cursor.execute("INSERT INTO result VALUES(?,?,?,?,?,?,?)", (self.ip_addr, self.sdate, self.rdate, self.title, self.body, self.file_name, self.hash))
    con.commit()
    con.close()