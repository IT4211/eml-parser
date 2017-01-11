#-*- coding: utf-8 -*-

# 전송한 사람의 ip 주소 파싱, 발신일시, 수신일시, 제목, 본문

import sqlite3
import re

class parsing():
    def __init__(self, emlcontents):
        self.emlcontents = emlcontents

    def ip_addr_parsing(self):
        reg_from_ip = r"[Ff]rom[:]? \b\d{1,3}[.]\d{1,3}[.]\d{1,3}[.]\d{1,3}\b"
        reg_ip_addr = r"(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((1[0-9]{2})|(2[0-4]\d)|(25[0-5])|(\d{1,2}))"
        from_ip = re.findall(reg_from_ip, self.emlcontents)
        ip_addr = re.findall(reg_ip_addr, from_ip[0])
        if len(ip_addr): # 유효한 IP 주소가 파싱됬다면
            self.ip_addr = ip_addr

    """
    eml file timestamp format example
    Mon, 26 Dec 2016 08:18:39 +0900
    24 Dec 2016 00:50:28 -0000
    30 Nov 2016 21:09:42 -0000
    전송 시간은 Date: 로 시작함!!!
    정규 표현식 더욱 정교하게 작성해야 됨!!!
    """
    def send_date_parsing(self):
        regex_send_date = r"(\b[Dd]ate:) ( )?\d{2} (Dec) \d{4} (\d{2}:\d{2}:\d{2}) (-|\+)(\d{4})"
        send_date = re.findall(regex_send_date, self.emlcontents)
        self.send_date = send_date
        # TODO: 유효한 날짜인가 검증하는 부분

    def recv_date_parsing(self):
        regex_recv_date = r"(\b[Rr]eceived:)( )?((\(qmail )\d{4}( invoked from network\);))? \d{2} (Dec|Nov) \d{4} (\d{2}:\d{2}:\d{2}) (-|\+)(\d{4})"
        recv_date = re.findall(regex_recv_date, self.emlcontents)
        self.recv_date = recv_date
        #TODO: 유효한 날짜인가 검증하는 부분

    def subject_parsing(self):
        regex_subject = r"(\bSubject: ).*"
        subject = re.findall(regex_subject, self.emlcontents)
        self.subject = subject
        #TODO: 메일 제목이 base64인 경우를 판단!