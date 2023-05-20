
import time
from threading import Thread

import numpy as np

from PySide2.QtCore import Signal,QObject

class dataman(QObject):

    updateFigure = Signal()

    def __init__(self,drv):
        super().__init__()
        self.driver = drv
        self.flagstop = False
        self.reading = False
        self.samplingrate = 1 # segundos
        self.maxtime = 60 # minutos
        self.wsize = 10 # segundos
        self.maxpontos = self.maxtime * 60 / self.samplingrate
        self.pesodata = np.zeros(int(self.maxpontos)) 
        self.timedata = np.zeros(int(self.maxpontos))

    def resetData(self):
        self.pesodata = np.zeros(int(self.maxpontos)) 
        self.timedata = np.zeros(int(self.maxpontos))
        self.globalctreadings = 0

    def stopreadings(self):
        self.flagstop = True

    def startreadings(self):
        self.flagstop = False
        self.reading = True        
        self.mythread = Thread(target=self.readData)
        self.mythread.start()

    def readData(self):
        self.globalctreadings = 0
        while (not self.flagstop):
            val = self.driver.lepeso()
            self.pesodata[self.globalctreadings] = val
            self.globalctreadings += 1
            print(val)
            self.updateFigure.emit()
            time.sleep(1)
        self.reading = False
        print("Finished reading!")