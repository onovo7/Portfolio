from csv import DictReader, DictWriter
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import QApplication, QPushButton, QFileDialog, QVBoxLayout, QMessageBox
import sys, os
from analysis import Analysis

class Actions(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Email_Checker.ui', self)
        self.actionClose.triggered.connect(self.close)
        self.emailsforcheck = None
        self.comparewith = None
        self.list_duplicates = None
        self.list_unique = None
        self.show()
        self.pushButtons()

    def pushButtons(self):
        self.pushButton_emails_for_check.clicked.connect(self.emails_for_check)
        self.pushButton_compare_with.clicked.connect(self.compare_with)
        self.pushButton_seek_for_duplicates.clicked.connect(self.seek_for_duplicates)
        self.pushButton_download_duplicates.clicked.connect(self.download_duplicates)
        self.pushButton_download_unique.clicked.connect(self.download_unique)
        
    def emails_for_check(self):
        self.emailsforcheck, _ = QFileDialog.getOpenFileName(self, "Open File", "", ";; Csv File (*.csv)")
        self.lineEdit_file_name_emails_for_check.setText(self.emailsforcheck.split('/')[-1])

    def compare_with(self):
        self.comparewith, _ = QFileDialog.getOpenFileName(self, "Open File", "", ";; Csv File (*.csv)")
        self.lineEdit_file_name_compare_with.setText(self.comparewith.split('/')[-1])

    def seek_for_duplicates(self):
        self.activate_analysis = Analysis(emailsforcheck=self.emailsforcheck, comparewith=self.comparewith)
        if self.emailsforcheck and self.comparewith:
            self.activate_analysis.read_files()
#duplicates:
            self.list_duplicates = self.activate_analysis.list_duplicates()
            number_of_duplicates = len(self.list_duplicates)
            self.lineEdit_duplicates.setText(f'duplicates: {str(number_of_duplicates)}') 
            self.plainTextEdit_duplicate_emails.setText('\n'.join(self.list_duplicates))      
            self.plainTextEdit_unique_emails.setText('\n'.join(self.list_unique))      
#unique:
            self.list_unique = self.activate_analysis.list_unique()
            number_of_unique = len(self.list_unique)
            self.lineEdit_unique.setText(f'unique: {str(number_of_unique)}')
        else:
            if not self.emailsforcheck and not self.comparewith:
                self.error("Missing CSV files for analysis!")
                print('lists for check are missing')
            elif not self.emailsforcheck:
                self.error("Emails for check list is missing!")               
                print('emails for check list is missing')
            elif not self.comparewith:
                self.error("Compare with list is missing!")
                print('compare with list is missing')
        pass

    def download_duplicates(self):
        if self.list_duplicates and self.list_unique:
            self.path_duplicates, _ = QFileDialog.getSaveFileName(self, "Duplicate List", "", ";; Csv File (*.csv)")
            if self.path_duplicates:
                with open(self.path_duplicates, mode='w', encoding='utf-8') as file:
                    duplicates = '\n'.join(self.list_duplicates)
                    file.write('Email\n')
                    file.write(duplicates)
        else:
            self.error("No duplicates were searched for!")

    def download_unique(self):
        if self.list_duplicates and self.list_unique:
            self.path_unique, _ = QFileDialog.getSaveFileName(self, "Unique List", "", ";; Csv File (*.csv)")
            if self.path_unique:
                with open(self.path_unique, mode='w', encoding='utf-8') as file:
                    unique = '\n'.join(self.list_unique)
                    file.write('Email\n')
                    file.write(unique)
        else:
            self.error("No duplicates were searched for!")

    def error(self, message):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setText(message)
        msg.setWindowTitle("Critical MessageBox")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Cancel)
        retval = msg.exec()

    def close(self):
        sys.exit(0)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    activate_actions = Actions()
    sys.exit(app.exec())