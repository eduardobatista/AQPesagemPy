# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'aqpesagem.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(3, 3, 3, 3)
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout = QHBoxLayout(self.widget)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(3, 3, 3, 3)
        self.bInit = QPushButton(self.widget)
        self.bInit.setObjectName(u"bInit")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bInit.sizePolicy().hasHeightForWidth())
        self.bInit.setSizePolicy(sizePolicy)
        self.bInit.setMinimumSize(QSize(0, 30))
        font = QFont()
        font.setBold(True)
        self.bInit.setFont(font)

        self.horizontalLayout.addWidget(self.bInit)

        self.bReset = QPushButton(self.widget)
        self.bReset.setObjectName(u"bReset")
        sizePolicy.setHeightForWidth(self.bReset.sizePolicy().hasHeightForWidth())
        self.bReset.setSizePolicy(sizePolicy)
        self.bReset.setMinimumSize(QSize(0, 30))
        self.bReset.setFont(font)

        self.horizontalLayout.addWidget(self.bReset)

        self.bSave = QPushButton(self.widget)
        self.bSave.setObjectName(u"bSave")
        sizePolicy.setHeightForWidth(self.bSave.sizePolicy().hasHeightForWidth())
        self.bSave.setSizePolicy(sizePolicy)
        self.bSave.setMinimumSize(QSize(0, 30))
        self.bSave.setFont(font)

        self.horizontalLayout.addWidget(self.bSave)

        self.bConfig = QPushButton(self.widget)
        self.bConfig.setObjectName(u"bConfig")
        sizePolicy.setHeightForWidth(self.bConfig.sizePolicy().hasHeightForWidth())
        self.bConfig.setSizePolicy(sizePolicy)
        self.bConfig.setMinimumSize(QSize(0, 30))
        self.bConfig.setFont(font)

        self.horizontalLayout.addWidget(self.bConfig)


        self.verticalLayout.addWidget(self.widget)

        self.widget_3 = QWidget(self.centralwidget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_2.setSpacing(3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 3, 3, 3)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_3 = QLabel(self.widget_3)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.labelpeso = QLabel(self.widget_3)
        self.labelpeso.setObjectName(u"labelpeso")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.labelpeso.sizePolicy().hasHeightForWidth())
        self.labelpeso.setSizePolicy(sizePolicy1)
        self.labelpeso.setMinimumSize(QSize(100, 30))
        self.labelpeso.setFont(font)
        self.labelpeso.setFrameShape(QFrame.Box)
        self.labelpeso.setLineWidth(2)
        self.labelpeso.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labelpeso)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_4 = QLabel(self.widget_3)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_2.addWidget(self.label_4)

        self.labeltempo = QLabel(self.widget_3)
        self.labeltempo.setObjectName(u"labeltempo")
        self.labeltempo.setMinimumSize(QSize(100, 30))
        self.labeltempo.setFont(font)
        self.labeltempo.setFrameShape(QFrame.Box)
        self.labeltempo.setLineWidth(2)
        self.labeltempo.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.labeltempo)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addWidget(self.widget_3)

        self.plotwidget = QWidget(self.centralwidget)
        self.plotwidget.setObjectName(u"plotwidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.plotwidget.sizePolicy().hasHeightForWidth())
        self.plotwidget.setSizePolicy(sizePolicy2)
        self.plotLayout = QVBoxLayout(self.plotwidget)
        self.plotLayout.setSpacing(0)
        self.plotLayout.setObjectName(u"plotLayout")
        self.plotLayout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout.addWidget(self.plotwidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"AQPesagemPy", None))
        self.bInit.setText(QCoreApplication.translate("MainWindow", u"Iniciar", None))
        self.bReset.setText(QCoreApplication.translate("MainWindow", u"Reiniciar", None))
        self.bSave.setText(QCoreApplication.translate("MainWindow", u"Salvar...", None))
        self.bConfig.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7\u00f5es", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Peso:", None))
        self.labelpeso.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Tempo:", None))
        self.labeltempo.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

