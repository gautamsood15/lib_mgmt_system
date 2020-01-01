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
        self.Ubuntu_Theme()

        self.Show_Category()
        self.Show_Author()
        self.Show_Publisher()

        self.Show_Category_Combo()
        self.Show_Author_Combo()
        self.Show_Publisher_Combo()

        self.Show_All_Clients()
        self.Show_All_Books()
    
    def Handel_UI_Changes(self):
        self.Hiding_Themes()
        self.tabWidget.tabBar().setVisible(False)
        
    
    def Handel_Buttons(self):
        self.pushButton_5.clicked.connect(self.Show_Themes)
        self.pushButton_26.clicked.connect(self.Hiding_Themes)

        self.pushButton.clicked.connect(self.Open_Today_Tab)
        self.pushButton_2.clicked.connect(self.Open_Books_Tab)
        self.pushButton_27.clicked.connect(self.Open_Clients_Tab)
        self.pushButton_3.clicked.connect(self.Open_Users_tab)
        self.pushButton_4.clicked.connect(self.Open_Settings_Tab)

        self.pushButton_7.clicked.connect(self.Add_New_Book)

        self.pushButton_15.clicked.connect(self.Add_Category)
        self.pushButton_16.clicked.connect(self.Add_Author)
        self.pushButton_17.clicked.connect(self.Add_Publisher)

        self.pushButton_10.clicked.connect(self.Search_Books)
        self.pushButton_9.clicked.connect(self.Edit_Books)
        self.pushButton_11.clicked.connect(self.Delete_Books)

        self.pushButton_12.clicked.connect(self.Add_New_User)
        self.pushButton_13.clicked.connect(self.Login)
        self.pushButton_14.clicked.connect(self.Edit_User)

        self.pushButton_23.clicked.connect(self.Aqua_Theme)
        self.pushButton_22.clicked.connect(self.Ubuntu_Theme)
        self.pushButton_25.clicked.connect(self.ElegantDark_Theme)
        self.pushButton_24.clicked.connect(self.MaterialDark_Theme)
        self.pushButton_8.clicked.connect(self.Default_Theme)

        self.pushButton_18.clicked.connect(self.Add_New_Client)
        self.pushButton_20.clicked.connect(self.Search_Client)
        self.pushButton_21.clicked.connect(self.Delete_Client)
        self.pushButton_19.clicked.connect(self.Edit_Client)

    def Show_Themes(self):
        self.groupBox_3.show()

    def Hiding_Themes(self):
        self.groupBox_3.hide()


###################### OPENING TABS ####################################

    def Open_Today_Tab(self):
        self.tabWidget.setCurrentIndex(0)

    def Open_Books_Tab(self):
        self.tabWidget.setCurrentIndex(1)

    def Open_Clients_Tab(self):
        self.tabWidget.setCurrentIndex(2)

    def Open_Users_tab(self):
        self.tabWidget.setCurrentIndex(3)

    def Open_Settings_Tab(self):
        self.tabWidget.setCurrentIndex(4)






########################################## BOOK ###############################################

    def Show_All_Books(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT book_name,book_description,book_code,book_category,book_author,book_publisher,book_price FROM book''')
        data = self.cur.fetchall()

        self.tableWidget_6.insertRow(0)

        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_6.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_6.rowCount()
            self.tableWidget_6.insertRow(row_position)

        self.db.close()



    def Add_New_Book(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_2.text()
        book_description = self.textEdit.toPlainText()
        book_code = self.lineEdit_3.text()
        book_category = self.comboBox_3.currentText()
        book_author = self.comboBox_4.currentText()
        book_publisher = self.comboBox_5.currentText()
        book_price = self.lineEdit_4.text()

        self.cur.execute('''
            INSERT INTO book(book_name,book_description,book_code,book_category,book_author,book_publisher,book_price)
            VALUES (%s , %s , %s , %s , %s , %s ,%s)
        ''' ,(book_title , book_description , book_code , book_category , book_author , book_publisher , book_price))

        self.db.commit()
        self.statusBar().showMessage('New Book Added')

        self.lineEdit_2.setText('')
        self.textEdit.setPlainText('')
        self.lineEdit_3.setText('')
        self.comboBox_3.setCurrentIndex(0)
        self.comboBox_4.setCurrentIndex(0)
        self.comboBox_5.setCurrentIndex(0)
        self.lineEdit_4.setText('')




    def Search_Books(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_10.text()

        sql = ''' SELECT * FROM book WHERE book_name = %s'''
        self.cur.execute(sql , [(book_title)])

        data = self.cur.fetchone()


        self.lineEdit_11.setText(data[1])
        self.textEdit_2.setText(data[2])
        self.lineEdit_8.setText(data[3])
        self.comboBox_9.setCurrentIndex(data[4])
        self.comboBox_10.setCurrentIndex(data[5])
        self.comboBox_11.setCurrentIndex(data[6])
        self.lineEdit_9.setText(str(data[7]))


    def Edit_Books(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_11.text()
        book_description = self.textEdit_2.toPlainText()
        book_code = self.lineEdit_8.text()
        book_category = self.comboBox_9.currentIndex()
        book_author = self.comboBox_10.currentIndex()
        book_publisher = self.comboBox_11.currentIndex()
        book_price = self.lineEdit_9.text()

        search_book_title = self.lineEdit_10.text()

        self.cur.execute('''
            UPDATE book SET book_name=%s,book_description=%s,book_code=%s,book_category=%s,book_author=%s,book_publisher=%s,book_price=%s WHERE book_name = %s
        ''', (book_title , book_description , book_code , book_category , book_author , book_publisher , book_price , search_book_title))

        self.db.commit()
        self.statusBar().showMessage('Book Updated Sucessfully')





    def Delete_Books(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        book_title = self.lineEdit_10.text()

        warning = QMessageBox.warning(self , 'Delete Book' , "Are you sure you want to delete this Book" , QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM book WHERE book_name = %s'''
            self.cur.execute(sql , [(book_title)])
            self.db.commit()
            self.statusBar().showMessage('Book Deleted')

        else :
            pass   # meaning do nothing




####################################### CLIENTS ###################################################


    def Add_New_Client(self):
        client_name = self.lineEdit_5.text()
        client_email = self.lineEdit_6.text()
        client_aadharID = self.lineEdit_7.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute('''
            INSERT INTO clients(client_name , client_email , client_aadhar_id)
            VALUES (%s , %s , %s)
        ''' , (client_name , client_email , client_aadharID))

        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('New Client Added')

        self.lineEdit_5.setText('')
        self.lineEdit_6.setText('')
        self.lineEdit_7.setText('')



    def Show_All_Clients(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT client_name , client_email , client_aadhar_id FROM clients''')
        data = self.cur.fetchall()

        self.tableWidget_5.insertRow(0)

        for row , form in enumerate(data):
            for column , item in enumerate(form):
                self.tableWidget_5.setItem(row , column , QTableWidgetItem(str(item)))
                column += 1
            row_position = self.tableWidget_5.rowCount()
            self.tableWidget_5.insertRow(row_position)

        self.db.close()



    def Search_Client(self):
        client_aadharID = self.lineEdit_27.text()

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        sql = ''' SELECT * FROM clients WHERE client_aadhar_ID = %s '''
        self.cur.execute(sql , [(client_aadharID)])

        data = self.cur.fetchone()

        self.lineEdit_28.setText(data[1])
        self.lineEdit_29.setText(data[2])
        self.lineEdit_30.setText(data[3])

        self.db.commit()
        self.db.close()


    def Edit_Client(self):
        client_original_aadharID = self.lineEdit_27.text()
        client_name = self.lineEdit_28.text()
        client_email = self.lineEdit_28.text()
        client_aadharID = self.lineEdit_30.text()
        
        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()
        
        self.cur.execute('''
            UPDATE clients SET client_name = %s , client_email = %s , client_aadhar_id = %s WHERE client_aadhar_id = %s
        ''' , (client_name , client_email , client_aadharID , client_original_aadharID))

        self.db.commit()
        self.db.close()
        self.statusBar().showMessage('Client Details Updated')

        self.lineEdit_27.setText('')
        self.lineEdit_28.setText('')
        self.lineEdit_29.setText('')
        self.lineEdit_30.setText('')



    def Delete_Client(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        client_aadhar = self.lineEdit_27.text()

        warning = QMessageBox.warning(self , 'Delete Client' , "Are you sure you want to delete this Client" , QMessageBox.Yes | QMessageBox.No)

        if warning == QMessageBox.Yes :
            sql = ''' DELETE FROM clients WHERE client_aadhar_id = %s'''
            self.cur.execute(sql , [(client_aadhar)])
            self.db.commit()
            self.statusBar().showMessage('Client Deleted')

            self.lineEdit_27.setText('')
            self.lineEdit_28.setText('')
            self.lineEdit_29.setText('')
            self.lineEdit_30.setText('')

        else :
            pass   # meaning do nothing





####################################### USERS ###################################################



    def Add_New_User(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        username = self.lineEdit_12.text()
        email = self.lineEdit_13.text()
        password = self.lineEdit_14.text()
        password2 = self.lineEdit_15.text()

        if password == password2 :
            self.cur.execute('''
                INSERT INTO users(user_name , user_email , user_password) 
                VALUES (%s , %s , %s)
            ''', (username , email, password))

            self.db.commit()
            self.statusBar().showMessage('New User Added')

        else:
            self.label_9.setText('Ensure that both passwords match !!')



    def Login(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        username = self.lineEdit_16.text()
        password = self.lineEdit_17.text()

        sql = ''' SELECT * FROM users'''

        self.cur.execute(sql)
        data = self.cur.fetchall()
        for row in data :
            if username == row[1] and password == row[3]:
                print('User Match')
                self.statusBar().showMessage('Valid Username & Password')
                self.groupBox_4.setEnabled(True)

                self.lineEdit_18.setText(row[1])
                self.lineEdit_20.setText(row[2])
                self.lineEdit_19.setText(row[3])



    def Edit_User(self):

        original_name = self.lineEdit_16.text()

        username = self.lineEdit_18.text()
        email = self.lineEdit_20.text()
        password = self.lineEdit_19.text()
        password2 = self.lineEdit_21.text()

        if password == password2 :
            self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
            self.cur = self.db.cursor()

            self.cur.execute('''
                UPDATE users SET user_name = %s , user_email = %s , user_password = %s WHERE user_name = %s
            ''', (username , email , password , original_name))

            self.db.commit()
            self.statusBar().showMessage('User Data Updated Successfully')

            self.lineEdit_16.setText('')
            self.lineEdit_17.setText('')
            self.groupBox_4.setEnabled(False)
            self.lineEdit_18.setText('')
            self.lineEdit_20.setText('')
            self.lineEdit_19.setText('')
            self.lineEdit_21.setText('')

        else:
            print('Make sure you entered your password correctly')





########################################## SETTINGS ##################################################

    def Add_Category(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        category_name = self.lineEdit_22.text()

        self.cur.execute('''
            INSERT INTO category (category_name) VALUES (%s)
        ''' , (category_name,))

        self.db.commit()
        self.statusBar().showMessage('New Category Added')
        self.lineEdit_22.setText('')
        self.Show_Category()
        self.Show_Category_Combo()

    def Show_Category(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        self.cur.execute( ''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_2.setRowCount(0)
            self.tableWidget_2.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_2.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_2.rowCount()
                self.tableWidget_2.insertRow(row_position)






    def Add_Author(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        author_name = self.lineEdit_23.text()

        self.cur.execute('''
            INSERT INTO author (author_name) VALUES (%s)
        ''' , (author_name,))

        self.db.commit()
        self.statusBar().showMessage('New Author Added')
        self.lineEdit_23.setText('')
        self.Show_Author()
        self.Show_Author_Combo()


    def Show_Author(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        self.cur.execute( ''' SELECT author_name FROM author ''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_3.setRowCount(0)
            self.tableWidget_3.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_3.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_3.rowCount()
                self.tableWidget_3.insertRow(row_position)






    def Add_Publisher(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        publisher_name = self.lineEdit_24.text()

        self.cur.execute('''
            INSERT INTO publisher (publisher_name) VALUES (%s)
        ''' , (publisher_name,))

        self.db.commit()
        self.statusBar().showMessage('New Publisher Added')
        self.lineEdit_24.setText('')
        self.Show_Publisher()
        self.Show_Publisher_Combo()



    def Show_Publisher(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        self.cur.execute( ''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        if data :
            self.tableWidget_4.setRowCount(0)
            self.tableWidget_4.insertRow(0)
            for row , form in enumerate(data):
                for column , item in enumerate(form):
                    self.tableWidget_4.setItem(row , column , QTableWidgetItem(str(item)))
                    column += 1

                row_position = self.tableWidget_4.rowCount()
                self.tableWidget_4.insertRow(row_position)





########################### SHOW SETTINGS DATA IN UI #####################################

    def Show_Category_Combo(self):

        self.db = MySQLdb.connect(host='localhost' , user='root' , password='root@123' , db='library')
        self.cur = self.db.cursor()

        self.cur.execute( ''' SELECT category_name FROM category ''')
        data = self.cur.fetchall()

        self.comboBox_3.clear()

        self.comboBox_3.addItem('SELECT A CATEGORY')
        self.comboBox_9.addItem('SELECT A CATEGORY')
        for category in data :
            self.comboBox_3.addItem(category[0])
            self.comboBox_9.addItem(category[0])



    def Show_Author_Combo(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT author_name FROM author ''')
        data = self.cur.fetchall()

        self.comboBox_4.clear()

        self.comboBox_4.addItem('SELECT AN AUTHOR')
        self.comboBox_10.addItem('SELECT AN AUTHOR')
        for auth in data:
            self.comboBox_4.addItem(auth[0])
            self.comboBox_10.addItem(auth[0])





    def Show_Publisher_Combo(self):

        self.db = MySQLdb.connect(host='localhost', user='root', password='root@123', db='library')
        self.cur = self.db.cursor()

        self.cur.execute(''' SELECT publisher_name FROM publisher ''')
        data = self.cur.fetchall()

        self.comboBox_5.clear()

        self.comboBox_5.addItem('SELECT A PUBLISHER')
        self.comboBox_11.addItem('SELECT A PUBLISHER')
        for pub in data:
            self.comboBox_5.addItem(pub[0])
            self.comboBox_11.addItem(pub[0])





########################### UI THEMES #####################################


    def Ubuntu_Theme(self):
        style = open('themes/ubuntu.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Aqua_Theme(self):
        style = open('themes/aqua.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def ElegantDark_Theme(self):
        style = open('themes/elegantdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def MaterialDark_Theme(self):
        style = open('themes/materialdark.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)

    def Default_Theme(self):
        style = open('themes/default.css' , 'r')
        style = style.read()
        self.setStyleSheet(style)










########################################################################################################################

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

