import sys
import sqlite3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QTableWidgetItem, 
    QStackedWidget
)

import MainWindowKursacha
import Clienti
import Postavhiki
import Prodazhi
import Tovari
import Zakaz



class Expample(QtWidgets.QMainWindow, MainWindowKursacha.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        



class Accidents(QtWidgets.QMainWindow,Postavhiki.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellAccidents)
        self.Add.clicked.connect(self.AddAccidents)
        self.Sort.clicked.connect(self.SortAccidents)
        self.Change.clicked.connect(self.ChangeAccidents)

    def test(self):

        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Postavshiki'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellAccidents(self):
           
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Postavshiki' WHERE ID_postav = ?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def AddAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Postavshiki' (naimenovanie,adres,kontact,Email) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def SortAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Postavshiki' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeAccidents(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Postavshiki' SET naimenovanie='{self.ChangeLine_1.text()}', adres='{self.ChangeLine_2.text()}', kontact='{self.ChangeLine_3.text()}', Email='{self.ChangeLine_4.text()}' WHERE ID_postav='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()

class Drivers(QtWidgets.QMainWindow,Prodazhi.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellDrivers)
        self.Add.clicked.connect(self.AddDrivers)
        self.Sort.clicked.connect(self.SortDrivers) 
        self.Change.clicked.connect(self.ChangeDrivers)
        
        
    
    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Prodazhi'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Prodazhi' WHERE ID_prodazhi =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Prodazhi' ('ID_klienta', 'ID_tovara', 'data_prodazhi', 'kolichestvo', 'stoimost') VALUES (?, ?, ?, ?, ?)",
                       (self.AddLine.text(), self.AddLine_1.text(), self.AddLine_2.text(), self.AddLine_3.text(), self.AddLine_4.text()))
                           
        self.connection.commit()
        self.connection.close()

    def SortDrivers(self):

        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Prodazhi' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()
        
        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    def ChangeDrivers(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Prodazhi' SET ID_klienta='{self.ChangeLine_1.text()}', ID_tovara='{self.ChangeLine_2.text()}', data_prodazhi='{self.ChangeLine_3.text()}', kolichestvo='{self.ChangeLine_4.text()}', stoimost='{self.ChangeLine_5.text()}' WHERE ID_prodazhi='{self.ChangeLine.text()}'")
        
        self.connection.commit()
        self.connection.close()

class Fuel(QtWidgets.QMainWindow,Zakaz.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test)
        self.Dell.clicked.connect(self.DellFuel)
        self.Add.clicked.connect(self.AddFuel)
        self.Sort.clicked.connect(self.SortFuel)
        self.Change.clicked.connect(self.ChangeFuel)
        

    def test(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Zakaz'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def DellFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Zakaz' WHERE ID_zakaza =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def AddFuel(self):

        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Zakaz' (ID_postav,ID_klienta,Data_zakaza,Data_dostavki,summa,status_zakaza) VALUES(?,?,?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),self.AddLine_4.text(),self.AddLine_5.text()))
        self.connection.commit()
        self.connection.close()

    def SortFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Zakaz' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeFuel(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Zakaz' SET ID_postav='{self.ChangeLine_1.text()}', ID_klienta='{self.ChangeLine_2.text()}', Data_zakaza='{self.ChangeLine_3.text()}', Data_dostavki='{self.ChangeLine_4.text()}', summa='{self.ChangeLine_5.text()}', status_zakaza='{self.ChangeLine_5.text()}' WHERE ID_zakaza='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Inspection(QtWidgets.QMainWindow,Clienti.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Dell.clicked.connect(self.DellInspection)
        self.Sort.clicked.connect(self.SortInspection)
        self.Add.clicked.connect(self.AddInspection)
        self.Change.clicked.connect(self.ChangeInspection)


    def test1(self):
        
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Clients'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def DellInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Clients' WHERE ID_klienta =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()

    def SortInspection(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Clients' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def AddInspection(self):

        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Clients' (FIO,Kontact,Email,Adress_klienta) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def ChangeInspection(self):
        
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Clients' SET FIO='{self.ChangeLine_1.text()}', Kontact='{self.ChangeLine_2.text()}', Email='{self.ChangeLine_3.text()}', Adress_klienta='{self.ChangeLine_4.text()}' WHERE ID_klienta='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()


class Mainstance(QtWidgets.QMainWindow,Tovari.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.Open.clicked.connect(self.test1)
        self.Add.clicked.connect(self.MainstanceAdd)
        self.Dell.clicked.connect(self.DellMainstance)
        self.Sort.clicked.connect(self.SortMainstance)
        self.Change.clicked.connect(self.ChangeMainstance)


    def test1(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("SELECT * FROM 'Tovari'")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()
    
    def MainstanceAdd(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("INSERT INTO 'Tovari' (naimenovanie,articul,cena,nalichie) VALUES(?,?,?,?)", (self.AddLine.text(), self.AddLine_1.text(),self.AddLine_2.text(),self.AddLine_3.text(),))
        self.connection.commit()
        self.connection.close()

    def DellMainstance(self):

        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("DELETE FROM 'Tovari' WHERE ID_tovara =?", (self.DellLine.text(),))
        self.connection.commit()
        self.connection.close()
    
    def SortMainstance(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"SELECT * FROM 'Tovari' ORDER BY {self.lineEdit_13.text()}")
        rows = self.cursor.fetchall()

        # получить список имен столбцов
        column_names = [i[0] for i in self.cursor.description]

        # добавить имена столбцов в первую строку таблицы
        self.tableWidget.setColumnCount(len(column_names))
        self.tableWidget.setRowCount(len(rows) + 1)
        for i, name in enumerate(column_names):
            item = QTableWidgetItem(name)
            self.tableWidget.setItem(0, i, item)

        # заполнить таблицу данными из запроса
        for i, row in enumerate(rows):
            for j, col in enumerate(row):
                item = QTableWidgetItem(str(col))
                self.tableWidget.setItem(i+1, j, item)

        self.connection.close()

    def ChangeMainstance(self):
        self.connection = sqlite3.connect("C:\\Users\\dpala\\OneDrive\\Рабочий стол\\kod\\db.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute(f"UPDATE 'Tovari' SET naimenovanie='{self.ChangeLine_1.text()}', articul='{self.ChangeLine_2.text()}', cena='{self.ChangeLine_3.text()}', nalichie='{self.ChangeLine_4.text()}' WHERE ID_tovara='{self.ChangeLine.text()}'")

        self.connection.commit()
        self.connection.close()







class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.stacked_widget = QStackedWidget()
        self.setCentralWidget(self.stacked_widget)



        self.example = Expample()
        self.accidents = Accidents()
        self.drivers = Drivers()
        self.fuel = Fuel()
        self.inspection = Inspection()
        self.maintenance = Mainstance()
        
        

        self.stacked_widget.addWidget(self.example)
        self.stacked_widget.addWidget(self.accidents)
        self.stacked_widget.addWidget(self.drivers)
        self.stacked_widget.addWidget(self.fuel)
        self.stacked_widget.addWidget(self.inspection)
        self.stacked_widget.addWidget(self.maintenance)
        
    

        self.example.AccidentsBtn.clicked.connect(self.show_accidents)
        self.accidents.Back.clicked.connect(self.show_example)
        self.example.DriversBtn.clicked.connect(self.show_drivers)
        self.drivers.Back.clicked.connect(self.show_example)
        self.example.FuelBtn.clicked.connect(self.show_fuel)
        self.fuel.Back.clicked.connect(self.show_example)
        self.example.InspectionsBtn.clicked.connect(self.show_inspection)
        self.inspection.Back.clicked.connect(self.show_example)
        self.example.MaintenanceBtn.clicked.connect(self.show_maintenance)
        self.maintenance.Back.clicked.connect(self.show_example)
        
        
        

    def show_example(self):
        self.stacked_widget.setCurrentWidget(self.example)

    def show_accidents(self):
        self.stacked_widget.setCurrentWidget(self.accidents)
    
    def show_drivers(self):
        self.stacked_widget.setCurrentWidget(self.drivers)
    
    def show_fuel(self):
        self.stacked_widget.setCurrentWidget(self.fuel)

    def show_inspection(self):
        self.stacked_widget.setCurrentWidget(self.inspection)
    
    def show_maintenance(self):
        self.stacked_widget.setCurrentWidget(self.maintenance)




if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
