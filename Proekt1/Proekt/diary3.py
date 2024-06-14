# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diary3.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QDialog,
    QFrame, QGridLayout, QHBoxLayout, QLabel,
    QLayout, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)
import res_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(280, 411)
        Dialog.setMinimumSize(QSize(280, 360))
        Dialog.setMaximumSize(QSize(280, 16777215))
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:2, y1:1, stop:0 rgba(178, 34, 34, 255), stop:0.5 rgba(0, 0, 205, 255), stop:1 rgba(178, 34, 34, 255));")
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setEnabled(True)
        self.frame.setMaximumSize(QSize(16777208, 16777215))
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.pb_32 = QPushButton(self.frame)
        self.pb_32.setObjectName(u"pb_32")
        self.pb_32.setEnabled(True)
        self.pb_32.setGeometry(QRect(20, 350, 221, 31))
        self.pb_32.setMinimumSize(QSize(170, 31))
        self.pb_32.setStyleSheet(u"QPushButton{\n"
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
        icon = QIcon()
        icon.addFile(u":/icons/icons/arrow_back_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_32.setIcon(icon)
        self.pb_32.setIconSize(QSize(24, 24))
        self.pb_31 = QPushButton(self.frame)
        self.pb_31.setObjectName(u"pb_31")
        self.pb_31.setGeometry(QRect(10, 309, 241, 31))
        self.pb_31.setMinimumSize(QSize(0, 30))
        self.pb_31.setStyleSheet(u"QPushButton{\n"
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
        icon1.addFile(u":/icons/icons/file_open_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_31.setIcon(icon1)
        self.pb_31.setIconSize(QSize(24, 24))
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 221, 22))
        self.horizontalLayout_2 = QHBoxLayout(self.widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.de_31 = QDateEdit(self.widget)
        self.de_31.setObjectName(u"de_31")
        self.de_31.setEnabled(True)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.de_31.sizePolicy().hasHeightForWidth())
        self.de_31.setSizePolicy(sizePolicy)
        self.de_31.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")
        self.de_31.setDateTime(QDateTime(QDate(2024, 1, 2), QTime(0, 0, 0)))
        self.de_31.setMaximumDate(QDate(9999, 12, 31))

        self.horizontalLayout_2.addWidget(self.de_31)

        self.lb_31 = QLabel(self.frame)
        self.lb_31.setObjectName(u"lb_31")
        self.lb_31.setEnabled(True)
        self.lb_31.setGeometry(QRect(20, 40, 221, 20))
        self.lb_31.setMinimumSize(QSize(15, 20))
        self.lb_31.setMaximumSize(QSize(16777215, 20))
        self.lb_31.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"color:  rgba(255, 0, 0,255);\n"
"font-weight: bold;")
        self.widget1 = QWidget(self.frame)
        self.widget1.setObjectName(u"widget1")
        self.widget1.setGeometry(QRect(20, 70, 221, 24))
        self.horizontalLayout_5 = QHBoxLayout(self.widget1)
        self.horizontalLayout_5.setSpacing(9)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(7, 3, 6, 3)
        self.label_12 = QLabel(self.widget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMaximumSize(QSize(16777215, 20))
        self.label_12.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 0);\n"
"\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_5.addWidget(self.label_12)

        self.cb_31 = QComboBox(self.widget1)
        self.cb_31.addItem("")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/sentiment_very_satisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/mood_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/sentiment_satisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/sentiment_neutral_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/sentiment_frustrated_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/sentiment_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/mood_bad_24dp_FILL0_wght400_GRAD0_opsz24 (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/sentiment_extremely_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon9, "")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/sentiment_very_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.cb_31.addItem(icon10, "")
        self.cb_31.setObjectName(u"cb_31")
        self.cb_31.setMaximumSize(QSize(55, 30))
        self.cb_31.setAcceptDrops(False)
        self.cb_31.setToolTipDuration(-1)
        self.cb_31.setStyleSheet(u"color: white;\n"
"font-weight: bold;")
        self.cb_31.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.cb_31.setIconSize(QSize(16, 16))

        self.horizontalLayout_5.addWidget(self.cb_31)

        self.pb_35 = QPushButton(self.widget1)
        self.pb_35.setObjectName(u"pb_35")
        self.pb_35.setMinimumSize(QSize(0, 0))
        self.pb_35.setMaximumSize(QSize(17, 17))
        self.pb_35.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 0);\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/check_box_outline_blank_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon11.addFile(u":/icons/icons/check_box_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.On)
        self.pb_35.setIcon(icon11)
        self.pb_35.setIconSize(QSize(16, 16))
        self.pb_35.setCheckable(True)

        self.horizontalLayout_5.addWidget(self.pb_35)

        self.widget2 = QWidget(self.frame)
        self.widget2.setObjectName(u"widget2")
        self.widget2.setGeometry(QRect(20, 100, 221, 201))
        self.verticalLayout_2 = QVBoxLayout(self.widget2)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 3)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(26)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout_4.setContentsMargins(2, 2, 2, 2)
        self.pb_33 = QPushButton(self.widget2)
        self.pb_33.setObjectName(u"pb_33")
        self.pb_33.setMaximumSize(QSize(16777215, 20))
        self.pb_33.setStyleSheet(u"QPushButton{\n"
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
        self.pb_33.setIcon(icon)

        self.horizontalLayout_4.addWidget(self.pb_33)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(1)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_32 = QLabel(self.widget2)
        self.lb_32.setObjectName(u"lb_32")
        self.lb_32.setMaximumSize(QSize(16777215, 20))
        self.lb_32.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.lb_32)

        self.lb_33 = QLabel(self.widget2)
        self.lb_33.setObjectName(u"lb_33")
        self.lb_33.setMaximumSize(QSize(16777215, 20))
        self.lb_33.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout_3.addWidget(self.lb_33)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.pb_34 = QPushButton(self.widget2)
        self.pb_34.setObjectName(u"pb_34")
        self.pb_34.setMaximumSize(QSize(16777215, 20))
        self.pb_34.setStyleSheet(u"QPushButton{\n"
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
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/arrow_forward_ios_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_34.setIcon(icon12)

        self.horizontalLayout_4.addWidget(self.pb_34)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetFixedSize)
        self.horizontalLayout.setContentsMargins(5, 0, 4, 0)
        self.label_4 = QLabel(self.widget2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(16777215, 20))
        self.label_4.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_4)

        self.label_10 = QLabel(self.widget2)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMaximumSize(QSize(16777215, 20))
        self.label_10.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_10)

        self.label_9 = QLabel(self.widget2)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMaximumSize(QSize(16777215, 20))
        self.label_9.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_9)

        self.label_8 = QLabel(self.widget2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMaximumSize(QSize(16777215, 20))
        self.label_8.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_8)

        self.label_6 = QLabel(self.widget2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMaximumSize(QSize(16777215, 20))
        self.label_6.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_6)

        self.label_5 = QLabel(self.widget2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(16777215, 20))
        self.label_5.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_5)

        self.label_11 = QLabel(self.widget2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setMaximumSize(QSize(16777215, 20))
        self.label_11.setStyleSheet(u"\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")

        self.horizontalLayout.addWidget(self.label_11)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(5, -1, 5, -1)
        self.pb_t1 = QPushButton(self.widget2)
        self.pb_t1.setObjectName(u"pb_t1")
        self.pb_t1.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t1.setCheckable(True)
        self.pb_t1.setChecked(False)
        self.pb_t1.setAutoRepeat(False)
        self.pb_t1.setAutoExclusive(False)

        self.gridLayout.addWidget(self.pb_t1, 0, 0, 1, 1)

        self.pb_t2 = QPushButton(self.widget2)
        self.pb_t2.setObjectName(u"pb_t2")
        self.pb_t2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t2.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t2, 0, 1, 1, 1)

        self.pb_t3 = QPushButton(self.widget2)
        self.pb_t3.setObjectName(u"pb_t3")
        self.pb_t3.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t3.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t3, 0, 2, 1, 1)

        self.pb_t4 = QPushButton(self.widget2)
        self.pb_t4.setObjectName(u"pb_t4")
        self.pb_t4.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t4.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t4, 0, 3, 1, 1)

        self.pb_t5 = QPushButton(self.widget2)
        self.pb_t5.setObjectName(u"pb_t5")
        self.pb_t5.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t5.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t5, 0, 4, 1, 1)

        self.pb_t6 = QPushButton(self.widget2)
        self.pb_t6.setObjectName(u"pb_t6")
        self.pb_t6.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t6.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t6, 0, 5, 1, 1)

        self.pb_t7 = QPushButton(self.widget2)
        self.pb_t7.setObjectName(u"pb_t7")
        self.pb_t7.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t7.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t7, 0, 6, 1, 1)

        self.pb_t8 = QPushButton(self.widget2)
        self.pb_t8.setObjectName(u"pb_t8")
        self.pb_t8.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t8.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t8, 1, 0, 1, 1)

        self.pb_t9 = QPushButton(self.widget2)
        self.pb_t9.setObjectName(u"pb_t9")
        self.pb_t9.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t9.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t9, 1, 1, 1, 1)

        self.pb_t10 = QPushButton(self.widget2)
        self.pb_t10.setObjectName(u"pb_t10")
        self.pb_t10.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t10.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t10, 1, 2, 1, 1)

        self.pb_t11 = QPushButton(self.widget2)
        self.pb_t11.setObjectName(u"pb_t11")
        self.pb_t11.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t11.setCheckable(True)
        self.pb_t11.setChecked(False)

        self.gridLayout.addWidget(self.pb_t11, 1, 3, 1, 1)

        self.pb_t12 = QPushButton(self.widget2)
        self.pb_t12.setObjectName(u"pb_t12")
        self.pb_t12.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t12.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t12, 1, 4, 1, 1)

        self.pb_t13 = QPushButton(self.widget2)
        self.pb_t13.setObjectName(u"pb_t13")
        self.pb_t13.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t13.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t13, 1, 5, 1, 1)

        self.pb_t14 = QPushButton(self.widget2)
        self.pb_t14.setObjectName(u"pb_t14")
        self.pb_t14.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t14.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t14, 1, 6, 1, 1)

        self.pb_t15 = QPushButton(self.widget2)
        self.pb_t15.setObjectName(u"pb_t15")
        self.pb_t15.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t15.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t15, 2, 0, 1, 1)

        self.pb_t16 = QPushButton(self.widget2)
        self.pb_t16.setObjectName(u"pb_t16")
        self.pb_t16.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t16.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t16, 2, 1, 1, 1)

        self.pb_t17 = QPushButton(self.widget2)
        self.pb_t17.setObjectName(u"pb_t17")
        self.pb_t17.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t17.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t17, 2, 2, 1, 1)

        self.pb_t18 = QPushButton(self.widget2)
        self.pb_t18.setObjectName(u"pb_t18")
        self.pb_t18.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t18.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t18, 2, 3, 1, 1)

        self.pb_t19 = QPushButton(self.widget2)
        self.pb_t19.setObjectName(u"pb_t19")
        self.pb_t19.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t19.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t19, 2, 4, 1, 1)

        self.pb_t20 = QPushButton(self.widget2)
        self.pb_t20.setObjectName(u"pb_t20")
        self.pb_t20.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t20.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t20, 2, 5, 1, 1)

        self.pb_t21 = QPushButton(self.widget2)
        self.pb_t21.setObjectName(u"pb_t21")
        self.pb_t21.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t21.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t21, 2, 6, 1, 1)

        self.pb_t22 = QPushButton(self.widget2)
        self.pb_t22.setObjectName(u"pb_t22")
        self.pb_t22.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t22.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t22, 3, 0, 1, 1)

        self.pb_t23 = QPushButton(self.widget2)
        self.pb_t23.setObjectName(u"pb_t23")
        self.pb_t23.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t23.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t23, 3, 1, 1, 1)

        self.pb_t24 = QPushButton(self.widget2)
        self.pb_t24.setObjectName(u"pb_t24")
        self.pb_t24.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t24.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t24, 3, 2, 1, 1)

        self.pb_t25 = QPushButton(self.widget2)
        self.pb_t25.setObjectName(u"pb_t25")
        self.pb_t25.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t25.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t25, 3, 3, 1, 1)

        self.pb_t26 = QPushButton(self.widget2)
        self.pb_t26.setObjectName(u"pb_t26")
        self.pb_t26.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t26.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t26, 3, 4, 1, 1)

        self.pb_t27 = QPushButton(self.widget2)
        self.pb_t27.setObjectName(u"pb_t27")
        self.pb_t27.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t27.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t27, 3, 5, 1, 1)

        self.pb_t28 = QPushButton(self.widget2)
        self.pb_t28.setObjectName(u"pb_t28")
        self.pb_t28.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t28.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t28, 3, 6, 1, 1)

        self.pb_t29 = QPushButton(self.widget2)
        self.pb_t29.setObjectName(u"pb_t29")
        self.pb_t29.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t29.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t29, 4, 0, 1, 1)

        self.pb_t30 = QPushButton(self.widget2)
        self.pb_t30.setObjectName(u"pb_t30")
        self.pb_t30.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t30.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t30, 4, 1, 1, 1)

        self.pb_t31 = QPushButton(self.widget2)
        self.pb_t31.setObjectName(u"pb_t31")
        self.pb_t31.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t31.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t31, 4, 2, 1, 1)

        self.pb_t32 = QPushButton(self.widget2)
        self.pb_t32.setObjectName(u"pb_t32")
        self.pb_t32.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t32.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t32, 4, 3, 1, 1)

        self.pb_t33 = QPushButton(self.widget2)
        self.pb_t33.setObjectName(u"pb_t33")
        self.pb_t33.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t33.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t33, 4, 4, 1, 1)

        self.pb_t34 = QPushButton(self.widget2)
        self.pb_t34.setObjectName(u"pb_t34")
        self.pb_t34.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t34.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t34, 4, 5, 1, 1)

        self.pb_t35 = QPushButton(self.widget2)
        self.pb_t35.setObjectName(u"pb_t35")
        self.pb_t35.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t35.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t35, 4, 6, 1, 1)

        self.pb_t36 = QPushButton(self.widget2)
        self.pb_t36.setObjectName(u"pb_t36")
        self.pb_t36.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t36.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t36, 5, 0, 1, 1)

        self.pb_t37 = QPushButton(self.widget2)
        self.pb_t37.setObjectName(u"pb_t37")
        self.pb_t37.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t37.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t37, 5, 1, 1, 1)

        self.pb_t38 = QPushButton(self.widget2)
        self.pb_t38.setObjectName(u"pb_t38")
        self.pb_t38.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t38.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t38, 5, 2, 1, 1)

        self.pb_t39 = QPushButton(self.widget2)
        self.pb_t39.setObjectName(u"pb_t39")
        self.pb_t39.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t39.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t39, 5, 3, 1, 1)

        self.pb_t40 = QPushButton(self.widget2)
        self.pb_t40.setObjectName(u"pb_t40")
        self.pb_t40.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t40.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t40, 5, 4, 1, 1)

        self.pb_t41 = QPushButton(self.widget2)
        self.pb_t41.setObjectName(u"pb_t41")
        self.pb_t41.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t41.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t41, 5, 5, 1, 1)

        self.pb_t42 = QPushButton(self.widget2)
        self.pb_t42.setObjectName(u"pb_t42")
        self.pb_t42.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 5px;\n"
"color: white;\n"
"font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255, 255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255, 255, 255, 70);\n"
"}")
        self.pb_t42.setCheckable(True)

        self.gridLayout.addWidget(self.pb_t42, 5, 6, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0429\u043e\u0434\u0435\u043d\u043d\u0438\u043a", None))
        self.pb_32.setText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0430\u0434", None))
        self.pb_31.setText(QCoreApplication.translate("Dialog", u"\u0412\u0456\u0434\u043a\u0440\u0438\u0442\u0438 \u043e\u0431\u0440\u0430\u043d\u0443 \u0434\u0430\u0442\u0443", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0412\u0432\u0435\u0434\u0456\u0442 \u043f\u043e\u0442\u0440\u0456\u0431\u043d\u0443 \u0434\u0430\u0442\u0443:", None))
        self.lb_31.setText(QCoreApplication.translate("Dialog", u"asdasdasdddddddddddddddddddddddd", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u0428\u0443\u043a\u0430\u0442\u0438 \u0437\u0430 \u043d\u0430\u0441\u0442\u0440\u043e\u0454\u043c:", None))
        self.cb_31.setItemText(0, "")
        self.cb_31.setItemText(1, QCoreApplication.translate("Dialog", u"    1", None))
        self.cb_31.setItemText(2, QCoreApplication.translate("Dialog", u"    2", None))
        self.cb_31.setItemText(3, QCoreApplication.translate("Dialog", u"    3", None))
        self.cb_31.setItemText(4, QCoreApplication.translate("Dialog", u"    4", None))
        self.cb_31.setItemText(5, QCoreApplication.translate("Dialog", u"    5", None))
        self.cb_31.setItemText(6, QCoreApplication.translate("Dialog", u"    6", None))
        self.cb_31.setItemText(7, QCoreApplication.translate("Dialog", u"    7", None))
        self.cb_31.setItemText(8, QCoreApplication.translate("Dialog", u"    8", None))
        self.cb_31.setItemText(9, QCoreApplication.translate("Dialog", u"    9", None))

        self.pb_35.setText("")
        self.pb_33.setText("")
        self.lb_32.setText(QCoreApplication.translate("Dialog", u"\u0412\u0435\u0440\u0435\u0441\u0435\u043d\u044c", None))
        self.lb_33.setText(QCoreApplication.translate("Dialog", u"2024", None))
        self.pb_34.setText("")
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u041f\u043d", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u0412\u0442", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"\u0421\u0440", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u0427\u0442", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u041f\u0442", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u0421\u0431", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u041d\u0434", None))
        self.pb_t1.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t2.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t3.setText(QCoreApplication.translate("Dialog", u"31", None))
        self.pb_t4.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t5.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t6.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t7.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t8.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t9.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t10.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t11.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t12.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t13.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t14.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t15.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t16.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t17.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t18.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t19.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t20.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t21.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t22.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t23.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t24.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t25.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t26.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t27.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t28.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t29.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t30.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t31.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t32.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t33.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t34.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t35.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t36.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t37.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t38.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t39.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t40.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t41.setText(QCoreApplication.translate("Dialog", u"30", None))
        self.pb_t42.setText(QCoreApplication.translate("Dialog", u"30", None))
    # retranslateUi

