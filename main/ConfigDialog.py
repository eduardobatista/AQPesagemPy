# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'configdialog.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(400, 144)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(6, 6, 6, 6)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)

        self.spinSampling = QSpinBox(Dialog)
        self.spinSampling.setObjectName(u"spinSampling")
        self.spinSampling.setMinimum(1)
        self.spinSampling.setMaximum(30)

        self.gridLayout.addWidget(self.spinSampling, 1, 1, 1, 1)

        self.comboSerial = QComboBox(Dialog)
        self.comboSerial.addItem("")
        self.comboSerial.addItem("")
        self.comboSerial.setObjectName(u"comboSerial")

        self.gridLayout.addWidget(self.comboSerial, 3, 1, 1, 1)

        self.spinTMax = QSpinBox(Dialog)
        self.spinTMax.setObjectName(u"spinTMax")
        self.spinTMax.setMinimum(360)
        self.spinTMax.setMaximum(1440)
        self.spinTMax.setSingleStep(60)

        self.gridLayout.addWidget(self.spinTMax, 2, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.comboDevice = QComboBox(Dialog)
        self.comboDevice.addItem("")
        self.comboDevice.addItem("")
        self.comboDevice.addItem("")
        self.comboDevice.setObjectName(u"comboDevice")

        self.gridLayout.addWidget(self.comboDevice, 4, 1, 1, 1)

        self.bSave = QPushButton(Dialog)
        self.bSave.setObjectName(u"bSave")

        self.gridLayout.addWidget(self.bSave, 5, 0, 1, 2)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Configura\u00e7\u00f5es", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Dispositivo:", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Porta Serial:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Tempo m\u00e1ximo de experimento:", None))
        self.spinSampling.setSuffix(QCoreApplication.translate("Dialog", u" seg", None))
        self.comboSerial.setItemText(0, QCoreApplication.translate("Dialog", u"COM3", None))
        self.comboSerial.setItemText(1, QCoreApplication.translate("Dialog", u"/dev/ttyUSB0", None))

        self.spinTMax.setSuffix(QCoreApplication.translate("Dialog", u" min", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Amostragem:", None))
        self.comboDevice.setItemText(0, QCoreApplication.translate("Dialog", u"3101C", None))
        self.comboDevice.setItemText(1, QCoreApplication.translate("Dialog", u"3102", None))
        self.comboDevice.setItemText(2, QCoreApplication.translate("Dialog", u"LD1050", None))

        self.bSave.setText(QCoreApplication.translate("Dialog", u"Salvar Configura\u00e7\u00f5es", None))
    # retranslateUi

