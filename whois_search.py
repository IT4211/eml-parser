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

import urllib
import json

def get_ip_info(ip_addr):

    whois_api_key = 2017010901372246522659

    whois_ip_url = "http://whois.kisa.or.kr/openapi/whois.jsp?" \
                   "query="+ ip_addr +"&" \
                   "key=2017010901372246522659&" \
                   "answer=json"
    ip_info = urllib.urlopen(whois_ip_url)
    print ip_info.read()

