#-*- coding: utf-8 -*-

import urllib
import json

def get_ip_info(ip_addr):

    #whois_api_key = 2017010901372246522659
    #ip주소와 도메인으로 검색할 때 각각 결과가 다름

    whois_ip_url = "http://whois.kisa.or.kr/openapi/whois.jsp?" \
                   "query="+ ip_addr +"&" \
                   "key=2017010901372246522659&" \
                   "answer=json"
    result = urllib.urlopen(whois_ip_url)
    ip_info = result.read()
    result.close()
    return ip_info_parsing(ip_info)

def ip_info_parsing(ip_info):
    print "[debug]", ip_info
    json_info = json.loads(ip_info)

    if 'korean' in json_info['whois']: # 한국 IP 검색할 때
        countryCode = json_info['whois']['countryCode']
        orgName = json_info['whois']['korean']['user']['netinfo']['orgName']
        addr = json_info['whois']['korean']['user']['netinfo']['addr']
        zipCode = json_info['whois']['korean']['user']['netinfo']['zipCode']
        regDate = json_info['whois']['korean']['user']['netinfo']['regDate']
        name = json_info['whois']['korean']['user']['techContact']['name']
        phone = json_info['whois']['korean']['user']['techContact']['phone']
        email = json_info['whois']['korean']['user']['techContact']['email']

        res = "CountryCode : " + countryCode + "\n"
        res += "OrgName : " + orgName + "\n"
        res += "Address : " + addr + "\n"
        res += "ZipCode : " + zipCode + "\n"
        res += "RegDate : " + regDate + "\n"
        res += "Name : " + name + "\n"
        res += "Phone : " + phone + "\n"
        res += "Email : " + email
    else: # 그외 국가 IP 검색할 때
        countryCode = json_info['whois']['countryCode']
        registry = json_info['whois']['registry']

        res = "CountryCode : " + countryCode + "\n"
        res += "Registry : " + registry



    return res

