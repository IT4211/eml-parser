#-*- coding: utf-8 -*-

# 전송한 사람의 ip 주소 파싱, 발신일시, 수신일시, 제목, 본문

import email
import re

class parsing():
    def __init__(self, emlcontents):
        self.emlcontents = emlcontents
        self.texthtml = ""
        self.textplain = ""

    def ip_addr_parsing(self):
        reg_from_ip = r"([Ff]rom[:]? (((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((1[0-9]{2})|(2[0-4]\d)|(25[0-5])|(\d{1,2})))"
        #reg_ip_addr = r"(((\d{1,2})|(1\d{2})|(2[0-4]\d)|(25[0-5]))\.){3}((1[0-9]{2})|(2[0-4]\d)|(25[0-5])|(\d{1,2}))"
        #reg_ip_addr = ((?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?))
        from_ip = re.findall(reg_from_ip, self.emlcontents)
        self.ip_addr = from_ip[0][0]

    """
    eml file timestamp format example
    Mon, 26 Dec 2016 08:18:39 +0900
    24 Dec 2016 00:50:28 -0000
    30 Nov 2016 21:09:42 -0000
    전송 시간은 Date: 로 시작함!!!
    정규 표현식 더욱 정교하게 작성해야 됨!!!
    """
    def send_date_parsing(self):
        regex_send_date = r"(\b[Dd]ate: ?)(\d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} [\-\+]\d{4})"
        send_date = re.findall(regex_send_date, self.emlcontents)
        self.send_date = send_date
        # TODO: 유효한 날짜인가 검증하는 부분

    def recv_date_parsing(self):
        regex_recv_date = r"(\bReceived: ?)(\([\w\d ]*\)\;)? (\d{2} \w{3} \d{4} \d{2}:\d{2}:\d{2} [\-\+]\d{4})"
        recv_date = re.findall(regex_recv_date, self.emlcontents)
        self.recv_date = recv_date
        #TODO: 유효한 날짜인가 검증하는 부분

    def subject_parsing(self):
        regex_subject = r"(\bSubject: )([\w ].*)"
        subject = re.findall(regex_subject, self.emlcontents)
        self.subject = subject
        #TODO: 메일 제목이 base64인 경우를 판단!

    def content_parsing(self):
        msg = email.message_from_string(self.emlcontents)
        for part in msg.walk():
            charset = part.get_content_charset()
            print "[debug]  ", charset
            if part.get_content_type() == 'text/plain':
                self.textplain = part.get_payload()

            elif part.get_content_type == 'text/html':
                self.texthtml = part.get_payload()
                # html 파일로 떨구는 부분 생각해보기!

    def attach_file_parsing(self):
        pass

    def debug_print(self):
        print "[debug]  ", self.ip_addr
        print "[debug]  ", self.send_date
        print "[debug]  ", self.recv_date
        print "[debug]  ", self.subject
        #print "[debug]  ", self.textplain
        #print "[debug]  ", self.texthtml