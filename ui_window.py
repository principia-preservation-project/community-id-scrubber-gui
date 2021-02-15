# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'windowUtdNsd.ui'
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
        MainWindow.resize(450, 180)
        icon = QIcon()
        icon.addFile(u"icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QSize(22, 22))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.backup_checkbox = QCheckBox(self.centralwidget)
        self.backup_checkbox.setObjectName(u"backup_checkbox")
        self.backup_checkbox.setGeometry(QRect(50, 60, 381, 22))
        self.backup_checkbox.setStyleSheet(u"width: 100%;")
        self.backup_checkbox.setChecked(True)
        self.go_button = QPushButton(self.centralwidget)
        self.go_button.setObjectName(u"go_button")
        self.go_button.setGeometry(QRect(10, 100, 431, 51))
        self.path_input = QLineEdit(self.centralwidget)
        self.path_input.setObjectName(u"path_input")
        self.path_input.setGeometry(QRect(10, 10, 331, 32))
        self.browse_button = QPushButton(self.centralwidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setGeometry(QRect(350, 10, 91, 34))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        self.statusBar.setEnabled(True)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Community ID Scrubber", None))
        self.backup_checkbox.setText(QCoreApplication.translate("MainWindow", u"Back up original level file (Recommended)", None))
        self.go_button.setText(QCoreApplication.translate("MainWindow", u"Scrub!", None))
        self.path_input.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Level File", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Browse...", None))
    # retranslateUi

