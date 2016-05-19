# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:07:26 2016

@author: kkk
"""

import http.client

conn = http.client.HTTPConnection("openapi.hira.or.kr")
conn.request("GET", "/openapi/service/hospInfoService/getHospBasisList?pageNo=1&numOfRows=10&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D") 
req = conn.getresponse()
cLen = req.getheader("Content-Length") 
req.read(cLen).decode('utf-8')