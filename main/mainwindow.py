

from PySide2 import QtWidgets

from .aqpesagem import Ui_MainWindow
from .basefig import basefig
from .dataman import dataman
from .driverhardware import driverhardware
from .dialogs import configdialog

class mainwindow(QtWidgets.QMainWindow):    

    def __init__(self, app, dman : dataman, drv : driverhardware, mainfig : basefig):
        super(mainwindow, self).__init__()
        self.app = app
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.port = "COM3"
        self.driver = drv
        self.dman = dman
        self.mainfig = mainfig
        self.ui.plotLayout.addWidget(self.mainfig)
        self.statusMessage("Teste!")

        self.mainfig.setSamplingPeriod(1.0)
        self.mainfig.setTWindow(0,30)

        self.configdialog = configdialog()

        self.ui.bInit.clicked.connect(self.startreadings)
        self.ui.bReset.clicked.connect(self.reset)
        self.ui.bConfig.clicked.connect(self.config)
        self.dman.updateFigure.connect(self.updatePlot)

    def config(self):
        self.configdialog.showConfigDialog(self.driver)

    def statusMessage(self, msg):
        if msg is None:
            self.ui.statusbar.clearMessage()
        else:
            self.ui.statusbar.showMessage(msg) 

    def reset(self):
        self.dman.resetData()        
        self.mainfig.resetFigure()

    def updatePlot(self):
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
            self.ui.bInit.setText("Parar")
            for bt in [self.ui.bReset,self.ui.bSave,self.ui.bConfig]:
                bt.setEnabled(False)
            self.dman.startreadings()
            self.statusMessage(None)
            
        