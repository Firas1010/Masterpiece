from PyQt5 import QtCore, QtGui, QtWidgets
from FINTER import Ui_Inter
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QMessageBox
import pandas as pd
from datetime import datetime
import os



class Ui_LogM(object):
    def __init__(self):
        self.window = None  # Store the reference to the choix window
        self.login_window = None  # Store the reference to the login window 
        
    def HID(self):
        LogM.close()  
        
        
    def Openchoix(self):
        Matricule = self.lineEdit.text().strip()  # Remove leading/trailing spaces

        try:
            file_Matricule = "Traçabilité.xlsx"

            # Get the current date and time
            current_time = datetime.now().strftime("%H:%M:%S")
            current_date = datetime.now().strftime("%d-%m-%Y")

            # Check if the result file already exists
            if os.path.isfile(file_Matricule):
                # Read the existing result file
                existing_data = pd.read_excel(file_Matricule)

                # Create a DataFrame with the new entry
                new_entry = pd.DataFrame({'Matricule': [Matricule], 'Time': [current_time], 'Date': [current_date]})

                # Concatenate the existing data and the new entry
                updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

                # Save the updated data to the result file
                updated_data.to_excel(file_Matricule, index=False, engine='openpyxl')
                print("Matricule added to the result file successfully.")
            else:
                # Create a new result file with the new entry
                data = pd.DataFrame({'Matricule': [Matricule], 'Time': [current_time], 'Date': [current_date]})

                # Save the new entry DataFrame to the result file
                data.to_excel(file_Matricule, index=False, engine='openpyxl')
                print("Matricule added to the result file successfully.")
            
            
            
            database = pd.read_excel(r"Matricule.xlsx",sheet_name="Maintenance")
            print(database)
            print(Matricule)
            DB = database['Matricule'].astype(str).str.strip().tolist()  # Convert to string and remove leading/trailing spaces
            print(DB)
            
            if Matricule.lower() in [x.lower() for x in DB]:  # Case-insensitive comparison
                print(Matricule)
                self.window = QtWidgets.QMainWindow()
                self.ui = Ui_Inter()
                self.ui.setupUi(self.window)
                self.window.show()
                # self.login_window.hide()  # Hide the login window  
                self.login_window.hide() 
                
                
                
            else:
                msg = QMessageBox()
                msg.setWindowTitle('Erreur')
                msg.setText("Mot de passe incorrect.\nVeuillez saisir à nouveau le mot de passe.")
                msg.setIcon(QMessageBox.Warning)
                x = msg.exec_()
        except FileNotFoundError:
            print("Error: Database file not found.")
            exit()

   
                       
   

    def setupUi(self, MainWindow):
        self.login_window = MainWindow  # Store the reference to the login window
       
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(391, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 391, 601))
        self.label.setStyleSheet("background-color: #F1F2F6;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 30, 361, 141))
        self.label_2.setStyleSheet("color: #0056D2; font-size: 18pt; font-weight: 600;")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(80, 300, 251, 51))
        self.lineEdit.setObjectName("lineEdit")

        # Set the font size
        font = QtGui.QFont()
        font.setPointSize(18)
        self.lineEdit.setFont(font)

        # Synchronize font size with widget size
        self.lineEdit.setStyleSheet('''
            QLineEdit {
                border: 2px solid gray;
                border-radius: 10px;
                padding: 5px;
                font-size: 18px;
            }
            QLineEdit:focus {
                border: 2px solid #0095F6;
            }
            QLineEdit::hover {
                border: 2px solid #B2B2B2;
            }
        ''')

        # Only allow integer input
        validator = QtGui.QIntValidator()
        self.lineEdit.setValidator(validator)

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 270, 101, 36))
        self.label_3.setStyleSheet("color: #80BFFF; font-size: 16pt; font-weight: 75;")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 480, 391, 121))
        self.label_4.setStyleSheet("border-image: url(:/loggg/ak.jpg);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.Id = QtWidgets.QPushButton(self.centralwidget)
        self.Id.setGeometry(QtCore.QRect(180, 380, 141, 41))
        self.Id.setStyleSheet("background-color: #0056D2; color: #FFFFFF; font-weight: 600; border-radius: 5px;")
        self.Id.setObjectName("Id")

        self.Id.clicked.connect(self.Openchoix)
        # self.Closet = QtWidgets.QPushButton(self.centralwidget)
        # self.Closet.setGeometry(QtCore.QRect(365, 0, 25, 25))
        # self.Closet.setStyleSheet("border-image: url(:/loggg/cancel.png);")
        # self.Closet.setText("")
        # self.Closet.setObjectName("Closet")

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        # self.Closet.clicked.connect(self.HID) 
        

        
        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Login Technicien"))


        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\"vertical-align:super;\">Bonjour Monsieur pouvez-vous taper </span></p><p align=\"center\"><span style=\"vertical-align:super;\">votre matricule ?</span></p><p align=\"center\"><span style=\"vertical-align:super;\">"))
        self.label_3.setText(_translate("MainWindow", "Matricule"))
        self.Id.setText(_translate("MainWindow", "S'identifier"))
import akwel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogM = QtWidgets.QMainWindow()
    ui = Ui_LogM()
    ui.setupUi(LogM)
    LogM.show()
    sys.exit(app.exec_())

