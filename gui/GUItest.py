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
from http.client import HTTPConnection
from urllib.parse   import quote
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from hospital import Hospihal as hospi
from xml.etree import ElementTree


##### global
BooksDoc = None
sidoName=None
sgguName=None
Hname=None
Hdata = []
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
       # self.show(self)

    def slot1_click(self):
         self.search=SearchForm()
         self.search.show()
         self.close()
         return

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
                    yadmname = item.find("yadmNm")
                    addrname = item.find("addr")
                    clname = item.find("clCdNm")
                    xpos = item.find("XPos")
                    ypos = item.find("YPos")
                    telno = item.find("telno")
                    if clname == None or yadmname == None or addrname == None or xpos == None or ypos == None or telno==None:
                        print("못찾음")
                    else:
                        data = hospi(yadmname.text, addrname.text, clname.text, xpos.text, ypos.text, telno.text)
                        m_count += 1
                        Hdata.append(data)
            self.ui.tableWidget.setRowCount(m_count)
            for item in range(m_count):
                self.ui.tableWidget.setItem(samplenum, 0, QtGui.QTableWidgetItem(Hdata[item].yadm))
                self.ui.tableWidget.setItem(samplenum, 1, QtGui.QTableWidgetItem(Hdata[item].addr))
                self.ui.tableWidget.setItem(samplenum, 2, QtGui.QTableWidgetItem(Hdata[item].xpos))
                self.ui.tableWidget.setItem(samplenum, 3, QtGui.QTableWidgetItem(Hdata[item].ypos))
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
        print(self.ui.comboBox.itemText(self.ui.comboBox.currentIndex()))
        sido = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())
        sidoName = "sidoCd=" + Code[sido] + "&"  # 읽어올 파일경로를 입력 받습니다.
        self.sidohttp()
        tree = ElementTree.fromstring(HospitalDoc.read().decode('utf-8'))
        itemElements = tree.getiterator("item")  # return list type
        sggulist = []
        for i in range(sggunumber):
            self.ui.comboBox_2.removeItem(i)
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
        for i in range(sggunumber):
            if i % 10 == 0:
                print()
            print(sggulist[i], end=" ")
        print("")
        print("-----------------------------------------")
        self.sidohttp()
       # Hospital = self.ui.comboBox.itemText(self.ui.comboBox.currentIndex())

        samplenumber = 0
        for i in sggulist:
            if samplenumber>sggunumber:
                self.ui.comboBox_2.addItem(_fromUtf8(""))
            self.ui.comboBox_2.setItemText(samplenumber, _translate("mainWindow", i, None))
            samplenumber += 1
        self.changessgname()



if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    app.exec_()