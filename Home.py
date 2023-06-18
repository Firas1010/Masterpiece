from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QFont
from Login import Ui_login
from LogMaint import Ui_LogM
from PyQt5.QtWidgets import QHBoxLayout,QMessageBox,QPushButton,QApplication
import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="pyqtgraph")
import os
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
import matplotlib.pyplot as plt



class Ui_APP(object):
    def message(self):
            msg=QMessageBox()
            msg.setWindowTitle("APropos")
            msg.setText("Application pour résoudre le probléme de fiabilité des données.\n"
"\n"                        
"L'application développée par Firas HOUIMEL, élève ingénieur en Génie des Systèmes Industriels et Logistiques à l'Ecole Nationale d’Ingénieurs de Carthage (ENICarthage), est le fruit d'un projet de fin d'études réalisé entre 2022 et 2023.\n"
"Cette application a été conçue pour résoudre le problème de fiabilité des données dans le contexte industriel. Elle vise à garantir l'exactitude et la précision des données tout en orientant l'entreprise vers les 5 Zeros, c'est-à-dire zéro défaut, zéro panne, zéro arrêt, zéro stock et zéro délai.\n"
"\n"
"En s'appuyant sur les principes de l'industrie 4.0 et de la digitalisation, cette application offre des fonctionnalités avancées pour améliorer la gestion et la traçabilité des opérations de production. Elle automatise les processus, collecte et enregistre les données en temps réel, facilite la génération de rapports et permet une surveillance continue de la performance de la ligne de production.\n"
"\n"
"cette application représente une solution innovante pour résoudre le problème de fiabilité des données dans le domaine industriel. Elle offre un moyen efficace de transformer l'entreprise vers l'industrie 4.0 et la digitalisation tout en garantissant des opérations plus efficaces, une meilleure traçabilité et une prise de décision basée sur des données fiables. \n")
            msg.setIcon(QMessageBox.Information)
            x = msg.exec_()

    def Openlogin(self):
  
        
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_login()
        self.ui.setupUi(self.window)
        APP.hide()
        self.window.show()




    def OpenL(self):
        os.system('start excel.exe "%s"' % ("L229.xlsx", )) 


    def Opendashb(self):
        df2=pd.read_excel('ReportingMaintenance.xlsx',engine='openpyxl')
        
        MTTR=df2['Temps dintervention en min'].sum()/df2['Famille'].count()
        print(MTTR)


        # Sample data (replace with your actual data)
        excel_file_path = 'DBSCM.xlsx'
        df = pd.read_excel(excel_file_path,engine='openpyxl')
        print(df)
        print (df['Date de fab'])
        MTBF=df['H Payée'].sum()/df2['Famille'].count()
        print(MTBF)
        # Create subplots with 2 rows and 2 columns
        fig = make_subplots(rows=2, cols=4,
                            vertical_spacing=0.2,
                            horizontal_spacing=0.1,
                            specs=[[{}, {}, {},{}],
                                  [{}, {}, {},{}]],
                            row_width=[1, 1],
                            column_width=[1,1,1,1]
                            )

        # Add Bar Graph: Quantité produite vs. Date de fab
        df_grouped7 = df.groupby('Date de fab')['Quantité produite'].sum().reset_index()
        fig.add_trace(go.Bar(x=df_grouped7['Date de fab'], y=df_grouped7['Quantité produite'],name='Quantité produite'), row=1, col=1)
        fig.update_layout(title='Quantité produite par rapport à la date de fab',
                        xaxis_title='Date de fab',
                        yaxis_title='Quantité produite')
        
        
        # Add Bar Graph: Quantité produite vs. Date de fab
        df_grouped9 = df.groupby('Equipe')['Quantité produite'].sum().reset_index()
        df_grouped10= df.groupby('Equipe')['Rendement'].sum().reset_index()
        print(df_grouped9)
        fig.add_trace(go.Bar(
        x=df_grouped10['Equipe'],
        y=(df_grouped10['Rendement'] / df_grouped10['Equipe'].count()) * 100,
        text=(df_grouped10['Rendement'] / df_grouped10['Equipe'].count()) * 100,
        texttemplate='%{text:.2f}',  # Format the labels to two decimal places
        textposition='auto',  # Display text above the bars
        name='Efficience en %'),row=1, col=4)
        fig.update_layout(title='Rendement des Equipe',
                        xaxis_title='Equipe',
                        yaxis_title='Quantité produite')
        

        # Add Line Graph: H Réel and H Payée vs. Date de fab
        df_grouped5 = df.groupby('Date de fab')['H Réel'].sum().reset_index()
        df_grouped6= df.groupby('Date de fab')['H Payée'].sum().reset_index()
        fig.add_trace(go.Scatter(x=df_grouped5['Date de fab'], y=df_grouped5['H Réel'], mode='lines+markers', name='H Réel'), row=1, col=3)
        fig.add_trace(go.Scatter(x=df_grouped6['Date de fab'], y=['22.5']*df_grouped6['Date de fab'].count(), mode='lines+markers', name='H Payée'), row=1, col=3)
        fig.update_layout(title='H Réel and H Payée par rapport à la date de fab',
                        xaxis_title='Date de fab',
                        yaxis_title='H')

        # Add Bar Graph: Vente and Perte vs. Semaine
        df_grouped3 = df.groupby('Date de fab')['Vente'].sum().reset_index()
        df_grouped4= df.groupby('Date de fab')['Perte'].sum().reset_index()
        fig.add_trace(go.Scatter(x=df_grouped3['Date de fab'], y=df_grouped3['Vente'], mode='lines+markers', name='Vente'), row=2, col=3)
        fig.add_trace(go.Scatter(x=df_grouped4['Date de fab'], y=df_grouped4['Perte'], mode='lines+markers', name='Perte'), row=2, col=3)
        fig.update_layout(title='Vente and Perte par rapport à la semaine de fabrication',
                        xaxis_title='Semaine',
                        yaxis_title='Quantité')

        # Create Pie Chart: Quantité produite vs. Total Rebut
        labels = ['Quantité produite', 'Total Rebut']
        values = [df['Quantité produite'].sum(), df['Total Rebut'].sum()]
        fig_pie = go.Figure(data=[go.Pie(labels=labels, values=values)])
        fig_pie.update_layout(title='Quantité produite vs. Total Rebut')
        
        df_grouped1 = df.groupby('Date de fab')['Total Rebut'].sum().reset_index()
        df_grouped8= df.groupby('Date de fab')['Total Rebut'].sum().reset_index()
        fig.add_trace(go.Scatter(x=df_grouped8['Date de fab'], y=(df_grouped8['Total Rebut']/df_grouped7['Quantité produite'])*100, mode='lines+markers', name='Taux de non conformité'), row=1, col=2)
        fig.add_trace(go.Scatter(x=df_grouped1['Date de fab'], y=df_grouped1['Total Rebut'], mode='lines+markers', name='Scrap'), row=1, col=2)
        fig.update_layout(title='Rejet',
                        xaxis_title='Date de fab',
                        yaxis_title='Scrap')
        
        df_grouped = df2.groupby('Date')['Temps dintervention en min'].sum().reset_index()
        print(df_grouped)
        fig.add_trace(go.Scatter(x=df_grouped['Date'], y=df_grouped['Temps dintervention en min'], mode='lines+markers', name='Arrêt machine'), row=2, col=2)
        fig.update_layout(title='Arrêt machine',
                        xaxis_title='Date de fab',
                        yaxis_title='Temps dintervention')

        # Gauge Chart: Mean of Rendement
        mean_rendement = df['Rendement'].mean()
        fig.add_trace(go.Indicator(
            mode='gauge+number',
            value=mean_rendement * 100,
            title={'text': "Moyenne Rendement", 'font': {'size': 12}},
            domain={'x': [0, 0.2], 'y': [0, 0.3]},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': "white"},
                'steps': [
                    {'range': [0, 50], 'color': 'RED'},
                    {'range': [50, 85], 'color': 'yellow'},
                    {'range': [85, 100], 'color': 'green'}],
                'threshold': {
                    'line': {'color': "green", 'width': 4},
                    'thickness': 0.75,
                    'value': mean_rendement * 100}}))
        
        df3 = pd.read_excel('Production.xlsx',engine='openpyxl')
        print(df3['Week '])
        fig.add_trace(go.Scatter(x=df3['Week '], y=df3['QRMC'], mode='lines+markers', name='QRMC'), row=2, col=4)
        fig.add_trace(go.Scatter(x=df3['Week '], y=df3['POR'], mode='lines+markers', name='POR'), row=2, col=4)
        fig.update_layout(title='Indicateur de performance',
                        xaxis_title='Date',
                        yaxis_title='Quantité')

        # Display the combined figure
        
        fig.show()
        plt.show()

    def OpenM(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogM()
        self.ui.setupUi(self.window)
        APP.hide()
        self.window.show()


    def setupUi(self, APP):


        APP.setWindowFlags(QtCore.Qt.CustomizeWindowHint | QtCore.Qt.FramelessWindowHint)
        APP.setObjectName("APP")
        APP.resize(450, 646)
        self.centralwidget = QtWidgets.QWidget(APP)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 451, 651))
        self.label.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.Prod = QtWidgets.QPushButton(self.centralwidget)
        self.Prod.setGeometry(QtCore.QRect(155, 300, 151, 40))
        self.Prod.setStyleSheet("""
            QPushButton {
                background-color: #0080FF;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #988ECA;
            }
            QPushButton:pressed {
                background-color: #6459C9;
            }
        """)
        font = QFont("Arial", 18)
        font.setBold(True)
        self.Prod.setFont(font)
        self.Prod.setObjectName("Prod")

        self.DB = QtWidgets.QPushButton(self.centralwidget)
        self.DB.setGeometry(QtCore.QRect(155, 360, 151, 40))
        self.DB.setStyleSheet("""
            QPushButton {
                background-color: #0080FF;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #988ECA;
            }
            QPushButton:pressed {
                background-color: #6459C9;
            }
        """)
        font = QFont("Arial", 18)
        font.setBold(True)
        self.DB.setFont(font)    
        self.DB.setObjectName("DB")
        self.L2 = QtWidgets.QPushButton(self.centralwidget)
        self.L2.setGeometry(QtCore.QRect(155, 420, 151, 40))
        self.L2.setStyleSheet("""
            QPushButton {
                background-color: #0080FF;
                color: white;
                border: none;
                border-radius: 5px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: #988ECA;
            }
            QPushButton:pressed {
                background-color: #6459C9;
            }
        """)
        font = QFont("Arial", 18)
        font.setBold(True)
        self.L2.setFont(font)        
        self.L2.setObjectName("L2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 451, 241))
        self.label_2.setStyleSheet("border-image: url(:/loggg/Robots-in-car-manufacturing1.jpg);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.Info = QtWidgets.QPushButton(self.centralwidget)
        self.Info.setGeometry(QtCore.QRect(420, 0, 31, 21))
        self.Info.setStyleSheet("border-image: url(:/loggg/information.png);")
        self.Info.setText("")
        self.Info.setObjectName("Info")
        self.Close = QtWidgets.QPushButton(self.centralwidget)
        self.Close.setGeometry(QtCore.QRect(0, 0, 21, 20))
        self.Close.setStyleSheet("border-image: url(:/loggg/cancel.png);")
        self.Close.setText("")
        self.Close.setObjectName("Close")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 530, 461, 121))
        self.label_3.setStyleSheet("border-image: url(:/loggg/ak.jpg);")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        APP.setCentralWidget(self.centralwidget)

        self.retranslateUi(APP)
        QtCore.QMetaObject.connectSlotsByName(APP)
        self.Prod.clicked.connect(self.Openlogin)
        self.DB.clicked.connect(self.Opendashb)
        self.L2.clicked.connect(self.OpenL)
        # self.Maint.clicked.connect(self.OpenM)
        self.Close.clicked.connect(APP.close) 
        self.Info.clicked.connect(self.message)
        
    def retranslateUi(self, APP):
        _translate = QtCore.QCoreApplication.translate
        APP.setWindowTitle(_translate("APP", "APP"))
        self.Prod.setText(_translate("APP", "Production"))
        # self.Maint.setText(_translate("APP", "Maintenance"))
        self.DB.setText(_translate("APP", "Dashboard"))
        self.L2.setText(_translate("APP", "L229"))
import akwel


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    APP = QtWidgets.QMainWindow()
    ui = Ui_APP()
    ui.setupUi(APP)
    APP.show()
    sys.exit(app.exec_())
