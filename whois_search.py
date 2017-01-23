#-*- coding: utf-8 -*-
"""
whois 검색 결과 : json 형태
파싱할 내용 및 json 항목
['whois']['contryCode']
['whois']['korean']['user']['netinfo']['orgName']
['whois']['korean']['user']['netinfo']['orgID']
['whois']['korean']['user']['netinfo']['addr']
['whois']['korean']['user']['netinfo']['zipCode']
['whois']['korean']['user']['netinfo']['regDate']
['whois']['korean']['user']['techContact']['name']
['whois']['korean']['user']['techContact']['phone']
['whois']['korean']['user']['techContact']['email']
json 정렬 : http://json.parser.online.fr/
"""

import struct
import urllib
import json

def get_ip_info(ip_addr):

    #whois_api_key = 2017010901372246522659
    #ip주소와 도메인으로 검색할 때 각각 결과가 다름

    whois_ip_url = "http://whois.kisa.or.kr/openapi/whois.jsp?" \
                   "query="+ ip_addr +"&" \
                   "key=2017010901372246522659&" \
                   "answer=json"
    ip_info = urllib.urlopen(whois_ip_url)
    print ip_info.read()

def ip_info_parsing(ip_info):
    json_info = json.loads(ip_info)

    contryCode = json_info['whois']['contryCode']
    orgName = json_info['whois']['korean']['user']['netinfo']['orgName']
    addr = json_info['whois']['korean']['user']['netinfo']['addr']
    zipCode = json_info['whois']['korean']['user']['netinfo']['zipCode']
    regDate = json_info['whois']['korean']['user']['netinfo']['regDate']
    name = json_info['whois']['korean']['user']['techContact']['name']
    phone = json_info['whois']['korean']['user']['techContact']['phone']
    email = json_info['whois']['korean']['user']['techContact']['email']








