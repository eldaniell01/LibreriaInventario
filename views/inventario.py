from PyQt6 import uic
import os
from openpyxl import load_workbook
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt6.QtGui import QFont

class Inventory(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main = uic.loadUi('views/inventario.ui')
        self.main.show()
        self.showTVenta()
        
    def showTVenta(self):
        columns = ['CANTIDAD', 'DESC. DEL PRODUCTO', 'MEDIDA', 'PRECIO COSTO', 'PRECIO VENTA']
        self.main.tablaVenta.setFont(QFont("Arial", 12))
        self.main.tablaVenta.setColumnCount(len(columns))
        for column, name in enumerate(columns):
            self.main.tablaVenta.setHorizontalHeaderItem(column, QTableWidgetItem(name))
        self.main.tablaVenta.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        header_style = """
        QHeaderView::section {
            font-family: "Arial";
            font-size: 12pt;
            font-weight: bold;
            background-color: rgb(255, 255, 255);
        }
        QTableWidget{
            background-color: rgb(255, 255, 255);
        }
        """
        self.main.tablaVenta.setStyleSheet(header_style)