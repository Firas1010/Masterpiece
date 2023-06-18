from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import os 
from PyQt5.QtWidgets import QMessageBox
import datetime
class Ui_Inter(object):
    
    def __init__(self):
        self.window = None  # Store the reference to the choix window
        self.login_window = None  # Store the reference to the login window 
    
    def Save(self):
        DATE=self.dateEdit.text()
        OT=self.NOT.text()
        MT=self.TM.text()
        machine=self.MACH.text()
        Famille=self.FAM.currentText() 

        # Extracting Time Components from self.TDEBUT.text()
        HD_time = datetime.datetime.strptime(self.TDEBUT.text(), '%H:%M')
        HD = HD_time.hour*60 + HD_time.minute
        HDéb =self.TDEBUT.text()
        HFIN=self.TF.text()

        # Extracting Time Components from self.TF.text()
        HF_time =  datetime.datetime.strptime(self.TF.text(), '%H:%M')
        HF = HF_time.hour*60 + HF_time.minute
        if self.TI.text() != '':
            Tpinter = float(self.TI.text())
        else:
            Tpinter = 0.0  # or any default value you prefer

        demandeur=self.DD.text()
        equipe=self.EQ.currentText() 
        type=self.Tinter.currentText()
        res=HF-HD
        Commentaire=self.textEdit.toPlainText()
        if type=='Préventive':
            if (OT=='') or (machine =='') or (Tpinter=='') or (demandeur=='') or (Commentaire==''):
                    msg = QMessageBox()
                    msg.setWindowTitle('Erreur')
                    msg.setText("Champs Vide.\nVeuillez Remplier les champs vide.")
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
            else :        
                    print(res)
                    
                    L=[DATE,OT,machine,Famille,HD,HF,Tpinter,demandeur,equipe,type,Commentaire]
                    print(L)
                    if (OT=='') or (machine =='') or (Tpinter=='') or (demandeur==''):
                            msg = QMessageBox()
                            msg.setWindowTitle('Erreur')
                            msg.setText("Champs Vide.\nVeuillez Remplier les champs vide.")
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                    else :
                            if res== Tpinter :
                                try:
                                    def round_up_time(current_time):
                                        if current_time.minute >= 55:
                                            current_time = current_time.replace(minute=0, second=0) + datetime.timedelta(hours=1)
                                        else:
                                            current_time = current_time.replace(minute=0, second=0) + datetime.timedelta(hours=1)
                                        return current_time

                                    # Get the current time as a datetime object
                                    Tpreel = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")

                                    # Check if the Tpréel needs rounding
                                    rounded_time = round_up_time(Tpreel)
                                    rounded_time_str = rounded_time.strftime("%H:%M")


                                    print(rounded_time.strftime("%H:%M"))
                                    KNOW=datetime.datetime.now().strftime("%H:%M:%S")
                                    file = "ReportingMaintenance.xlsx"

                                    # Check if the result file already exists
                                    if os.path.isfile(file):
                                        # Read the existing result file
                                        existing_data = pd.read_excel(file)

                                        # Create a DataFrame with the new entry for maintenance
                                        maintenance_entry = pd.DataFrame({'Date': [DATE],'Temps/H de travail': [rounded_time_str], 'Technicien':[MT],'Ordre de travail': [OT], 'Machine': [machine], 'Famille': [Famille], 'Heure de début': [HDéb], 'Heure de fin': [HFIN], 'Temps dintervention en min': [Tpinter], 'Demandeur': [demandeur], 'Equipe': [equipe], 'Type dintervention': [type],'Déscription': [Commentaire],'SAVE':[KNOW]})

                                        # Concatenate the existing maintenance data and the new entry
                                        updated_maintenance_data = pd.concat([existing_data, maintenance_entry], ignore_index=True)

                                        # Save the updated maintenance data to the result file in the "Maintenance" sheet
                                        updated_maintenance_data.to_excel(file, sheet_name='Maintenance', index=False, engine='openpyxl')
                                        print("Maintenance data added to the result file successfully.")
                                        msg = QMessageBox()
                                        msg.setWindowTitle('SAVE')
                                        msg.setText("Données enregistrer.\nMaintenance data added to the file successfully.")
                                        msg.setIcon(QMessageBox.Information)
                                        x = msg.exec_()  
                                        os.system('start excel.exe "%s"' % ("Préventive.xlsx", ))
                                    else:
                                        # Create a new result file with the new entry for maintenance
                                        maintenance_data = pd.DataFrame({'Date': [DATE], 'Temps/H de travail': [rounded_time_str],'Technicien':[MT],'Ordre de travail': [OT], 'Machine': [machine], 'Famille': [Famille], 'Heure de début': [HDéb], 'Heure de fin': [HFIN], 'Temps dintervention en min': [Tpinter], 'Demandeur': [demandeur], 'Equipe': [equipe], 'Type dintervention': [type],'Déscription': [Commentaire],'SAVE':[KNOW]})

                                        # Save the new maintenance entry DataFrame to the result file in the "Maintenance" sheet
                                        maintenance_data.to_excel(file, sheet_name='Maintenance', index=False, engine='openpyxl')
                                        print("Maintenance data added to the result file successfully.")

                                        msg = QMessageBox()
                                        msg.setWindowTitle('SAVE')
                                        msg.setText("Données enregistrer.\nMaintenance data added to the file successfully.")
                                        msg.setIcon(QMessageBox.Information)
                                        x = msg.exec_()                     
                                        
                                        os.system('start excel.exe "%s"' % ("Préventive.xlsx", ))                 
                                except FileNotFoundError:
                                    print("Error: Database file not found.")
                                    exit() 
                            else :
                                    msg = QMessageBox()
                                    msg.setWindowTitle('Erreur')
                                    msg.setText("Temps d'intervention incorrect.\nVeuillez saisir à nouveau le temps réel de maitenance.")
                                    msg.setIcon(QMessageBox.Warning)
                                    x = msg.exec_()     
    
                                  
        else :    
            if (OT=='') or (machine =='') or (Tpinter=='') or (demandeur=='') or (Commentaire==''):
                    msg = QMessageBox()
                    msg.setWindowTitle('Erreur')
                    msg.setText("Champs Vide.\nVeuillez Remplier les champs vide.")
                    msg.setIcon(QMessageBox.Warning)
                    x = msg.exec_()
            else :        
                    print(res)
                    
                    L=[DATE,OT,machine,Famille,HD,HF,Tpinter,demandeur,equipe,type,Commentaire]
                    print(L)
                    if (OT=='') or (machine =='') or (Tpinter=='') or (demandeur==''):
                            msg = QMessageBox()
                            msg.setWindowTitle('Erreur')
                            msg.setText("Champs Vide.\nVeuillez Remplier les champs vide.")
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()
                    else :
                            if res== Tpinter :
                                try:
                                    def round_up_time(current_time):
                                        if current_time.minute >= 55:
                                            current_time = current_time.replace(minute=0, second=0) + datetime.timedelta(hours=1)
                                        else:
                                            current_time = current_time.replace(minute=0, second=0) + datetime.timedelta(hours=1)
                                        return current_time

                                    # Get the current time as a datetime object
                                    Tpreel = datetime.datetime.strptime(datetime.datetime.now().strftime("%H:%M:%S"), "%H:%M:%S")

                                    # Check if the Tpréel needs rounding
                                    rounded_time = round_up_time(Tpreel)
                                    rounded_time_str = rounded_time.strftime("%H:%M")


                                    print(rounded_time.strftime("%H:%M"))
                                    KNOW=datetime.datetime.now().strftime("%H:%M:%S")
                                    file = "ReportingMaintenance.xlsx"

                                    # Check if the result file already exists
                                    if os.path.isfile(file):
                                        # Read the existing result file
                                        existing_data = pd.read_excel(file)

                                        # Create a DataFrame with the new entry for maintenance
                                        maintenance_entry = pd.DataFrame({'Date': [DATE],'Temps/H de travail': [rounded_time_str], 'Technicien':[MT],'Ordre de travail': [OT], 'Machine': [machine], 'Famille': [Famille], 'Heure de début': [HDéb], 'Heure de fin': [HFIN], 'Temps dintervention en min': [Tpinter], 'Demandeur': [demandeur], 'Equipe': [equipe], 'Type dintervention': [type],'Déscription': [Commentaire],'SAVE':[KNOW]})

                                        # Concatenate the existing maintenance data and the new entry
                                        updated_maintenance_data = pd.concat([existing_data, maintenance_entry], ignore_index=True)

                                        # Save the updated maintenance data to the result file in the "Maintenance" sheet
                                        updated_maintenance_data.to_excel(file, sheet_name='Maintenance', index=False, engine='openpyxl')
                                        print("Maintenance data added to the result file successfully.")
                                        msg = QMessageBox()
                                        msg.setWindowTitle('SAVE')
                                        msg.setText("Données enregistrer.\nMaintenance data added to the file successfully.")
                                        msg.setIcon(QMessageBox.Information)
                                        x = msg.exec_()  
                                    else:
                                        # Create a new result file with the new entry for maintenance
                                        maintenance_data = pd.DataFrame({'Date': [DATE], 'Temps/H de travail': [rounded_time_str],'Technicien':[MT],'Ordre de travail': [OT], 'Machine': [machine], 'Famille': [Famille], 'Heure de début': [HDéb], 'Heure de fin': [HFIN], 'Temps dintervention en min': [Tpinter], 'Demandeur': [demandeur], 'Equipe': [equipe], 'Type dintervention': [type],'Déscription': [Commentaire],'SAVE':[KNOW]})

                                        # Save the new maintenance entry DataFrame to the result file in the "Maintenance" sheet
                                        maintenance_data.to_excel(file, sheet_name='Maintenance', index=False, engine='openpyxl')
                                        print("Maintenance data added to the result file successfully.")

                                        msg = QMessageBox()
                                        msg.setWindowTitle('SAVE')
                                        msg.setText("Données enregistrer.\nMaintenance data added to the file successfully.")
                                        msg.setIcon(QMessageBox.Information)
                                        x = msg.exec_()                     
                                        
                                        
                                except FileNotFoundError:
                                    print("Error: Database file not found.")
                                    exit()   
                                    
                            else :
                                    msg = QMessageBox()
                                    msg.setWindowTitle('Erreur')
                                    msg.setText("Temps d'intervention incorrect.\nVeuillez saisir à nouveau le temps réel de maitenance.")
                                    msg.setIcon(QMessageBox.Warning)
                                    x = msg.exec_()     
    
    def setupUi(self, Inter):

        Inter.setObjectName("Inter")
        Inter.resize(343, 890)
        self.centralwidget = QtWidgets.QWidget(Inter)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 361, 891))
        self.label.setStyleSheet("background-color: #ÚF8F6F4;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.dateEdit = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit.setGeometry(QtCore.QRect(180, 160, 121, 32))
        self.dateEdit.setObjectName("dateEdit")
        self.dateEdit.setStyleSheet('''
    QDateEdit {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 12px;
    }
    QDateEdit:focus {
        border: 2px solid #0095F6;
    }
    QDateEdit::hover {
        border: 2px solid #B2B2B2;
    }
''')
        self.dateEdit.setDate(datetime.datetime.now())
        self.TDEBUT = QtWidgets.QTimeEdit(self.centralwidget)
        self.TDEBUT.setGeometry(QtCore.QRect(180, 330, 121, 32))
        self.TDEBUT.setObjectName("TDEBUT")
        self.TDEBUT.setStyleSheet('''
    QTimeEdit {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 12px;
    }
    QTimeEdit:focus {
        border: 2px solid #0095F6;
    }
    QTimeEdit::hover {
        border: 2px solid #B2B2B2;
    }
''')
        self.TF = QtWidgets.QTimeEdit(self.centralwidget)
        self.TF.setGeometry(QtCore.QRect(180, 370, 121, 32))
        self.TF.setObjectName("TF")
        self.TF.setStyleSheet('''
    QTimeEdit {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 12px;
    }
    QTimeEdit:focus {
        border: 2px solid #0095F6;
    }
    QTimeEdit::hover {
        border: 2px solid #B2B2B2;
    }
''')
        self.MACH = QtWidgets.QLineEdit(self.centralwidget)
        self.MACH.setGeometry(QtCore.QRect(180, 240, 121, 31))
        self.MACH.setObjectName("MACH")
        self.MACH.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
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
        validator = QtGui.QIntValidator()
        self.MACH.setValidator(validator)
        self.FAM = QtWidgets.QComboBox(self.centralwidget)
        self.FAM.setGeometry(QtCore.QRect(180, 280, 121, 31))
        self.FAM.setObjectName("FAM")
        self.FAM.setStyleSheet('''
    QComboBox {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 14px;
    }
    QComboBox:focus {
        border: 2px solid #0095F6;
    }
    QComboBox::hover {
        border: 2px solid #B2B2B2;
    }
''')
        self.FAM.addItems(['PV', 'PM1','PM2','PM3', 'TET'])
        self.DD = QtWidgets.QLineEdit(self.centralwidget)
        self.DD.setGeometry(QtCore.QRect(180, 460, 121, 31))
        self.DD.setObjectName("DD")
        self.DD.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
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
        validator = QtGui.QIntValidator()
        self.DD.setValidator(validator)
        self.EQ = QtWidgets.QComboBox(self.centralwidget)
        self.EQ.setGeometry(QtCore.QRect(180, 500, 121, 31))
        self.EQ.setObjectName("EQ")
        self.EQ.setStyleSheet('''
    QComboBox {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 14px;
    }
    QComboBox:focus {
        border: 2px solid #0095F6;
    }
    QComboBox::hover {
        border: 2px solid #B2B2B2;
    }
''')
        self.EQ.addItems(['A', 'B', 'C'])
        self.Tinter = QtWidgets.QComboBox(self.centralwidget)
        self.Tinter.setGeometry(QtCore.QRect(180, 560, 121, 31))
        self.Tinter.setObjectName("Tinter")
        self.Tinter.setStyleSheet('''
    QComboBox {
        border: 2px solid #30A2FF;
        border-radius: 10px;
        padding: 5px;
        font-size: 14px;
    }
    QComboBox:focus {
        border: 2px solid #0095F6;
    }
    QComboBox::hover {
        border: 2px solid #B2B2B2;
    }
''')

        self.Tinter.addItems(['Corrective', 'Préventive']) 
        self.NOT = QtWidgets.QLineEdit(self.centralwidget)
        self.NOT.setGeometry(QtCore.QRect(180, 200, 121, 31))
        self.NOT.setObjectName("NOT")
        self.NOT.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
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
        validator = QtGui.QIntValidator()
        self.NOT.setValidator(validator)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 160, 51, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 200, 51, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 240, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(30, 280, 101, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(30, 320, 121, 31))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(30, 365, 121, 31))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(30, 460, 121, 31))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 500, 121, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(30, 540, 141, 71))
        self.label_10.setObjectName("label_10")
        self.TI = QtWidgets.QLineEdit(self.centralwidget)
        self.TI.setGeometry(QtCore.QRect(180, 410, 121, 31))
        self.TI.setObjectName("TI")
        self.TI.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
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
        validator = QtGui.QIntValidator()
        self.TI.setValidator(validator)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(30, 395, 121, 71))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(30, 650, 141, 31))
        self.label_12.setObjectName("label_12")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 680, 341, 171))
        self.textEdit.setStyleSheet("border-color: rgb(0, 0, 255);")
        self.textEdit.setObjectName("textEdit")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(0, 0, 345, 91))
        self.label_13.setStyleSheet("border-image: url(:/loggg/ak.jpg);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(70, 110, 211, 21))
        self.label_14.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_14.setObjectName("label_14")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(-10, 820, 361, 71))
        self.pushButton.setStyleSheet("color: rgb(0, 85, 255);\n"
"font: 75 28pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 830, 41, 41))
        self.label_15.setStyleSheet("border-image: url(:/loggg/Save_37110.png);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        self.TM = QtWidgets.QLineEdit(self.centralwidget)
        self.TM.setGeometry(QtCore.QRect(180, 610, 121, 31))
        self.TM.setObjectName("NOT")
        self.TM.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
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
        validator = QtGui.QIntValidator()
        self.TM.setValidator(validator)
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(30, 610, 141, 31))
        self.label_18.setObjectName("label_12")
        Inter.setCentralWidget(self.centralwidget)
        self.pushButton.clicked.connect(self.Save)
        self.retranslateUi(Inter)
        QtCore.QMetaObject.connectSlotsByName(Inter)

    def retranslateUi(self, Inter):
        _translate = QtCore.QCoreApplication.translate
        Inter.setWindowTitle(_translate("Inter", "Fiche d'inetervention"))
        self.label_2.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Date</span></p></body></html>"))
        self.label_3.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">N°OT</span></p><p><br/></p></body></html>"))
        self.label_4.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Machine</span></p></body></html>"))
        self.label_5.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Famille</span></p></body></html>"))
        self.label_6.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Heure Début</span></p></body></html>"))
        self.label_7.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Heure Fin</span></p></body></html>"))
        self.label_8.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Demandeur</span></p></body></html>"))
        self.label_9.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Equipe</span></p></body></html>"))
        self.label_10.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Type </span></p><p><span style=\" font-size:14pt; font-weight:600;\">d\'intervention</span></p><p><br/></p></body></html>"))
        self.label_11.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:13pt; font-weight:600;\">Temps </span></p><p><span style=\" font-size:13pt; font-weight:600;\">d\'intervention</span></p></body></html>"))
        self.label_12.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Déscription</span></p></body></html>"))
        self.label_14.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Fiche d\'intervention</span></p></body></html>"))
        self.label_18.setText(_translate("Inter", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Technicien</span></p></body></html>"))
        self.pushButton.setText(_translate("Inter", "Valider"))
        
import akwel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Inter = QtWidgets.QMainWindow()
    ui = Ui_Inter()
    ui.setupUi(Inter)

   
    Inter.show()
    sys.exit(app.exec_())
