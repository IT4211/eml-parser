#-*- coding: utf-8 -*-


def eml_file_handling(emlfile):
    try:
        fp = open(emlfile, "r")
        buffer = fp.read()
    except:
        print '.eml file processing error'