# -*- coding: utf-8 -*-
"""
Created on Thu May 19 13:07:26 2016

@author: kkk
"""

import http.client




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

def extractBookData(strXml):
    from xml.etree import ElementTree
    tree = ElementTree.fromstring(strXml)
    # Book 엘리먼트를 가져옵니다.
    itemElements = tree.getiterator("item")  # return list type
    for item in itemElements:
        strTitle = item.find("yadmNm")
        if len(strTitle.text) > 0 :
            print("yadmNm : ",strTitle.text)
   


def LoadXMLFromHTTP():
    global HospitalDoc
    conn = http.client.HTTPConnection("openapi.hira.or.kr")
    sidoName ="sidoCd="+ str(input ("please input sido name to load :"))+"&"  # 읽어올 파일경로를 입력 받습니다.
    sgguName = "sgguCd="+str(input ("please input sggu name to load :"))+"&"  # 읽어올 파일경로를 입력 받습니다.
   
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