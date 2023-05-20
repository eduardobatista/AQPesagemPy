
import typing
import PySide2.QtCore
from .ConfigDialog import Ui_Dialog as configdialog

from PySide2 import QtCore
from PySide2.QtWidgets import QDialog

from .ConfigDialog import Ui_Dialog as CDialog

class configdialog(QtCore.QObject):

    def __init__(self) -> None:
        super().__init__()
        self.cdialog = QDialog()
        self.cdialog.ui = CDialog()
        self.cdialog.ui.setupUi(self.cdialog)
        self.cdialog.ui.bSave.clicked.connect(self.salvaconfigs)

    def showConfigDialog(self,driver):   
        ports = driver.listPorts()
        print(ports)
        # self.cdialog.ui.comboSerial.clear()
        self.cdialog.ui.comboSerial.addItems(ports)          
        self.cdialog.exec_()
    
    def salvaconfigs(self):
        print("Uepa!")
