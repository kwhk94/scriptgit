from http.client import HTTPConnection
from urllib.parse   import quote
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from hospital import Hospihal as hospi
from xml.etree import ElementTree


Code={'서울':'110000','부산':'210000','인천':'220000'
,'대구':'230000','경남':'380000','경기':'310000',
'충남':'340000','강원':'320000','전북':'350000','광주':'240000'
,'충북':'330000','울산':'260000','전남':'360000','대전':'250000'
,'경북':'370000','제주':'390000','세종시':'410000'}
print(list(Code.keys()))
conn = HTTPConnection("openapi.hira.or.kr")
sido=str(input ("please input sido name to load :"))
sidoName ="sidoCd="+ Code[sido]+"&"  # 읽어올 파일경로를 입력 받습니다.

conn.request("GET", "/openapi/service/hospInfoService/getHospBasisList?"+sidoName+"numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
req = conn.getresponse()
tree = ElementTree.fromstring(req.read().decode('utf-8'))
# Book 엘리먼트를 가져옵니다.
itemElements = tree.getiterator("item")  # return list type
print("-------------------------------")
sggulist = []
sggunumber = 0

for item in itemElements:
    check= True
    for i in range(sggunumber):
        if sggulist[i] == item.find("sgguCdNm").text:
            check = False
    if check == True:
        sggulist.append(item.find("sgguCdNm").text)
        sggunumber+=1

for i in range(sggunumber):
    if i%10==0 :
        print()
    print(sggulist[i],end=" ")
