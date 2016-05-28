# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:07:26 2016

@author: kkk
"""
from http.client import HTTPConnection
from urllib.parse   import quote




##### global
loopFlag = 1
xmlFD = -1
BooksDoc = None

#### Menu  implementation
def printMenu():
    print("\nWelcome! hospital Manager Program (http version)") 
    print("========Menu==========")
    print("Load http:  l")
    print("Print dom to xml: p")
    print("Quit program:   q")
    print("print Book list: b")
    print("sEarch Book Title: e")
    print("==================")


def launcherFunction(menu):
    global HospitalDoc
    global cLen
    if menu ==  'l':
        LoadXMLFromHTTP()  
    elif menu == 'q':
        QuitBookMgr()
    elif menu == 'p':     
        extractBookData(HospitalDoc.read().decode('utf-8'))
#    elif menu == 'b':
#        PrintBookList(["title",])    
#    elif menu == 'e':
#        keyword = str(input ('input keyword to search :'))
#        printBookList(SearchBookTitle(keyword))

    else:
        print ("error : unknow menu key")



def connectOpenAPIServer():
    global conn, server
    server="openapi.hira.or.kr"
    conn = HTTPConnection(server)
  

def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    for item in itemElements:
        strTitle = item.find("sidoCdNm")
        if len(strTitle.text) > 0 :
            print("sidoNm : ",strTitle.text)
   


def LoadXMLFromHTTP():
    global HospitalDoc,Code
    Code={'서울':'110000','부산':'210000','인천':'220000'
    ,'대구':'230000','경남':'380000','경기':'310000',
    '충남':'340000','강원':'320000','전북':'350000','광주':'240000'
    ,'충북':'330000','울산':'260000','전남':'360000','대전':'250000'
    ,'경북':'370000','제주':'390000','세종시':'410000'}
    conn = HTTPConnection("openapi.hira.or.kr")
    sido=str(input ("please input sido name to load :"))
    print(Code[sido])
    sidoName ="sidoCd="+ Code[sido]+"&"  # 읽어올 파일경로를 입력 받습니다.
    sgguName = "sgguCd="+quote(input ("please input sggu name to load :"))+"&"  # 읽어올 파일경로를 입력 받습니다.
    print(quote(sidoName))
    conn.request("GET", "/openapi/service/hospInfoService/getHospBasisList?"+sidoName+sgguName+"numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D") 
    req = conn.getresponse()   
    print(req.status,req.reason)
    HospitalDoc=req
    return None   



    

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