import json
import numpy as np

from PySide2 import QtCore
from PySide2.QtWidgets import QWidgetAction,QWidget,QMenu

import pyqtgraph as pg
from pyqtgraph import GraphicsLayoutWidget

from .MainFigContextMenu import Ui_MainForm as MainFigContextMenu

class mainfig(GraphicsLayoutWidget):

    def __init__(self, dman, nplots=1, samplingperiod=1):        
        pg.setConfigOption("background", "w")
        pg.setConfigOption("foreground", "k")
        super().__init__()
        self.pitens = []
        for k in range(nplots):
            self.pitens.append(self.addPlot(row=k, col=0))
        for k,pi in enumerate(self.pitens):
            pi.setMenuEnabled(enableMenu=False, enableViewBoxMenu=True)
            pi.getViewBox().menu.clear()
            pi.getViewBox().menu = MyPersoMenu(self,k)
            pi.getMenu().clear()
            pi.showAxis('top')
            pi.getAxis('top').setStyle(showValues=False)
            pi.showAxis('right')
            pi.getAxis('right').setStyle(showValues=False)
            pi.hideButtons()                     
            pi.setClipToView(True)  
            pi.setMouseEnabled(x=False,y=True)    
        self.samplingperiod = samplingperiod
        self.janelax, self.miny, self.maxy, self.autoy, self.vetoreixox, self.npontosjanela = [], [], [], [], [], []
        for k in range(len(self.pitens)):
            self.janelax.append(5)
            self.miny.append(0)
            self.maxy.append(256)
            self.autoy.append(False)
            self.vetoreixox.append(0)
            self.npontosjanela.append(0)
        self.flagchangeranges = True
        for pi in self.pitens:
            pi.sigXRangeChanged.connect(self.sigXRangeChanged)
            pi.sigYRangeChanged.connect(self.sigYRangeChanged)

        pens = [pg.mkPen('r', width=1), pg.mkPen('b', width=1), pg.mkPen('g', width=1), pg.mkPen('y', width=1)]
        self.plotline = self.pitens[0].plot(np.array([]), np.array([]), pen=pens[k])

        self.pitens[0].setLabel('left','Peso (gramas)')
        self.pitens[0].setLabel('bottom','Tempo (últimos segundos)')

        self.dman = dman
        self.janelax[0] = 30.0
        self.sigXRangeChanged()
    
    def getMenu(self,plotid):
        return self.pitens[plotid].getViewBox().menu
    
    def resetFigure(self):
        for k, pitem in enumerate(self.pitens):
            self.pitens[k].setXRange(-self.janelax[k],0,padding=0.01)
            self.pitens[k].setMouseEnabled(x=False,y=True)
        self.updateFig()

    def sizeHint(self):
        if self.parent() is None:
            return QtCore.QSize(30, 30)
        else:
            return QtCore.QSize(self.parent().frameGeometry().width(), self.parent().frameGeometry().height())

    def setTWindow(self,plotid,newwindow):
        self.janelax[plotid] = float(newwindow)
        self.npontosjanela[plotid] = int(self.janelax[plotid] / self.samplingperiod)
        self.vetoreixox[plotid] = np.linspace(-self.janelax[plotid], 0, self.npontosjanela[plotid])
        self.pitens[plotid].setXRange(-self.janelax[plotid],0,padding=0.01)

    def setYRange(self,plotid,ylim1,ylim2):
        self.pitens[plotid].setYRange(ylim1,ylim2,padding=0.01)

    def sigYRangeChanged(self):
        for k, pi in enumerate(self.pitens):
            rgs = pi.viewRange()
            if self.flagchangeranges:
                self.miny[k] = rgs[1][0]
                self.maxy[k] = rgs[1][1]

    def sigXRangeChanged(self):
        for k, pi in enumerate(self.pitens):
            if self.flagchangeranges:
                self.janelax[k] = round(-pi.viewRange()[0][0])
            self.npontosjanela[k] = int(self.janelax[k] / self.samplingperiod)
            self.vetoreixox[k] = np.linspace(-self.janelax[k], 0, self.npontosjanela[k])

    def setSamplingPeriod(self,newsampling):
        self.samplingperiod = newsampling
        self.sigXRangeChanged()

    def getConfigString(self):
        mvars = vars(self)
        d = {}
        for k in ('janelax', 'miny', 'maxy', 'autoy'):
            d[k] = mvars[k]
        return json.dumps(d)

    def parseConfigString(self, strdata):
        d = json.loads(strdata)
        ll = len(d['janelax'])
        self.janelax[0:ll] = d['janelax']
        self.miny[0:ll] = d['miny']
        self.maxy[0:ll] = d['maxy']
        self.autoy[0:ll] = d['autoy']
        self.flagchangeranges = False
        for k, pi in enumerate(self.pitens):
            self.pitens[k].setXRange(-self.janelax[k], 0.0, padding=0.01)
            self.pitens[k].setYRange(self.miny[k], self.maxy[k], padding=0.01)
        self.flagchangeranges = True


    def updateFig(self):
        limi = 0
        limf = 0
        npontos = 0
       
        limi = self.dman.globalct - self.npontosjanela[0]
        limf = self.dman.globalct
        if limi < 0:
            limi = 0
            npontos = limf - limi
        else:
            npontos = self.npontosjanela[0]

        if npontos > 0:
            self.plotline.setData(self.vetoreixox[0][-npontos:], self.dman.pesodata[limi:limf])
            # self.plotline.setData(self.dman.timedata[limi:limf], self.dman.pesodata[limi:limf])
        else:
            self.plotline.setData([],[])



class MyPersoMenu(QMenu):

    def __init__(self,parent,plotid):
        super().__init__(parent)
        self.menuwidget = QWidget(self)        
        self.menuwidget.ui = MainFigContextMenu()
        self.menuwidget.ui.setupUi(self.menuwidget)
        self.mwaction = QWidgetAction(self)
        self.mwaction.setDefaultWidget(self.menuwidget)
        self.addAction(self.mwaction)

        self.plotid = plotid

        self.menuwidget.ui.spinTWindow.editingFinished.connect(self.windowChanged)
        self.menuwidget.ui.bviewall.clicked.connect(self.viewAll)
        self.menuwidget.ui.ylim1.editingFinished.connect(self.ylimChanged)
        self.menuwidget.ui.ylim2.editingFinished.connect(self.ylimChanged)

        self.aboutToShow.connect(self.getValues)

    def ylimChanged(self):
        try:
            ylim1 = float(self.menuwidget.ui.ylim1.text())
            ylim2 = float(self.menuwidget.ui.ylim2.text())
            if ylim1 > ylim2:
                self.getValues()
                return
            self.parentWidget().setYRange(self.plotid,ylim1,ylim2)
        except BaseException as ex:
            self.getValues()

    def windowChanged(self):
        self.parentWidget().setTWindow(self.plotid,self.menuwidget.ui.spinTWindow.value())
        self.hide()

    def getValues(self):
        self.menuwidget.ui.spinTWindow.setValue(self.parentWidget().janelax[self.plotid])
        rgs = self.parentWidget().pitens[self.plotid].viewRange()
        self.menuwidget.ui.ylim1.setText(f"{rgs[1][0]:.3f}")
        self.menuwidget.ui.ylim2.setText(f"{rgs[1][1]:.3f}")
        
    def viewAll(self):
        self.parentWidget().pitens[self.plotid].autoRange(padding=0.01)
        self.parentWidget().pitens[self.plotid].setXRange(-self.menuwidget.ui.spinTWindow.value(),0,padding=0.01)
        self.hide()
