from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
from datetime import datetime
import os
import shutil
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtCore import QDate, QTime
from LogMaint import Ui_LogM



class Ui_Proddata(object):
    def __init__(self):
        self.window = None  # Store the reference to the choix window
        self.login_window = None  # Store the reference to the login window    
    
    
    
    def OpenRebut(self):
        source_file = "Rebut jj_mm_aaaa.xlsx"
        new_name = datetime.now().strftime("%d-%m-%Y")
        def check_time():
            now = datetime.now().time()

            if now < datetime(1, 1, 1, 6, 30).time():
                return 'C'
            elif now < datetime(1, 1, 1, 14, 30).time():
                return 'A'
            elif now < datetime(1, 1, 1, 22, 30).time():
                return 'B'
            else:
                return 'C'

        # Example usage
        result = check_time()
        print(result)

        # Get the directory path of the source file
        directory = os.path.dirname(source_file)

        # Get the file extension of the source file
        extension = os.path.splitext(source_file)[1]

        # Construct the new file name with the new name and the existing extension
        new_file = os.path.join(directory, 'Rebut'+'_'+ 'Equipe'+'_'+ result+'_'+new_name +  extension)

        # Copy the source file to the new destination
        shutil.copy2(source_file, new_file)

        # Open the copied file
        os.system('start excel.exe "%s"' % new_file)
        
    def OpenM(self):

        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_LogM()
        self.ui.setupUi(self.window)
        
        self.window.show()
    
    def DSB(self):
        try :
            #remplir les variables
            
            Date = self.DATELINE.text()
            OP = self.LENOB.text()
            Ligne = self.LE229.text()
            Tc = float(self.LETC.text()) if self.LETC.text() else 0.0
            RE = self.REF.text()
            Eq = self.LEequipe.text()

    # Convert empty fields to 0.0
            Cad1 = float(self.CAD1.text()) if self.CAD1.text() else 0.0
            Cad2 = float(self.CAD2.text()) if self.CAD2.text() else 0.0
            Cad3 = float(self.CAD3.text()) if self.CAD3.text() else 0.0
            Cad4 = float(self.CAD4.text()) if self.CAD4.text() else 0.0
            Cad5 = float(self.CAD5.text()) if self.CAD5.text() else 0.0
            Cad6 = float(self.CAD6.text()) if self.CAD6.text() else 0.0
            Cad7 = float(self.CAD7.text()) if self.CAD7.text() else 0.0
            Cad8 = float(self.CAD8.text()) if self.CAD8.text() else 0.0
            # Convert empty fields to 0.0 for Work
            Work1 = float(self.LEcad1.text()) if self.LEcad1.text() else 0.0
            Work2 = float(self.LEcad2.text()) if self.LEcad2.text() else 0.0
            Work3 = float(self.LEcad3.text()) if self.LEcad3.text() else 0.0
            Work4 = float(self.LEcad4.text()) if self.LEcad4.text() else 0.0
            Work5 = float(self.LEcad5.text()) if self.LEcad5.text() else 0.0
            Work6 = float(self.LEcad6.text()) if self.LEcad6.text() else 0.0
            Work7 = float(self.LEcad7.text()) if self.LEcad7.text() else 0.0
            Work8 = float(self.LEcad8.text()) if self.LEcad8.text() else 0.0

            # Convert empty fields to 0.0 for Rebut
            Rebut1 = float(self.LER1.text()) if self.LER1.text() else 0.0
            Rebut2 = float(self.LER2.text()) if self.LER2.text() else 0.0
            Rebut3 = float(self.LER3.text()) if self.LER3.text() else 0.0
            Rebut4 = float(self.LER4.text()) if self.LER4.text() else 0.0
            Rebut5 = float(self.LER5.text()) if self.LER5.text() else 0.0
            Rebut6 = float(self.LER6.text()) if self.LER6.text() else 0.0
            Rebut7 = float(self.LER7.text()) if self.LER7.text() else 0.0
            Rebut8 = float(self.LER8.text()) if self.LER8.text() else 0.0
            Heure1 = self.H1.text()
            Heure2 = self.H2.text()
            Heure3 = self.H3.text()
            Heure4 = self.H4.text()
            Heure5 = self.H5.text()
            Heure6 = self.H6.text()
            Heure7 = self.H7.text()
            Heure8 = self.H8.text()
            Prod=[Work1, Work2, Work3, Work4, Work5, Work6, Work7, Work8]
            x=sum(Prod)
            print(x)
            Scrap=[Rebut1, Rebut2, Rebut3, Rebut4, Rebut5, Rebut6, Rebut7, Rebut8]
            y=sum(Scrap)
            print(y)
            def get_week_number(date_string):
                    date = datetime.strptime(date_string, "%d/%m/%Y")
                    week_number = date.isocalendar()[1]
                    return week_number

                # Example usage
            date_string = Date
            week_number = get_week_number(date_string)
            WEEK='W'+str(week_number)
            CADH=sum([Cad1,Cad2,Cad3,Cad4,Cad5,Cad6,Cad7,Cad8])/8
            HR=(x*Tc)/60
            HP=22.5
            P="EB2020"
            EFF=HR/HP
            MG=4.34*y
            V=4.34*x
            file="DBSCM.xlsx"
            now = datetime.now().time()
            # if now < datetime(1, 1, 1, 6, 30).time() or now < datetime(1, 1, 1, 14, 30).time() or now < datetime(1, 1, 1, 22, 30).time() :

            def get_intervention_time(Search_date, time):


                Search_date = str(Search_date)
                time = str(time)
                DT = Search_date
                print(DT)
                print(time)
                df = pd.read_excel('ReportingMaintenance.xlsx')
                df['Temps dintervention en min'] = df['Temps dintervention en min'].astype(float)
                print(df)
                filtered_df = df[(df['Date'] == DT) & (df['Temps/H de travail'] == time)]
                if not filtered_df.empty:
                    intervention_time = float(sum(filtered_df['Temps dintervention en min']))
                    return intervention_time

                return float(0)


            Search_date = Date
            time1 = Heure1
            intervention_time1 = get_intervention_time(Search_date, time1)

            time2 = Heure2
            intervention_time2 = get_intervention_time(Search_date, time2)

                    
            time3 = Heure3
            intervention_time3 = get_intervention_time(Search_date, time3)
            
            time4 = Heure4
            intervention_time4 = get_intervention_time(Search_date, time4)
            
            time5 = Heure5
            intervention_time5 = get_intervention_time(Search_date, time5)
            
            time6 = Heure6
            intervention_time6 = get_intervention_time(Search_date, time6)
            
            time7 = Heure7
            intervention_time7 = get_intervention_time(Search_date, time7)
            
            time8 = Heure8
            intervention_time8 = get_intervention_time(Search_date, time8)

        
            if ((Cad1!=Work1+Rebut1+round(intervention_time1/Tc) )or (Cad2!=Work2+Rebut2+round(intervention_time2/Tc) ) or (Cad3!=Work3+Rebut3+round(intervention_time3/Tc) )or (Cad4!=Work4+Rebut4+(intervention_time4/Tc)  )or (Cad5!=Work5+Rebut5+(intervention_time5/Tc) )or (Cad6!=Work6+Rebut6+(intervention_time6/Tc)  )or (Cad7!=Work7+Rebut7+(intervention_time7/Tc) )or (Cad8!=Work8+Rebut8+(intervention_time8/Tc) ) ):
                                    msg = QMessageBox()
                                    msg.setWindowTitle('Erreur')
                                    msg.setText("Données incorrect.\nVeuillez saisir à nouveau les données.")
                                    msg.setIcon(QMessageBox.Warning)
                                    x = msg.exec_()     
                    
            else :   
                    if '' in (OP, Ligne, Tc, Eq, Cad1, Cad2, Cad3, Cad4, Cad5, Cad6, Cad7, Cad8, Work1, Work2, Work3, Work4, Work5, Work6, Work7, Work8, Rebut1, Rebut2, Rebut3, Rebut4, Rebut5, Rebut6, Rebut7, Rebut8):
                            return 
                
    
                    else : 
                        if os.path.isfile(file):
                                                    current_time = datetime.now().strftime("%H:%M:%S")
                                                    # Read the existing result file
                                                    existing_data = pd.read_excel(file, sheet_name='BigData')

                                                    # Create a DataFrame with the new BigData entry
                                                    new_entry = pd.DataFrame({'Référence ':[RE],'Semaine':[WEEK],'Date de fab': [Date], 'Projet':[ P],'Ligne':[Ligne] ,'Equipe': [Eq],'CAD/H':[ CADH],'Nombre dops ': [OP],  'Tc': [Tc],  'H Réel': [HR], 'H Payée': [HP],'Rendement':[EFF] ,'Quantité produite': [x], 'Total Rebut': [y],'Perte':[MG],'Vente':[V]})

                                                    # Concatenate the existing BigData data and the new BigData entry
                                                    updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

                                                    # Save the updated BigData data to the result file
                                                    updated_data.to_excel(file, sheet_name='BigData', index=False, engine='openpyxl')
                                                    
                                                    print("BigData data added to the result file successfully.")
                                                    msg = QMessageBox()
                                                    msg.setWindowTitle('SAVE')
                                                    msg.setText("Données enregistrer.\nProduction data added to the file successfully.")
                                                    msg.setIcon(QMessageBox.Information)
                                                    x = msg.exec_()
                        else:
                                                    # Create a new result file with the new BigData entry
                                                    data = pd.DataFrame({'Référence ':[RE],'Semaine':[WEEK],'Date de fab': [Date], 'Projet':[ P],'Ligne':[Ligne] ,'Equipe': [Eq],'CAD/H':[ CADH],'Nombre dops ': [OP],  'Tc': [Tc],  'H Réel': [HR], 'H Payée': [HP], 'Rendement':[EFF],'Quantité produite': [x], 'Total Rebut': [y],'Perte':[MG],'Vente':[V]})

                                                    # Save the new BigData entry DataFrame to the result file
                                                    data.to_excel(file, sheet_name='BigData', index=False, engine='openpyxl')

                                                    print("BigData data added to the result file successfully.")
                                                    msg = QMessageBox()
                                                    msg.setWindowTitle('SAVE')
                                                    msg.setText("Données enregistrer.\nProduction data added to the file successfully.")
                                                    msg.setIcon(QMessageBox.Information)
                                                    x = msg.exec_() 
                        # else :
                        #                     msg = QMessageBox()
                        #                     msg.setWindowTitle('Erreur')
                        #                     msg.setText("Données incorrect.\nVeuillez saisir à nouveau les données.")
                        #                     msg.setIcon(QMessageBox.Warning)
                        #                     x = msg.exec_()   
        except FileNotFoundError:
                                    msg = QMessageBox()
                                    msg.setWindowTitle('Erreur')
                                    msg.setText("Données incorrect.\nVeuillez saisir à nouveau les données.")
                                    msg.setIcon(QMessageBox.Warning)
                                    x = msg.exec_()   


    def clear_variables(self):
        # Clear input variables
        self.DATELINE.setDate(datetime.now())

        # Clear other variables
        self.LENOB.setText('4')
        self.LE229.setText('229')
        self.LETC.setText('1')
        def check_time():
                            now = datetime.now().time()

                            if now < datetime(1, 1, 1, 6, 30).time():
                                return 'C'
                            elif now < datetime(1, 1, 1, 14, 30).time():
                                return 'A'
                            elif now < datetime(1, 1, 1, 22, 30).time():
                                return 'B'
                            else:
                                return 'C'

        EQ = check_time()
        self.LEequipe.setText(EQ)
        self.REF.setText('P1026363A02')
        self.H1.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H2.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H3.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H4.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H5.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H6.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H7.setTime(QTime.fromString("00:00", "hh:mm"))
        self.H8.setTime(QTime.fromString("00:00", "hh:mm"))

        # Clear CAD variables
        self.CAD1.setText('')
        self.CAD2.setText('')
        self.CAD3.setText('')
        self.CAD4.setText('')
        self.CAD5.setText('')
        self.CAD6.setText('')
        self.CAD7.setText('')
        self.CAD8.setText('')

        # Clear Work variables
        self.LEcad1.setText('')
        self.LEcad2.setText('')
        self.LEcad3.setText('')
        self.LEcad4.setText('')
        self.LEcad5.setText('')
        self.LEcad6.setText('')
        self.LEcad7.setText('')
        self.LEcad8.setText('')

        # Clear Rebut variables
        self.LER1.setText('')
        self.LER2.setText('')
        self.LER3.setText('')
        self.LER4.setText('')
        self.LER5.setText('')
        self.LER6.setText('')
        self.LER7.setText('')
        self.LER8.setText('')

        # Clear COM variables
        self.C1.setText('')
        self.C2.setText('')
        self.C3.setText('')
        self.C4.setText('')
        self.C5.setText('')
        self.C6.setText('')
        self.C7.setText('')
        self.C8.setText('')
   

    

    def Tpréel(self, window):

            
        #remplir les variables
        Date = self.DATELINE.text()
        OP = self.LENOB.text()
        Ligne = self.LE229.text()
        Tc = float(self.LETC.text()) if self.LETC.text() else 0.0
        Eq = self.LEequipe.text()
        Heure1 = self.H1.text()
        Heure2 = self.H2.text()
        Heure3 = self.H3.text()
        Heure4 = self.H4.text()
        Heure5 = self.H5.text()
        Heure6 = self.H6.text()
        Heure7 = self.H7.text()
        Heure8 = self.H8.text()
# Convert empty fields to 0.0
        Cad1 = float(self.CAD1.text()) if self.CAD1.text() else 0.0
        Cad2 = float(self.CAD2.text()) if self.CAD2.text() else 0.0
        Cad3 = float(self.CAD3.text()) if self.CAD3.text() else 0.0
        Cad4 = float(self.CAD4.text()) if self.CAD4.text() else 0.0
        Cad5 = float(self.CAD5.text()) if self.CAD5.text() else 0.0
        Cad6 = float(self.CAD6.text()) if self.CAD6.text() else 0.0
        Cad7 = float(self.CAD7.text()) if self.CAD7.text() else 0.0
        Cad8 = float(self.CAD8.text()) if self.CAD8.text() else 0.0
        # Convert empty fields to 0.0 for Work
        Work1 = float(self.LEcad1.text()) if self.LEcad1.text() else 0.0
        Work2 = float(self.LEcad2.text()) if self.LEcad2.text() else 0.0
        Work3 = float(self.LEcad3.text()) if self.LEcad3.text() else 0.0
        Work4 = float(self.LEcad4.text()) if self.LEcad4.text() else 0.0
        Work5 = float(self.LEcad5.text()) if self.LEcad5.text() else 0.0
        Work6 = float(self.LEcad6.text()) if self.LEcad6.text() else 0.0
        Work7 = float(self.LEcad7.text()) if self.LEcad7.text() else 0.0
        Work8 = float(self.LEcad8.text()) if self.LEcad8.text() else 0.0

        # Convert empty fields to 0.0 for Rebut
        Rebut1 = float(self.LER1.text()) if self.LER1.text() else 0.0
        Rebut2 = float(self.LER2.text()) if self.LER2.text() else 0.0
        Rebut3 = float(self.LER3.text()) if self.LER3.text() else 0.0
        Rebut4 = float(self.LER4.text()) if self.LER4.text() else 0.0
        Rebut5 = float(self.LER5.text()) if self.LER5.text() else 0.0
        Rebut6 = float(self.LER6.text()) if self.LER6.text() else 0.0
        Rebut7 = float(self.LER7.text()) if self.LER7.text() else 0.0
        Rebut8 = float(self.LER8.text()) if self.LER8.text() else 0.0

# Rest of the code...

        COM1 = self.C1.text()
        COM2 = self.C2.text()
        COM3 = self.C3.text()
        COM4 = self.C4.text()
        COM5 = self.C5.text()
        COM6 = self.C6.text()
        COM7 = self.C7.text()
        COM8 = self.C8.text()
        
 


        def get_intervention_time(Search_date, time):


            Search_date = str(Search_date)
            time = str(time)
            DT = Search_date
            print(DT)
            print(time)
            df = pd.read_excel('ReportingMaintenance.xlsx')
            df['Temps dintervention en min'] = df['Temps dintervention en min'].astype(float)
            print(df)
            filtered_df = df[(df['Date'] == DT) & (df['Temps/H de travail'] == time)]
            if not filtered_df.empty:
                intervention_time = float(sum(filtered_df['Temps dintervention en min']))
                return intervention_time

            return float(0)


        Search_date = Date
        time1 = Heure1
        intervention_time1 = get_intervention_time(Search_date, time1)

        time2 = Heure2
        intervention_time2 = get_intervention_time(Search_date, time2)

                 
        time3 = Heure3
        intervention_time3 = get_intervention_time(Search_date, time3)
        
        time4 = Heure4
        intervention_time4 = get_intervention_time(Search_date, time4)
        
        time5 = Heure5
        intervention_time5 = get_intervention_time(Search_date, time5)
        
        time6 = Heure6
        intervention_time6 = get_intervention_time(Search_date, time6)
        
        time7 = Heure7
        intervention_time7 = get_intervention_time(Search_date, time7)
        
        time8 = Heure8
        intervention_time8 = get_intervention_time(Search_date, time8)

        
        if ((Cad1!=Work1+Rebut1+round(intervention_time1/Tc) )or (Cad2!=Work2+Rebut2+round(intervention_time2/Tc) ) or (Cad3!=Work3+Rebut3+round(intervention_time3/Tc) )or (Cad4!=Work4+Rebut4+(intervention_time4/Tc)  )or (Cad5!=Work5+Rebut5+(intervention_time5/Tc) )or (Cad6!=Work6+Rebut6+(intervention_time6/Tc)  )or (Cad7!=Work7+Rebut7+(intervention_time7/Tc) )or (Cad8!=Work8+Rebut8+(intervention_time8/Tc) ) ):
                                msg = QMessageBox()
                                msg.setWindowTitle('Erreur')
                                msg.setText("Données incorrect.\nVeuillez saisir à nouveau les données.")
                                msg.setIcon(QMessageBox.Warning)
                                x = msg.exec_()     
                
        else :   
                if None in (OP, Ligne, Tc, Eq, Cad1, Cad2, Cad3, Cad4, Cad5, Cad6, Cad7, Cad8, Work1, Work2, Work3, Work4, Work5, Work6, Work7, Work8, Rebut1, Rebut2, Rebut3, Rebut4, Rebut5, Rebut6, Rebut7, Rebut8):
                        return
            
 
                else :    
                    try:
                        def check_time():
                            now = datetime.now().time()

                            if now < datetime(1, 1, 1, 6, 30).time():
                                return 'C'
                            elif now < datetime(1, 1, 1, 14, 30).time():
                                return 'A'
                            elif now < datetime(1, 1, 1, 22, 30).time():
                                return 'B'
                            else:
                                return 'C'

                        EQ = check_time()
                        print(EQ)   
                        
                        def convert_date_format(TD):
                            day, month, year = TD.split('/')
                            CD = f"{day}-{month}-{year}"
                            return CD
                        DT = convert_date_format(Date)
                        
                        Vérifier="Rebut_Equipe_"+EQ+"_"+DT+".xlsx"
                        print(Vérifier)
                        
                        data1=pd.read_excel(Vérifier)
                        df1=pd.DataFrame(data1)
                        SR=df1.iloc[16,28]
                        print(SR)
                        
                        Prod=[Work1, Work2, Work3, Work4, Work5, Work6, Work7, Work8]
                        x=sum(Prod)
                        print(x)
                        Scrap=[Rebut1, Rebut2, Rebut3, Rebut4, Rebut5, Rebut6, Rebut7, Rebut8]
                        y=sum(Scrap)
                        print(y)
                        
                        if y==SR :
 
                            file = "ReportingProduction.xlsx"

                            # Check if the result file already exists
                            if os.path.isfile(file):
                                current_time = datetime.now().strftime("%H:%M:%S")
                                # Read the existing result file
                                existing_data = pd.read_excel(file, sheet_name='Production')

                                # Create a DataFrame with the new production entry
                                new_entry = pd.DataFrame({'Date': [Date], 'Time':[current_time ],'OP': [OP], 'Ligne': [Ligne], 'Tc': [Tc], 'Eq': [Eq], 'Heure1': [Heure1], 'Heure2': [Heure2], 'Heure3': [Heure3], 'Heure4': [Heure4], 'Heure5': [Heure5], 'Heure6': [Heure6], 'Heure7': [Heure7], 'Heure8': [Heure8], 'Cad1': [Cad1], 'Cad2': [Cad2], 'Cad3': [Cad3], 'Cad4': [Cad4], 'Cad5': [Cad5], 'Cad6': [Cad6], 'Cad7': [Cad7], 'Cad8': [Cad8], 'Work1': [Work1], 'Work2': [Work2], 'Work3': [Work3], 'Work4': [Work4], 'Work5': [Work5], 'Work6': [Work6], 'Work7': [Work7], 'Work8': [Work8], 'Rebut1': [Rebut1], 'Rebut2': [Rebut2], 'Rebut3': [Rebut3], 'Rebut4': [Rebut4], 'Rebut5': [Rebut5], 'Rebut6': [Rebut6], 'Rebut7': [Rebut7], 'Rebut8': [Rebut8], 'COM1': [COM1], 'COM2': [COM2], 'COM3': [COM3], 'COM4': [COM4], 'COM5': [COM5], 'COM6': [COM6], 'COM7': [COM7], 'COM8': [COM8]})

                                # Concatenate the existing production data and the new production entry
                                updated_data = pd.concat([existing_data, new_entry], ignore_index=True)

                                # Save the updated production data to the result file
                                updated_data.to_excel(file, sheet_name='Production', index=False, engine='openpyxl')
                                
                                print("Production data added to the result file successfully.")
                                msg = QMessageBox()
                                msg.setWindowTitle('SAVE')
                                msg.setText("Données enregistrer.\nProduction data added to the file successfully.")
                                msg.setIcon(QMessageBox.Information)
                                x = msg.exec_()
                            else:
                                # Create a new result file with the new production entry
                                data = pd.DataFrame({'Date': [Date], 'Time':[current_time],'OP': [OP], 'Ligne': [Ligne], 'Tc': [Tc], 'Eq': [Eq], 'Heure1': [Heure1], 'Heure2': [Heure2], 'Heure3': [Heure3], 'Heure4': [Heure4], 'Heure5': [Heure5], 'Heure6': [Heure6], 'Heure7': [Heure7], 'Heure8': [Heure8], 'Cad1': [Cad1], 'Cad2': [Cad2], 'Cad3': [Cad3], 'Cad4': [Cad4], 'Cad5': [Cad5], 'Cad6': [Cad6], 'Cad7': [Cad7], 'Cad8': [Cad8], 'Work1': [Work1], 'Work2': [Work2], 'Work3': [Work3], 'Work4': [Work4], 'Work5': [Work5], 'Work6': [Work6], 'Work7': [Work7], 'Work8': [Work8], 'Rebut1': [Rebut1], 'Rebut2': [Rebut2], 'Rebut3': [Rebut3], 'Rebut4': [Rebut4], 'Rebut5': [Rebut5], 'Rebut6': [Rebut6], 'Rebut7': [Rebut7], 'Rebut8': [Rebut8], 'COM1': [COM1], 'COM2': [COM2], 'COM3': [COM3], 'COM4': [COM4], 'COM5': [COM5], 'COM6': [COM6], 'COM7': [COM7], 'COM8': [COM8]})

                                # Save the new production entry DataFrame to the result file
                                data.to_excel(file, sheet_name='Production', index=False, engine='openpyxl')

                                print("Production data added to the result file successfully.")
                                print("Production data added to the result file successfully.")
                                msg = QMessageBox()
                                msg.setWindowTitle('SAVE')
                                msg.setText("Données enregistrer.\nProduction data added to the file successfully.")
                                msg.setIcon(QMessageBox.Information)
                                x = msg.exec_()
                        else :
                            msg = QMessageBox()
                            msg.setWindowTitle('Erreur')
                            msg.setText("Données incorrect.\nVeuillez saisir à nouveau les données.")
                            msg.setIcon(QMessageBox.Warning)
                            x = msg.exec_()        
                            
                        


                    except FileNotFoundError:
                        print("Error: Database file not found.")
                        exit()
        
    
    
    
    
    

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    def setupUi(self, Proddata, window):
        self.window = window
        Proddata.setObjectName("Proddata")
        Proddata.resize(1091, 534)
        self.centralwidget = QtWidgets.QWidget(Proddata)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1091, 541))
        self.label.setStyleSheet("background-color: #F8F6F4;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.LE229 = QtWidgets.QLineEdit(self.centralwidget)
        self.LE229.setGeometry(QtCore.QRect(20, 10, 113, 31))
        self.LE229.setObjectName("LE229")
        self.LE229.setStyleSheet('''
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
        self.LE229.setText("L229") 
        # Only allow integer input
        validator = QtGui.QIntValidator()
        self.LE229.setValidator(validator)
        self.DATELINE = QtWidgets.QDateEdit(self.centralwidget)
        self.DATELINE.setGeometry(QtCore.QRect(260, 65, 110, 22))
        self.DATELINE.setObjectName("DATELINE")
        self.DATELINE.setDate(datetime.now())
        self.LEequipe = QtWidgets.QLineEdit(self.centralwidget)
        self.LEequipe.setGeometry(QtCore.QRect(20, 59, 113, 31))
        self.LEequipe.setObjectName("LEequipe")
        self.LEequipe.setStyleSheet('''
            QLineEdit {
                border: 2px solid #FFE7A0;
                border-radius: 10px;
                padding: 5px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #0095F6;
            }
            QLineEdit::hover {
                border: 2px solid #B2B2B2;
            }
        ''')
        self.LEequipe.setText("equipe") 


        self.LEcad1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad1.setGeometry(QtCore.QRect(270, 140, 151, 41))
        self.LEcad1.setObjectName("LEcad1")
        self.LEcad1.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad1.setValidator(validator)
        self.LEcad2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad2.setGeometry(QtCore.QRect(270, 190, 151, 41))
        self.LEcad2.setObjectName("LEcad2")
        self.LEcad2.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad2.setValidator(validator)
        self.LEcad3 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad3.setGeometry(QtCore.QRect(270, 240, 151, 41))
        self.LEcad3.setObjectName("LEcad3")
        self.LEcad3.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad3.setValidator(validator)
        self.LEcad4 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad4.setGeometry(QtCore.QRect(270, 290, 151, 41))
        self.LEcad4.setObjectName("LEcad4")
        self.LEcad4.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad4.setValidator(validator)
        self.LEcad5 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad5.setGeometry(QtCore.QRect(270, 340, 151, 41))
        self.LEcad5.setObjectName("LEcad5")
        self.LEcad5.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad5.setValidator(validator)
        self.LEcad7 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad7.setGeometry(QtCore.QRect(270, 440, 151, 41))
        self.LEcad7.setObjectName("LEcad7")
        self.LEcad7.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad7.setValidator(validator)
        self.LEcad6 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad6.setGeometry(QtCore.QRect(270, 390, 151, 41))
        self.LEcad6.setObjectName("LEcad6")
        self.LEcad6.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad6.setValidator(validator)
        self.LEcad8 = QtWidgets.QLineEdit(self.centralwidget)
        self.LEcad8.setGeometry(QtCore.QRect(270, 490, 151, 41))
        self.LEcad8.setObjectName("LEcad8")
        self.LEcad8.setStyleSheet('''
            QLineEdit {
                border: 2px solid blue;
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
        self.LEcad8.setValidator(validator)
        self.LER1 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER1.setGeometry(QtCore.QRect(550, 140, 151, 41))
        self.LER1.setObjectName("LER1")
        self.LER1.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER1.setValidator(validator)
        self.LER6 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER6.setGeometry(QtCore.QRect(550, 390, 151, 41))
        self.LER6.setObjectName("LER6")
        self.LER6.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER6.setValidator(validator)
        self.LER3 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER3.setGeometry(QtCore.QRect(550, 240, 151, 41))
        self.LER3.setObjectName("LER3")
        self.LER3.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER3.setValidator(validator)
        self.LER5 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER5.setGeometry(QtCore.QRect(550, 340, 151, 41))
        self.LER5.setObjectName("LER5")
        self.LER5.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER5.setValidator(validator)
        self.LER7 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER7.setGeometry(QtCore.QRect(550, 440, 151, 41))
        self.LER7.setObjectName("LER7")
        self.LER7.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER7.setValidator(validator)
        self.LER8 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER8.setGeometry(QtCore.QRect(550, 490, 151, 41))
        self.LER8.setObjectName("LER8")
        self.LER8.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER8.setValidator(validator)
        self.LER2 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER2.setGeometry(QtCore.QRect(550, 190, 151, 41))
        self.LER2.setObjectName("LER2")
        self.LER2.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER2.setValidator(validator)
        self.LER4 = QtWidgets.QLineEdit(self.centralwidget)
        self.LER4.setGeometry(QtCore.QRect(550, 290, 151, 41))
        self.LER4.setObjectName("LER4")
        self.LER4.setStyleSheet('''
            QLineEdit {
                border: 2px solid Red;
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
        self.LER4.setValidator(validator)
        self.CB1 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB1.setGeometry(QtCore.QRect(480, 150, 70, 17))
        self.CB1.setText("")
        self.CB1.setObjectName("CB1")
        self.CB2 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB2.setGeometry(QtCore.QRect(480, 200, 70, 17))
        self.CB2.setText("")
        self.CB2.setObjectName("CB2")
        self.cb3 = QtWidgets.QCheckBox(self.centralwidget)
        self.cb3.setGeometry(QtCore.QRect(480, 250, 70, 17))
        self.cb3.setText("")
        self.cb3.setObjectName("cb3")
        self.CB4 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB4.setGeometry(QtCore.QRect(480, 300, 70, 17))
        self.CB4.setText("")
        self.CB4.setObjectName("CB4")
        self.CB5 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB5.setGeometry(QtCore.QRect(480, 360, 70, 17))
        self.CB5.setText("")
        self.CB5.setObjectName("CB5")
        self.CB8 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB8.setGeometry(QtCore.QRect(480, 510, 70, 17))
        self.CB8.setText("")
        self.CB8.setObjectName("CB8")
        self.CB6 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB6.setGeometry(QtCore.QRect(480, 410, 70, 17))
        self.CB6.setText("")
        self.CB6.setObjectName("CB6")
        self.CB7 = QtWidgets.QCheckBox(self.centralwidget)
        self.CB7.setGeometry(QtCore.QRect(480, 460, 70, 17))
        self.CB7.setText("")
        self.CB7.setObjectName("CB7")
        self.BValider = QtWidgets.QPushButton(self.centralwidget)
        self.BValider.setGeometry(QtCore.QRect(950, 10, 51, 51))
        self.BValider.setStyleSheet("border-image: url(:/loggg/1486486298-arrow-down-download-downloads-downloading-save_81238(1).png);")
        self.BValider.setText("")
        self.BValider.setObjectName("BValider")
        self.BRESRT = QtWidgets.QPushButton(self.centralwidget)
        self.BRESRT.setGeometry(QtCore.QRect(1010, 10, 61, 51))
        self.BRESRT.setStyleSheet("border-image: url(:/loggg/refresh_update_15608(1).png);")
        self.BRESRT.setText("")
        self.BRESRT.setObjectName("BRESRT")
        self.LETC = QtWidgets.QLineEdit(self.centralwidget)
        self.LETC.setGeometry(QtCore.QRect(140, 10, 113, 31))
        self.LETC.setObjectName("LETC")
        self.LETC.setStyleSheet('''
            QLineEdit {
                border: 2px solid #98EECC;
                border-radius: 10px;
                padding: 5px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #0095F6;
            }
            QLineEdit::hover {
                border: 2px solid #B2B2B2;
            }
        ''')
        self.LETC.setText("Tp de cycle") 
        validator = QtGui.QIntValidator()
        self.LETC.setValidator(validator)

        self.REF = QtWidgets.QLineEdit(self.centralwidget)
        self.REF.setGeometry(QtCore.QRect(260, 10, 113, 31))
        self.REF.setObjectName("REF")
        self.REF.setStyleSheet('''
            QLineEdit {
                border: 2px solid #98EECC;
                border-radius: 10px;
                padding: 5px;
                font-size: 12px;
            }
            QLineEdit:focus {
                border: 2px solid #0095F6;
            }
            QLineEdit::hover {
                border: 2px solid #B2B2B2;
            }
        ''')
        self.REF.setText("Référence") 


        self.LENOB = QtWidgets.QLineEdit(self.centralwidget)
        self.LENOB.setGeometry(QtCore.QRect(140, 60, 113, 31))
        self.LENOB.setObjectName("LENOB")
        self.LENOB.setStyleSheet('''
            QLineEdit {
                border: 2px solid #98EECC;
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
        self.LENOB.setText("N°OP") 
        validator = QtGui.QIntValidator()
        self.LENOB.setValidator(validator)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(950, 70, 61, 20))
        self.label_2.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(1020, 70, 61, 20))
        self.label_3.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.BAfficher = QtWidgets.QPushButton(self.centralwidget)
        self.BAfficher.setGeometry(QtCore.QRect(880, 10, 51, 51))
        self.BAfficher.setStyleSheet("border-image: url(:/loggg/graphmagnifier_118081.png);")
        self.BAfficher.setText("")
        self.BAfficher.setObjectName("BAfficher")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(850, 110, 111, 20))
        self.label_9.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_9.setObjectName("label_8")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(880, 70, 71, 20))
        self.label_4.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(600, 110, 71, 20))
        self.label_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 110, 71, 20))
        self.label_6.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(25, 110, 71, 20))
        self.label_7.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(155, 110, 71, 20))
        self.label_8.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")

        self.C1 = QtWidgets.QLineEdit(self.centralwidget)
        self.C1.setGeometry(QtCore.QRect(720, 140, 361, 41))
        self.C1.setObjectName("C1")
        self.C1.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C3 = QtWidgets.QLineEdit(self.centralwidget)
        self.C3.setGeometry(QtCore.QRect(720, 240, 361, 41))
        self.C3.setObjectName("C3")
        self.C3.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C2 = QtWidgets.QLineEdit(self.centralwidget)
        self.C2.setGeometry(QtCore.QRect(720, 190, 361, 41))
        self.C2.setObjectName("C2")
        self.C2.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C4 = QtWidgets.QLineEdit(self.centralwidget)
        self.C4.setGeometry(QtCore.QRect(720, 290, 361, 41))
        self.C4.setObjectName("C4")
        self.C4.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C5 = QtWidgets.QLineEdit(self.centralwidget)
        self.C5.setGeometry(QtCore.QRect(720, 340, 361, 41))
        self.C5.setObjectName("C5")
        self.C5.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C6 = QtWidgets.QLineEdit(self.centralwidget)
        self.C6.setGeometry(QtCore.QRect(720, 390, 361, 41))
        self.C6.setObjectName("C6")
        self.C6.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C8 = QtWidgets.QLineEdit(self.centralwidget)
        self.C8.setGeometry(QtCore.QRect(720, 490, 361, 41))
        self.C8.setObjectName("C8")
        self.C8.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.C7 = QtWidgets.QLineEdit(self.centralwidget)
        self.C7.setGeometry(QtCore.QRect(720, 440, 361, 41))
        self.C7.setObjectName("C7")
        self.C7.setStyleSheet("color: rgb(85, 0, 255);\n"
"font: 75 12pt \"Times New Roman\";"
"border:1px solid rgba(0, 0, 0, 0);\n"
"border-bottom-color:rgba(46, 82, 101, 255);\n")
        self.CAD1 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD1.setGeometry(QtCore.QRect(140, 140, 111, 41))
        self.CAD1.setObjectName("CAD1")
        self.CAD1.setStyleSheet('''
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
        self.CAD1.setValidator(validator)
        self.CAD2 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD2.setGeometry(QtCore.QRect(140, 190, 111, 41))
        self.CAD2.setObjectName("CAD2")
        self.CAD2.setStyleSheet('''
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
        self.CAD2.setValidator(validator)
        self.CAD4 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD4.setGeometry(QtCore.QRect(140, 290, 111, 41))
        self.CAD4.setObjectName("CAD4")
        self.CAD4.setStyleSheet('''
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
        self.CAD4.setValidator(validator)
        self.CAD3 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD3.setGeometry(QtCore.QRect(140, 240, 111, 41))
        self.CAD3.setObjectName("CAD3")
        self.CAD3.setStyleSheet('''
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
        self.CAD3.setValidator(validator)
        self.CAD6 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD6.setGeometry(QtCore.QRect(140, 390, 111, 41))
        self.CAD6.setObjectName("CAD6")
        self.CAD6.setStyleSheet('''
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
        self.CAD6.setValidator(validator)
        self.CAD5 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD5.setGeometry(QtCore.QRect(140, 340, 111, 41))
        self.CAD5.setObjectName("CAD5")
        self.CAD5.setStyleSheet('''
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
        self.CAD5.setValidator(validator)
        self.CAD8 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD8.setGeometry(QtCore.QRect(140, 490, 111, 41))
        self.CAD8.setObjectName("CAD8")
        self.CAD8.setStyleSheet('''
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
        self.CAD8.setValidator(validator)
        self.CAD7 = QtWidgets.QLineEdit(self.centralwidget)
        self.CAD7.setGeometry(QtCore.QRect(140, 440, 111, 41))
        self.CAD7.setObjectName("CAD7")
        self.CAD7.setStyleSheet('''
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
        self.CAD7.setValidator(validator)
        self.H1 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H1.setGeometry(QtCore.QRect(10, 140, 118, 31))
        self.H1.setObjectName("H1")

        self.H2 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H2.setGeometry(QtCore.QRect(10, 190, 118, 31))
        self.H2.setObjectName("H2")
        self.H3 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H3.setGeometry(QtCore.QRect(10, 240, 118, 31))
        self.H3.setObjectName("H3")
        self.H4 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H4.setGeometry(QtCore.QRect(10, 290, 118, 31))
        self.H4.setObjectName("H4")
        self.H5 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H5.setGeometry(QtCore.QRect(10, 340, 118, 31))
        self.H5.setObjectName("H5")
        self.H6 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H6.setGeometry(QtCore.QRect(10, 390, 118, 31))
        self.H6.setObjectName("H6")
        self.H7 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H7.setGeometry(QtCore.QRect(10, 440, 118, 31))
        self.H7.setObjectName("H7")
        self.H8 = QtWidgets.QTimeEdit(self.centralwidget)
        self.H8.setGeometry(QtCore.QRect(10, 490, 118, 31))
        self.H8.setObjectName("H8")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(750, 70, 111, 20))
        self.label_12.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_12.setObjectName("label_7")
        self.BAfficher_2 = QtWidgets.QPushButton(self.centralwidget)
        self.BAfficher_2.setGeometry(QtCore.QRect(780, 10, 51, 51))
        self.BAfficher_2.setStyleSheet("border-image: url(:/loggg/maintenance256_24835.png);")
        self.BAfficher_2.setText("")
        self.BAfficher_2.setObjectName("BAfficher_2")
        self.REB = QtWidgets.QPushButton(self.centralwidget)
        self.REB.setGeometry(QtCore.QRect(685, 10, 51, 51))
        self.REB.setStyleSheet("border-image: url(:/loggg/attachment_79877.png);")
        self.REB.setText("")
        self.REB.setObjectName("RE")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(680, 70, 111, 20))
        self.label_18.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_18.setObjectName("label_18")
        Proddata.setCentralWidget(self.centralwidget)
        self.BRESRT.clicked.connect(self.clear_variables)
        self.BValider.clicked.connect(lambda: self.Tpréel(self.window))
        self.BAfficher.clicked.connect(self.DSB)
        self.BAfficher_2.clicked.connect(self.OpenM)
        self.REB.clicked.connect(self.OpenRebut)

        
        self.retranslateUi(Proddata)
        QtCore.QMetaObject.connectSlotsByName(Proddata)



    def retranslateUi(self, Proddata):
        _translate = QtCore.QCoreApplication.translate
        Proddata.setWindowTitle(_translate("Proddata", "Tableau de Marche"))
        self.label_2.setText(_translate("Proddata", "Valider"))
        self.label_3.setText(_translate("Proddata", "Rest"))
        self.label_4.setText(_translate("Proddata", "SAVE"))
        self.label_5.setText(_translate("Proddata", "PNOK"))
        self.label_6.setText(_translate("Proddata", "POK"))
        self.label_7.setText(_translate("Proddata", "Heure"))
        self.label_8.setText(_translate("Proddata", "Capacité"))
        self.label_9.setText(_translate("Proddata", "Commentaire"))
        self.label_12.setText(_translate("Proddata", "Intervention"))
        self.label_18.setText(_translate("Proddata", "Rebut"))
        self.CB1.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB1, state))
        self.CB2.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB2, state))
        self.cb3.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.cb3, state))
        self.CB4.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB4, state))
        self.CB5.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB5, state))
        self.CB6.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB6, state))
        self.CB7.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB7, state))
        self.CB8.stateChanged.connect(lambda state: self.handle_CB_state_changed(self.CB8, state))

    def handle_CB_state_changed(self, checkbox, state):
        line_edit = None

        if checkbox == self.CB1:
            line_edit = self.LEcad1
        elif checkbox == self.CB2:
            line_edit = self.LEcad2
        elif checkbox == self.cb3:
            line_edit = self.LEcad3
        elif checkbox == self.CB4:
            line_edit = self.LEcad4
        elif checkbox == self.CB5:
            line_edit = self.LEcad5
        elif checkbox == self.CB6:
            line_edit = self.LEcad6
        elif checkbox == self.CB7:
            line_edit = self.LEcad7
        elif checkbox == self.CB8:
            line_edit = self.LEcad8

        if line_edit:
            if state == QtCore.Qt.Checked:
                line_edit.setStyleSheet('''
                    QLineEdit {
                        background-color: #00DFA2;
                        border: 2px solid #00DFA2;
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
            else:
                line_edit.setStyleSheet('''
                    QLineEdit {
                        border: 2px solid #8696FE;
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
import akwel





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Proddata = QtWidgets.QMainWindow()
    ui = Ui_Proddata()
    ui.setupUi(Proddata, Proddata)  # Pass Proddata as the window argument
    Proddata.show()
    sys.exit(app.exec_())

