# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:07:26 2016

@author: kkk
"""
from http.client import HTTPConnection
from urllib.parse   import quote
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from hospital import Hospihal as hospi
from xml.etree import ElementTree




##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None
sidoName=None
sgguName=None
Hname=None
Hdata = []



#### Menu  implementation
def printMenu():
    print("\nWelcome! hospital Manager Program (http version)") 
    print("========Menu==========")
    print("시에대한 HTTP 불러오기:  l")
    print("찾을 병원 이름 : h")
    print("Print: p")
    print("mail : m")
    print("Quit program:   q")
    print("print Book list: b")
    print("sEarch Book Title: e")
    print("==================")


def launcherFunction(menu):
    global HospitalDoc, Code, sidoName, Hname
    if menu ==  'l':
        LoadXMLFromHTTP()  
    elif menu == 'q':
        QuitBookMgr()
    elif menu=='h':
        LoadHospitalName()
    elif menu == 'p':
        if sidoName==None:
            print("시,도에대한 정보가없습니다.")
        elif Hname==None:
            print("병원이름에대한정보가없습니다.")
        else :
            extractBookData(HospitalDoc.read().decode('utf-8'))
    elif menu == 'm':
        if sidoName == None:
            print("시,도에대한 정보가없습니다.")
        elif Hname == None:
            print("병원이름에대한정보가없습니다.")
        else:
            mail();
#    elif menu == 'b':
#        PrintBookList(["title",])    
#    elif menu == 'e':
#        keyword = str(input ('input keyword to search :'))
#        printBookList(SearchBookTitle(keyword))

    else:
        print ("error : unknow menu key")

def LoadHospitalName():
    global HospitalDoc, Code, sidoName,Hname
    conn = HTTPConnection("openapi.hira.or.kr")
    Hospital = quote(input("please input hospital name to load :"))
    Hname = "yadmNm=" + Hospital + "&"  # 읽어올 파일경로를 입력 받습니다.
    print(sidoName      ,  Hname)
    conn.request("GET","/openapi/service/hospInfoService/getHospBasisList?" + sidoName+ Hname+"numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
    req = conn.getresponse()
    HospitalDoc = req
    return None

def connectOpenAPIServer():
    global conn, server
    server="openapi.hira.or.kr"
    conn = HTTPConnection(server)

def extractBookData(strXml):
    global Hdata,sgguName
    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    m_count=0
    for item in itemElements:
        sgguNmTitle = item.find("sgguCdNm")
        #print(sgguName)
        #print(sgguNmTitle.text)
        if sgguNmTitle.text== sgguName:
            yadmname=item.find("yadmNm")
            addrname= item.find("addr")
            data = hospi(yadmname.text,addrname.text)
            m_count+=1
            Hdata.append(data)
    for dada in range(m_count):
         print("병원이름 : ",Hdata[dada].yadm)
         print("주소 : ",Hdata[dada].addr)


   
def mail():
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    ID = input("(gmail)ID : ") + "@gmail.com"
    password= input("password : ")
    senderAddr = ID # 보내는 사람
    title = input(" 제목 : ")
    recipientAddr = input("받는 사람:")  # 받는 사람
    text = input(" 내용 : ")  # 보내는 내용


    msg = MIMEText(text, _charset='utf8')

    msg['Subject'] = Header(title, 'utf8')
    msg['From'] = senderAddr
    msg['To'] = recipientAddr

    s.login(ID, password)
    s.sendmail(senderAddr, recipientAddr, msg.as_string())
    s.quit()

def LoadXMLFromHTTP():
    global HospitalDoc,Code,sidoName,sgguName
    Code={'서울':'110000','부산':'210000','인천':'220000'
    ,'대구':'230000','경남':'380000','경기':'310000',
    '충남':'340000','강원':'320000','전북':'350000','광주':'240000'
    ,'충북':'330000','울산':'260000','전남':'360000','대전':'250000'
    ,'경북':'370000','제주':'390000','세종시':'410000'}
    print(list(Code.keys()))
    conn = HTTPConnection("openapi.hira.or.kr")
    sido=str(input ("please input sido name to load :"))
    sidoName ="sidoCd="+ Code[sido]+"&"  # 읽어올 파일경로를 입력 받습니다.

    conn.request("GET", "/openapi/service/hospInfoService/getHospBasisList?"+sidoName+"numOfRows=100&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
    req = conn.getresponse()
    print(req.status, req.reason)
    HospitalDoc = req

    tree = ElementTree.fromstring(req.read().decode('utf-8'))
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    print("-------------------------------")
    sggulist=[]
    sggunumber=0
    for item in itemElements:
        check = True
        for i in range(sggunumber):
            if sggulist[i] == item.find("sgguCdNm").text:
                check = False
        if check == True:
            sggulist.append(item.find("sgguCdNm").text)
            sggunumber += 1
    for i in range(sggunumber):
        if i % 10 == 0:
            print()
        print(sggulist[i], end=" ")
    print("")
    print("-----------------------------------------")
    sggu = str(input("please input sggu name to load :"))
    sgguName = sggu

    conn = HTTPConnection("openapi.hira.or.kr")
    conn.request("GET","/openapi/service/hospInfoService/getHospBasisList?" + sidoName + "numOfRows=100&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
    req = conn.getresponse()
    print(req.status, req.reason)
    HospitalDoc = req
    return None

def ReLoadHTTP():
    global HospitalDoc, Code, sidoName,Hname
    conn = HTTPConnection("openapi.hira.or.kr")
    if sidoName!=None:
        conn.request("GET","/openapi/service/hospInfoService/getHospBasisList?" + sidoName+ Hname + "numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
        req = conn.getresponse()
        print(req.status, req.reason)
        HospitalDoc = req
        return None
    else :
        print("시에대한 정보가 없습니다.")




def QuitBookMgr():
    global loopFlag
    loopFlag = 0
  #  BooksFree()





##### run #####
while(loopFlag > 0):
    printMenu()
    menuKey = str(input ('select menu :'))
    launcherFunction(menuKey)
else:
    print ("Thank you! Good Bye")