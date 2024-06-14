# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diary2.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QGridLayout, QHBoxLayout, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)
import res_rc

class Ui_Dialog_1(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(556, 592)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x1:2, y1:1, stop:0 rgba(178, 34, 34, 255), stop:0.5 rgba(0, 0, 205, 255), stop:1 rgba(178, 34, 34, 255));")
        Dialog.setInputMethodHints(Qt.InputMethodHint.ImhEmailCharactersOnly)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(-1, 4, -1, -1)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 1, 5, 2)
        self.pb_21 = QPushButton(self.frame)
        self.pb_21.setObjectName(u"pb_21")
        self.pb_21.setEnabled(True)
        self.pb_21.setMinimumSize(QSize(0, 31))
        self.pb_21.setMaximumSize(QSize(150, 31))
        self.pb_21.setStyleSheet(u"QPushButton{\n"
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
        icon.addFile(u":/icons/icons/search_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_21.setIcon(icon)
        self.pb_21.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_21)

        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);")

        self.horizontalLayout.addWidget(self.label_2)

        self.comboBox = QComboBox(self.frame)
        self.comboBox.addItem("")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/sentiment_very_satisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon1, "")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/mood_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon2, "")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/sentiment_satisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon3, "")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/sentiment_neutral_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon4, "")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/sentiment_frustrated_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon5, "")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/sentiment_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon6, "")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/mood_bad_24dp_FILL0_wght400_GRAD0_opsz24 (2).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon7, "")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/sentiment_extremely_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon8, "")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/sentiment_very_dissatisfied_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.comboBox.addItem(icon9, "")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMaximumSize(QSize(60, 30))
        self.comboBox.setAcceptDrops(False)
        self.comboBox.setToolTipDuration(-1)
        self.comboBox.setInputMethodHints(Qt.InputMethodHint.ImhNone)
        self.comboBox.setIconSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.comboBox)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"background-color: rgba(0, 0, 0, 0);\n"
"border: 1px solid rgba(0, 0, 0, 0);")

        self.horizontalLayout.addWidget(self.label)

        self.pb_22 = QPushButton(self.frame)
        self.pb_22.setObjectName(u"pb_22")
        self.pb_22.setMinimumSize(QSize(0, 30))
        self.pb_22.setMaximumSize(QSize(150, 31))
        self.pb_22.setStyleSheet(u"QPushButton{\n"
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
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/delete_24dp_FILL0_wght400_GRAD0_opsz24 (1).svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pb_22.setIcon(icon10)
        self.pb_22.setIconSize(QSize(24, 24))

        self.horizontalLayout.addWidget(self.pb_22)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.te_21 = QTextEdit(self.frame)
        self.te_21.setObjectName(u"te_21")
        self.te_21.setStyleSheet(u"background-color: rgba(0, 0, 0, 30);\n"
"border: 1px solid rgba(0, 0, 0, 40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"font-weight: bold;")
        self.te_21.setTabChangesFocus(False)
        self.te_21.setTabStopDistance(80.000000000000000)

        self.verticalLayout.addWidget(self.te_21)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u0429\u043e\u0434\u0435\u043d\u043d\u0438\u043a", None))
#if QT_CONFIG(accessibility)
        Dialog.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
        self.pb_21.setText(QCoreApplication.translate("Dialog", u"\u0406\u043d\u0448\u0438\u0439 \u0434\u0435\u043d\u044c", None))
        self.label_2.setText("")
        self.comboBox.setItemText(0, "")
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"  1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"  2", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"  3", None))
        self.comboBox.setItemText(4, QCoreApplication.translate("Dialog", u"  4", None))
        self.comboBox.setItemText(5, QCoreApplication.translate("Dialog", u"  5", None))
        self.comboBox.setItemText(6, QCoreApplication.translate("Dialog", u"  6", None))
        self.comboBox.setItemText(7, QCoreApplication.translate("Dialog", u"  7", None))
        self.comboBox.setItemText(8, QCoreApplication.translate("Dialog", u"  8", None))
        self.comboBox.setItemText(9, QCoreApplication.translate("Dialog", u"  9", None))

        self.label.setText("")
        self.pb_22.setText(QCoreApplication.translate("Dialog", u"\u0412\u0438\u0434\u0430\u043b\u0438\u0442\u0438 \u0437\u0430\u043f\u0438\u0441", None))
        self.te_21.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Segoe UI'; font-size:9pt; font-weight:700; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
    # retranslateUi

