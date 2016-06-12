import sys
from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


import hosdata
import search
import webbrowser
from http.client import HTTPConnection
from urllib.parse   import quote
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from hospital import Hospihal as hospi
from xml.etree import ElementTree
import near
import mail

##### global
BooksDoc = None
sidoName=None
sgguName=None
Hname=None
Hdata = []
ID=""
password=""
recipientAddr=""
finaldata=None
m_count=0
HospitalDoc=None
serviceKey="numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D"
conn = HTTPConnection("openapi.hira.or.kr")


class MyForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self,parent)
        self.ui = hosdata.Ui_MainWindow()
        self.ui.setupUi(self)
        if finaldata!=None:
            self.ui.textBrowser.append(finaldata.yadm)
            self.ui.textBrowser.append(finaldata.addr)
            self.ui.textBrowser.append(finaldata.url)
       # self.show(self)

    def slot1_click(self): #검색
         self.search=SearchForm()
         self.search.show()
         self.close()
         return

    def slot2_click(self): #지도
        if finaldata!=None:
            print(finaldata.xpos,finaldata.ypos)
            if finaldata.xpos!=None and finaldata.ypos!=None:
                url='https://www.google.co.kr/maps/@'+finaldata.ypos+','+finaldata.xpos+',17z'
                webbrowser.open_new(url)
            else:
                print("좌표가없습니다")
                self.ui.textBrowser.append("좌표가없습니다")

    def slot3_click(self): #홈페이지
        if finaldata!=None:
            if finaldata.url!=None:
                url = finaldata.url
                webbrowser.open_new(url)
            else:
                print("주소가없습니다.")
                self.ui.textBrowser.append("주소가없습니다")

    def slot4_click(self): #인근병원
        print("클릭")
        if finaldata != None:
            print("클릭1")
            self.search = NearForm()
            print("클릭2")
            self.search.show()
            print("클릭3")
            self.close()
            print("클릭4")
            
    def slot5_click(self): #길찾기
        if finaldata!=None:
           print(finaldata.xpos,finaldata.ypos)
           if finaldata.xpos!=None and finaldata.ypos!=None:
               url='https://www.google.co.kr/maps/dir//'+finaldata.ypos+','+finaldata.xpos+'/@'+finaldata.ypos+','+finaldata.xpos+',17z'
               webbrowser.open_new(url)
           else:
               print("좌표가없습니다")
               self.ui.textBrowser.append("좌표가없습니다")
               
    def slot6_click(self): #메일
        if finaldata != None:
            self.mail = mailForm()
            self.mail.show()
            self.close()
            
class mailForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = mail.Ui_dialog()
        self.ui.setupUi(self)
    def slot1_click(self):
        maildata=""
        global finaldata
        maildata = maildata + finaldata.yadm + "\n"+ finaldata.addr
        text = maildata
        self.MyForm = MyForm()
        self.MyForm.show()
        self.close()
    def slot3_click(self):
        self.MyForm = MyForm()
        self.MyForm.show()
        self.close()
     
def sendmail(ID,password,senderAddr, recipientAddr,text):
    title="병원정보"
    ID = ID + "@gmail.com"
    msg = MIMEText(text, _charset='utf8')
    msg['Subject'] = Header(title, 'utf8')
    msg['From'] = senderAddr
    msg['To'] = recipientAddr
    s = smtplib.SMTP("smtp.gmail.com", 587)
    s.ehlo()
    s.starttls()
    s.ehlo()    
    s.login(ID, password)
    s.sendmail(senderAddr, recipientAddr, msg.as_string())
    s.quit()
     
class NearForm(QtGui.QMainWindow):
    def __init__(self,parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = near.Ui_Form()
        self.ui.setupUi(self)
        global Code, sidoName, conn, HospitalDoc, sggunumber, ssgname,Neardata,m_neardata
        conn = HTTPConnection("openapi.hira.or.kr")
        conn.request("GET",
                     "/openapi/service/hospInfoService/getHospBasisList?" + sidoName + "numOfRows=100&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
        req = conn.getresponse()
        print(req.status, req.reason)
        HospitalDoc = req
        Neardata = []

        tree = ElementTree.fromstring(HospitalDoc.read().decode('utf-8'))
        itemElements = tree.getiterator("item")  # return list type
        count = 0
        data = hospi
        for item in itemElements:
                yadmname = item.find("yadmNm").text
                addrname = item.find("addr").text
                clname = item.find("clCdNm").text
                if item.find("XPos") != None:
                    xpos = item.find("XPos").text
                else:
                    xpos = None
                if item.find("YPos") != None:
                    ypos = item.find("YPos").text
                else:
                    ypos = None
                if item.find("telno") != None:
                    telno = item.find("telno").text
                else:
                    telno = None
                if item.find("hospUrl") != None:
                    url = item.find("hospUrl").text
                else:
                    url = None
                data = hospi(yadmname, addrname, clname, xpos, ypos, telno, url)
                count += 1
                Neardata.append(data)
        samplenum=0
        for nana in range(count):
            if Neardata[nana].xpos != None and Neardata[nana].ypos != None:
                if float(finaldata.xpos) - 0.05 < float(Neardata[nana].xpos) and float(finaldata.xpos) + 0.05 > float(
                    Neardata[nana].xpos) and float(finaldata.ypos) - 0.05 < float(Neardata[nana].ypos) and float(
                    finaldata.ypos) + 0.05 > float(Neardata[nana].ypos):
                    samplenum+=1
        self.ui.tableWidget.setRowCount(samplenum)

        rownum = 0
        m_neardata=[]
        for nana in range(count):
            print(Neardata[nana].yadm,Neardata[nana].addr,Neardata[nana].xpos,Neardata[nana].ypos)
            if Neardata[nana].xpos!=None and Neardata[nana].ypos!=None:
                if float(finaldata.xpos) - 0.05 < float(Neardata[nana].xpos) and float(finaldata.xpos) + 0.05 > float(Neardata[nana].xpos) and float(finaldata.ypos) - 0.05 < float(Neardata[nana].ypos) and float(finaldata.ypos) + 0.05 > float(Neardata[nana].ypos):
                    self.ui.tableWidget.setItem(rownum, 0, QtGui.QTableWidgetItem(Neardata[nana].yadm))
                    self.ui.tableWidget.setItem(rownum, 1, QtGui.QTableWidgetItem(Neardata[nana].addr))
                    self.ui.tableWidget.setItem(rownum, 2, QtGui.QTableWidgetItem(Neardata[nana].url))
                    self.ui.tableWidget.setItem(rownum, 3, QtGui.QTableWidgetItem(Neardata[nana].telno))
                    m_neardata.append(Neardata[nana])
                    rownum += 1
    def slot1_click(self):
        global finaldata, Hdata,m_neardata
        finaldata = m_neardata[self.ui.tableWidget.currentRow()]
        print(self.ui.tableWidget.currentRow())
        print(finaldata)
        self.MyForm = MyForm()
        self.MyForm.show()
        self.close()

    def slot2_click(self):
        self.MyForm = MyForm()
        self.MyForm.show()
        self.close()









class SearchForm(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        global Code,sidoName,conn,HospitalDoc,sggunumber,ssgname
        Code = {'서울': '110000', '부산': '210000', '인천': '220000'
            , '대구': '230000', '경남': '380000', '경기': '310000',
                '충남': '340000', '강원': '320000', '전북': '350000', '광주': '240000'
            , '충북': '330000', '울산': '260000', '전남': '360000', '대전': '250000'
            , '경북': '370000', '제주': '390000', '세종시': '410000'}

        self.ui = search.Ui_mainWindow()
        self.ui.setupUi(self)
        print(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        ####################시이름받기
        sido = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        sidoName = "sidoCd=" + Code[sido] + "&"  # 읽어올 파일경로를 입력 받습니다.

        self.sidohttp()
        tree = ElementTree.fromstring(HospitalDoc.read().decode('utf-8'))
        # Book 엘리먼트를 가져옵니다.
        itemElements = tree.getiterator("item")  # return list type
        sggulist = []
        sggunumber = 0
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
        self.sidohttp()
        samplenumber=0
        for i in sggulist:
            self.ui.comboBox_2.addItem(_fromUtf8(""))
            self.ui.comboBox_2.setItemText(samplenumber, _translate("mainWindow", i, None))
            samplenumber+=1

        self.ui.comboBox.currentIndexChanged.connect(self.selectionchange)
        ssgname = self.ui.comboBox_2.currentText()
        self.ui.comboBox_2.currentIndexChanged.connect(self.changessgname)
        for i in range(10):
            for j in range(4):
                self.ui.tableWidget.setItem(i, j, QtGui.QTableWidgetItem("-"))
        print(ssgname)


    def changessgname(self):
        global ssgname
        ssgname = self.ui.comboBox_2.currentText()
        print(ssgname)



    def access(self):
        global Code,sidoName,conn,HospitalDoc,sggunumber,hospitalname,ssgname,Hdata,m_count
        hospitalname="yadmNm=" + quote(self.ui.lineEdit.text()) + "&"
        print("/openapi/service/hospInfoService/getHospBasisList?" + sidoName + hospitalname + "numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
        conn = HTTPConnection("openapi.hira.or.kr")
        if sidoName != None:
            conn.request("GET",
                         "/openapi/service/hospInfoService/getHospBasisList?" + sidoName + hospitalname + "numOfRows=1000&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
            req = conn.getresponse()
            print(req.status, req.reason)
            HospitalDoc = req
            tree = ElementTree.fromstring(req.read().decode('utf-8'))
            # Book 엘리먼트를 가져옵니다.
            itemElements = tree.getiterator("item")  # return list type
            samplenum=0
            Hdata=[]
            for i in range(m_count):
                self.ui.tableWidget.removeRow(i)
            m_count=0
            for item in itemElements:
                sgguNmTitle = item.find("sgguCdNm")
                if sgguNmTitle.text == ssgname:
                    yadmname = item.find("yadmNm").text
                    addrname = item.find("addr").text
                    clname = item.find("clCdNm").text
                    if item.find("XPos")!=None:
                        xpos = item.find("XPos").text
                    else:
                        xpos=None
                    if item.find("YPos")!=None:
                        ypos = item.find("YPos").text
                    else:
                        ypos=None
                    if item.find("telno")!=None:
                        telno = item.find("telno").text
                    else:
                        telno=None
                    if item.find("hospUrl")!=None:
                        url = item.find("hospUrl").text
                    else :
                        url=None
                    data = hospi(yadmname, addrname, clname, xpos, ypos, telno,url)
                    m_count += 1
                    Hdata.append(data)
            self.ui.tableWidget.setRowCount(m_count)
            for item in range(m_count):
                self.ui.tableWidget.setItem(samplenum, 0, QtGui.QTableWidgetItem(Hdata[item].yadm))
                self.ui.tableWidget.setItem(samplenum, 1, QtGui.QTableWidgetItem(Hdata[item].addr))
                self.ui.tableWidget.setItem(samplenum, 2, QtGui.QTableWidgetItem(Hdata[item].url))
                self.ui.tableWidget.setItem(samplenum, 3, QtGui.QTableWidgetItem(Hdata[item].telno))
                self.ui.tableWidget.setItem(samplenum, 4, QtGui.QTableWidgetItem(Hdata[item].cl))

                samplenum += 1



            return None
        else:
            print("시에대한 정보가 없습니다.")
        print(self.ui.tableWidget.currentRow())


    def back(self):
        global finaldata,Hdata
        finaldata=Hdata[self.ui.tableWidget.currentRow()]
        print(self.ui.tableWidget.currentRow())
        print(finaldata)
        self.MyForm = MyForm()
        self.MyForm.show()
        self.close()



    def sidohttp(self):
        global  coon,HospitalDoc,sidoName
        conn = HTTPConnection("openapi.hira.or.kr")
        conn.request("GET",
                     "/openapi/service/hospInfoService/getHospBasisList?" + sidoName + "numOfRows=100&ServiceKey=Id4vjBVQEtf9S3cDoQcUnmSSidJLPlzQIflfPq2Nr2n6CTK5OBvtYqDU3T0skasLZybrxivIfIXiNXRs1%2Bhdlg%3D%3D")
        req = conn.getresponse()
        print(req.status, req.reason)
        HospitalDoc = req

    def selectionchange(self):
        global  conn,Hospital,Code,sidoName,sggunumber,ssgname
        #print(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        sido = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        sidoName = "sidoCd=" + Code[sido] + "&"  # 읽어올 파일경로를 입력 받습니다.
        self.sidohttp()
        tree = ElementTree.fromstring(HospitalDoc.read().decode('utf-8'))
        itemElements = tree.getiterator("item")  # return list type
        sggulist = []

        print(sggunumber)

        while self.ui.comboBox_2.itemText(0)!="":
            self.ui.comboBox_2.removeItem(0)
            #self.ui.comboBox_2.setItemText(i, _translate("mainWindow", "", None))

        sggunumber = 0

        for item in itemElements:
            check = True
            for i in range(sggunumber):
                if sggulist[i] == item.find("sgguCdNm").text:
                    check = False
            if check == True:
                sggulist.append(item.find("sgguCdNm").text)
                sggunumber += 1
        #for i in range(sggunumber):
            #if i % 10 == 0:
                #print(sggulist[i], end=" ")


        print("")
        print("-----------------------------------------")
        self.sidohttp()
       # Hospital = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        samplenumber = 0
        print(sggunumber)
        for i in range(sggunumber):
            self.ui.comboBox_2.addItem(_fromUtf8(sggulist[i]))
            #self.ui.comboBox_2.setItemText(samplenumber, _translate("mainWindow", sggulist[i], None))
            samplenumber += 1

        self.changessgname()



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec_()