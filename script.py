import http.client
from xml.dom.minidom import *

conn = http.client.HTTPConnection("openapi.hira.or.kr")

servicekey = "serviceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D"

conn.request("GET","/openapi/service/hospInfoService/getHospBasisList?" \
             +servicekey)

reg = conn.getresponse()

cLen = reg.getheader("Content-Length")

xmlsrc = reg.read(cLen).decode("utf-8")

doc = parseString(xmlsrc)


