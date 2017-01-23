#-*- coding: utf-8 -*-
import os
import parsing_engine
import res_db


# .PST 파일인지, .EML 파일인지 검사하고, 적절히 처리!
def eml_file_handling(thefile):

    if thefile.endswith('.eml'):
        try:
            fp = open(thefile, "r")
            fileContents = fp.read()
        except:
            print '.eml file processing error'

        finally:
            parsedData = parsing_engine.parsing(fileContents)
            parsedData.ip_addr_parsing() # 송신자 IP 주소 파싱
            parsedData.send_date_parsing() # 송신 날짜 파싱
            parsedData.recv_date_parsing() # 수신 날짜 파싱
            parsedData.subject_parsing() # 제목 파싱
            parsedData.content_parsing() # 본문 파싱
            parsedData.debug_print()
            fp.close()

    elif thefile.endswith('.pst'):
        #.pst 변환 과정
        pass