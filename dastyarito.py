# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dastyarito.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import requests
from bs4 import BeautifulSoup

dollar_var = ""


class Ui_MainWindow(object):
            
                
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 801, 571))
        self.tabWidget.setObjectName("tabWidget")
        self.tabs = QtWidgets.QWidget()
        self.tabs.setObjectName("tabs")
        self.textBrowser = QtWidgets.QTextBrowser(self.tabs)
        self.textBrowser.setGeometry(QtCore.QRect(0, 150, 421, 401))
        self.textBrowser.setObjectName("textBrowser")
        self.line = QtWidgets.QFrame(self.tabs)
        self.line.setGeometry(QtCore.QRect(410, -10, 20, 561))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.tabs)
        self.label_3.setGeometry(QtCore.QRect(80, 30, 251, 91))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.tabs)
        self.label_5.setGeometry(QtCore.QRect(490, 50, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tabs)
        self.textBrowser_2.setGeometry(QtCore.QRect(420, 150, 381, 401))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.tabWidget.addTab(self.tabs, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.label = QtWidgets.QLabel(self.tab_2)
        self.label.setGeometry(QtCore.QRect(300, 30, 191, 61))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.tab_2)
        self.label_2.setGeometry(QtCore.QRect(370, 160, 201, 51))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(90, 170, 281, 31))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.tab_2)
        self.pushButton.setGeometry(QtCore.QRect(330, 330, 131, 31))
        self.pushButton.setObjectName("pushButton")
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        self.pushButton.clicked.connect(self.dollar)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        
    def dollar() :
        url = 'http://www.tgju.org/dollar-chart'
        session = requests.session()
        site = session.get(url)
        soup = BeautifulSoup(site.text, 'html.parser')
        for sitedata in soup.find_all('td', class_='nf') :
            return sitedata.string
            update()
                
        
            

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "دستیاریتو"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Ubuntu\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Sans Serif\'; font-size:9pt;\">سلام این پروژه یک پروژه متن باز هست ممنون میشم که توی توسعه پروژه کمک کنید و توی گیت هاب به پروژه کامیت کنید هدف از این پروژه این هست که بیشتر برنامه هایی که ایرانی ها نوشتن  برای راحتی کاربران  و توی گیت هاب منتشر کردن رو یکم دیباگ کنیم و بهترشون کنیم و داخل این برنامه بیاریم تا مردم برای استفاده همه رو یک جا داشته باشند و برنامه هایی که استفاده می کنند بدون باگ باشه</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "برای توسعه دهنده ها"))
        self.label_5.setText(_translate("MainWindow", "برای کاربران"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabs), _translate("MainWindow", "توضیحات"))
        self.label.setText(_translate("MainWindow", "قیمت ارز"))
        self.label_2.setText(_translate("MainWindow", "قیمت دلار : "))
        self.label_4.setText(_translate("MainWindow", dollar_strval))
        self.pushButton.setText(_translate("MainWindow", "به روز رسانی"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "قیمت ارز"))


            
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())