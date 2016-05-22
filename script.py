import http.client
from xml.etree import ElementTree

def extractBookData(strXml):
    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    for item in itemElements:
        strTitle = item.find("yadmNm")
        if len(strTitle.text) > 0 :
            print("yadmNm : ",strTitle.text)


conn = http.client.HTTPConnection("openapi.hira.or.kr")

servicekey = "serviceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D"

conn.request("GET","/openapi/service/hospInfoService/getHospBasisList?" \
             +servicekey)

reg = conn.getresponse()
if int(reg.status) == 200:
    print("Book data downloading complete!")
    extractBookData(reg.read())
else:
    print("OpenAPI request has been failed!! please retry")
"""
cLen = reg.getheader("Content-Length")

xmlsrc = reg.read(cLen).decode("utf-8")
"""



