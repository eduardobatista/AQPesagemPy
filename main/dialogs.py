
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
        self.cdialog.ui.bSave.clicked.connect(lambda: self.salvaconfigs(True))
        self.cdialog.closeEvent = self.closeEvent

    def showConfigDialog(self,driver,dman):
        self.driver = driver
        self.dman = dman   
        ports = driver.listPorts()
        self.cdialog.ui.comboSerial.clear()
        self.cdialog.ui.comboSerial.addItems(ports)   
        self.cdialog.ui.spinSampling.setValue(int(dman.samplingrate))
        self.cdialog.ui.spinTMax.setValue(int(dman.maxtime))
        self.cdialog.ui.comboSerial.setCurrentText(driver.serial.port)
        self.cdialog.ui.comboDevice.setCurrentText(driver.device)       
        self.cdialog.show()       

    def salvaconfigs(self,closeWindow=True):
        self.dman.samplingrate = self.cdialog.ui.spinSampling.value()
        self.dman.maxtime = self.cdialog.ui.spinTMax.value()
        self.driver.setPort(self.cdialog.ui.comboSerial.currentText())
        self.driver.setDevice(self.cdialog.ui.comboDevice.currentText())
        if closeWindow:
            self.cdialog.done(0)

    def closeEvent(self, event):
        self.salvaconfigs(closeWindow=False)
        event.accept()
