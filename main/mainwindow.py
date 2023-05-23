import math

from PySide2 import QtWidgets,QtCore

from .aqpesagem import Ui_MainWindow
from .mainfig import mainfig
from .dataman import dataman
from .driverhardware import driverhardware
from .dialogs import configdialog

class mainwindow(QtWidgets.QMainWindow):    

    def __init__(self, app, dman : dataman, drv : driverhardware, mainfig : mainfig):
        super(mainwindow, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.port = "COM3"
        self.driver = drv
        self.dman = dman
        self.mainfig = mainfig
        self.ui.plotLayout.addWidget(self.mainfig)

        self.mainfig.setSamplingPeriod(1.0)
        self.mainfig.setTWindow(0,30)

        self.configdialog = configdialog()

        self.readconfigs()

        self.ui.bInit.clicked.connect(self.startreadings)
        self.ui.bReset.clicked.connect(self.reset)
        self.ui.bConfig.clicked.connect(self.config)
        self.dman.updateUi.connect(self.updateUi)
        self.dman.updateStatus.connect(self.statusMessage)

    def writeconfigs(self):
        settings = QtCore.QSettings("AQPesagem", "AQPesagem")
        settings.setValue("port", self.driver.serial.port)
        settings.setValue("device", self.driver.device)
        settings.setValue("samplingrate", self.dman.samplingrate)
        settings.setValue("maxtime", self.dman.maxtime)
    
    def readconfigs(self):
        settings = QtCore.QSettings("AQPesagem", "AQPesagem")
        if (settings.value("port") is not None):
            self.driver.setPort(settings.value("port"))
        if (settings.value("device") is not None):
            self.driver.setDevice(settings.value("device"))
        if (settings.value("samplingrate") is not None):
            self.dman.samplingrate = int(settings.value("samplingrate"))
        if (settings.value("maxtime") is not None):
            self.dman.maxtime = int(settings.value("maxtime"))
        self.dman.resetData()

    def config(self):
        self.configdialog.showConfigDialog(self.driver,self.dman)

    def statusMessage(self, msg):
        if msg is None:
            self.ui.statusbar.clearMessage()
        else:
            self.ui.statusbar.showMessage(msg) 

    def reset(self):
        self.dman.resetData()        
        self.mainfig.resetFigure()
        self.statusMessage(None)

    def updateUi(self):
        if math.isnan(self.dman.pesoatual):
            self.ui.labelpeso.setText("--")
        else:
            self.ui.labelpeso.setText(f"{self.dman.pesoatual} g")
        self.ui.labeltempo.setText(f"{self.dman.lastreadtime:.0f} s")
        self.mainfig.updateFig()

    def startreadings(self):
        if self.dman.reading:
            self.dman.stopreadings()
            for bt in [self.ui.bReset,self.ui.bSave,self.ui.bConfig]:
                bt.setEnabled(True)
            self.ui.bReset.setEnabled(True)
            self.ui.bSave.setEnabled(True)
            self.ui.bInit.setText("Iniciar")
        else:            
            try:
                self.dman.startreadings()
                self.ui.bInit.setText("Parar")
                for bt in [self.ui.bReset,self.ui.bSave,self.ui.bConfig]:
                    bt.setEnabled(False)
                self.statusMessage(None)
            except BaseException as ex:
                self.statusMessage(str(ex))

    def closeEvent(self, event) -> None:
        if self.dman.reading == True:
            self.statusMessage("Pare o experimento antes de fechar o programa.")
            event.ignore()
        else:
            self.writeconfigs()
            event.accept()          
        