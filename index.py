from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys

import MySQLdb

from PyQt5.uic import loadUiType


ui , _ = loadUiType('library.ui')

class MainApp(QMainWindow , ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handel_UI_Changes()
        self.Handel_Buttons()

    
    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)
        
    
    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_21.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Today_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_15.clicked.connect(self.Add_Category)
        self.pushButton_16.clicked.connect(self.Add_Author)
        self.pushButton_17.clicked.connect(self.Add_Publisher)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()


###################### OPENING TABS ####################################

    def Open_Today_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Users_tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(3)





###################### CONNECT db ####################################

############ Book ##############

    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.CurrentText()
        book_author = self.comboBox_4.CurrentText()
        book_publisher = self.comboBox_5.CurrentText()
        book_price = self.lineEdit_4.text()







    def Search_Books(self):
        pass

    def Edit_Books(self):
        pass

    def Delete_Books(self):
        pass



############ Users ##############

    def Add_New_User(self):
        pass

    def Login(self):
        pass

    def Edit_User(self):
        pass


############ SETTINGS ##############

    def Add_Category(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_22.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')



    def Add_Author(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_23.text()

        self.cur.execute('''
            INSERT INTO author (author_name) VALUES (%s)
        ''' , (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')



    def Add_Publisher(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_24.text()

        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''' , (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')





def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

