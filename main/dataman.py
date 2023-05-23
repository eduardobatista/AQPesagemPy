import time
from threading import Thread

import numpy as np

from PySide2.QtCore import Signal,QObject

from .driverhardware import driverhardware

class dataman(QObject):

    updateUi = Signal()
    updateStatus = Signal(str)

    def __init__(self, drv : driverhardware):
        super().__init__()
        self.driver = drv
        self.flagstop = False
        self.reading = False
        self.samplingrate = 1 # segundos
        self.maxtime = 60 # minutos
        self.resetData()

    def resetData(self):
        self.maxpontos = self.maxtime * 60 / self.samplingrate
        self.Ts = 1/self.samplingrate
        self.pesodata = np.zeros(int(self.maxpontos)) 
        self.timedata = np.zeros(int(self.maxpontos))
        self.pesoatual = 0.0
        self.globalct = 0
        self.startime = None
        self.lastreadtime = 0

    def setSamplingRate(self,srate):
        self.samplingrate = srate
        self.resetData()

    def stopreadings(self):
        self.flagstop = True

    def startreadings(self):    
        self.driver.openPort()
        self.driver.lepeso()
        self.flagstop = False
        self.reading = True        
        self.mythread = Thread(target=self.readData)
        self.mythread.start()


    def readData(self):

        lastwaserror = False

        if not self.startime:
            self.startime = time.time()
            self.nextsample = self.startime + self.Ts
        else:
            nnullsamples = int(np.ceil((time.time() - self.nextsample)/self.Ts))
            for k in range(nnullsamples):
                self.timedata[self.globalct] = self.lastreadtime + (k+1)*self.Ts
                self.pesoatual = float('nan')
                self.pesodata[self.globalct] = self.pesoatual
                self.globalct += 1
            self.nextsample = self.nextsample + nnullsamples*self.Ts

        while (not self.flagstop):

            slptime = self.nextsample - time.time()            
            if slptime > 0:
                time.sleep(slptime) 
            self.nextsample = self.nextsample + self.Ts
            
            self.lastreadtime = round(time.time() - self.startime,2)
            self.timedata[self.globalct] = self.lastreadtime
            try:
                self.pesoatual = self.driver.lepeso()
                if lastwaserror ==  True:
                    self.updateStatus.emit("")
                    lastwaserror = False
            except BaseException as ex:
                self.pesoatual = float('nan')
                self.updateStatus.emit(str(ex))
                lastwaserror = True
            self.pesodata[self.globalct] = self.pesoatual
            self.globalct += 1
            self.updateUi.emit()


        self.driver.closePort()
        self.reading = False
        self.updateStatus.emit("Leituras finalizadas.")