import sys
from PyQt6.QtWidgets import QApplication
from views.inventario import Inventory


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Inventory()
    
    sys.exit(app.exec()) 