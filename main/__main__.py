from pathlib import Path
import sys

from PySide2 import QtWidgets

from .mainwindow import mainwindow
from .driverhardware import driverhardware
from .dataman import dataman
from .basefig import basefig

app = QtWidgets.QApplication([])
app.setStyle('Fusion')

drv = driverhardware()
dman = dataman(drv)
mfig = basefig(dman)

mwindow = mainwindow(app,dman,drv,mfig)

print("Uepa!")

mwindow.show()

sys.exit(app.exec_())
