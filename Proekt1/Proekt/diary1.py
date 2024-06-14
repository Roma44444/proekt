# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diary1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
import res_rc

class Ui_MainWindow_1(object):
    def setupUi(self, MainWindow_1):
        if not MainWindow_1.objectName():
            MainWindow_1.setObjectName(u"MainWindow_1")
        MainWindow_1.setEnabled(True)
        MainWindow_1.resize(280, 310)
        MainWindow_1.setMinimumSize(QSize(280, 310))
        MainWindow_1.setMaximumSize(QSize(280, 310))
        MainWindow_1.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u":/icons/icons/edit_note_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow_1.setWindowIcon(icon)
        MainWindow_1.setAutoFillBackground(False)
        MainWindow_1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:2, y1:1, stop:0 rgba(178, 34, 34, 255), stop:0.5 rgba(0, 0, 205, 255), stop:1 rgba(178, 34, 34, 255));")
        MainWindow_1.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonIconOnly)
        MainWindow_1.setAnimated(False)
        self.centralwidget = QWidget(MainWindow_1)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 261, 291))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pb_12 = QPushButton(self.frame)
        self.pb_12.setObjectName(u"pb_12")
        self.pb_12.setEnabled(True)
        self.pb_12.setGeometry(QRect(50, 220, 171, 31))
        self.pb_12.setMinimumSize(QSize(170, 31))
        self.pb_12.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/arrow_forward_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_12.setIcon(icon1)
        self.pb_12.setIconSize(QSize(24, 24))
        self.pb_11 = QPushButton(self.frame)
        self.pb_11.setObjectName(u"pb_11")
        self.pb_11.setEnabled(True)
        self.pb_11.setGeometry(QRect(50, 180, 171, 31))
        self.pb_11.setMinimumSize(QSize(170, 31))
        self.pb_11.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/login_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_11.setIcon(icon2)
        self.pb_11.setIconSize(QSize(24, 24))
        self.le_11 = QLineEdit(self.frame)
        self.le_11.setObjectName(u"le_11")
        self.le_11.setEnabled(True)
        self.le_11.setGeometry(QRect(50, 50, 170, 31))
        self.le_11.setMinimumSize(QSize(170, 31))
        self.le_11.setMaximumSize(QSize(10000000, 10000000))
        self.le_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")
        self.le_12 = QLineEdit(self.frame)
        self.le_12.setObjectName(u"le_12")
        self.le_12.setEnabled(True)
        self.le_12.setGeometry(QRect(50, 90, 171, 31))
        self.le_12.setMinimumSize(QSize(170, 31))
        self.le_12.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")
        self.pb_14 = QPushButton(self.frame)
        self.pb_14.setObjectName(u"pb_14")
        self.pb_14.setGeometry(QRect(190, 90, 31, 31))
        self.pb_14.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/visibility_off_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon3.addFile(u":/icons/icons/visibility_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pb_14.setIcon(icon3)
        self.pb_14.setIconSize(QSize(24, 24))
        self.pb_14.setCheckable(True)
        self.pb_13 = QPushButton(self.frame)
        self.pb_13.setObjectName(u"pb_13")
        self.pb_13.setGeometry(QRect(50, 130, 131, 31))
        self.pb_13.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/check_box_outline_blank_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon4.addFile(u":/icons/icons/check_box_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pb_13.setIcon(icon4)
        self.pb_13.setIconSize(QSize(24, 24))
        self.pb_13.setCheckable(True)
        self.lb_11 = QLabel(self.frame)
        self.lb_11.setObjectName(u"lb_11")
        self.lb_11.setEnabled(True)
        self.lb_11.setGeometry(QRect(10, 10, 241, 20))
        self.lb_11.setMinimumSize(QSize(50, 20))
        self.lb_11.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color:  rgba(255, 0, 0,255);\n"
"font-weight: bold;")
        MainWindow_1.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow_1)

        QMetaObject.connectSlotsByName(MainWindow_1)
    # setupUi

    def retranslateUi(self, MainWindow_1):
        MainWindow_1.setWindowTitle(QCoreApplication.translate("MainWindow_1", u"\u0429\u043e\u0434\u0435\u043d\u043d\u0438\u043a", None))
        self.pb_12.setText(QCoreApplication.translate("MainWindow_1", u"\u0417\u0430\u0440\u0435\u0454\u0441\u0442\u0440\u0443\u0432\u0430\u0442\u0438\u0441\u044f", None))
        self.pb_11.setText(QCoreApplication.translate("MainWindow_1", u"\u0423\u0432\u0456\u0439\u0442\u0438", None))
        self.le_11.setPlaceholderText(QCoreApplication.translate("MainWindow_1", u"\u041b\u043e\u0433\u0456\u043d", None))
        self.le_12.setPlaceholderText(QCoreApplication.translate("MainWindow_1", u"\u041f\u0430\u0440\u043e\u043b\u044c", None))
        self.pb_14.setText("")
        self.pb_13.setText(QCoreApplication.translate("MainWindow_1", u"\u0410\u0432\u0442\u043e\u0437\u0430\u043f\u043e\u0432\u043d\u0435\u043d\u043d\u044f", None))
        self.lb_11.setText(QCoreApplication.translate("MainWindow_1", u"\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432\u0432", None))
    # retranslateUi

