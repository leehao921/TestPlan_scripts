# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_importOtherTestPlanDlg(object):
    def setupUi(self, importOtherTestPlanDlg):
        if not importOtherTestPlanDlg.objectName():
            importOtherTestPlanDlg.setObjectName(u"importOtherTestPlanDlg")
        importOtherTestPlanDlg.resize(480, 580)
        importOtherTestPlanDlg.setMinimumSize(QSize(480, 580))
        font = QFont()
        font.setFamily(u"Tahoma")
        importOtherTestPlanDlg.setFont(font)
        self.verticalLayout = QVBoxLayout(importOtherTestPlanDlg)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox = QGroupBox(importOtherTestPlanDlg)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBoxWaf = QGroupBox(self.groupBox)
        self.groupBoxWaf.setObjectName(u"groupBoxWaf")
        self.groupBoxWaf.setEnabled(True)
        self.horizontalLayout_3 = QHBoxLayout(self.groupBoxWaf)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.lineEditWaf = QLineEdit(self.groupBoxWaf)
        self.lineEditWaf.setObjectName(u"lineEditWaf")

        self.horizontalLayout_3.addWidget(self.lineEditWaf)

        self.pushButtonWaf = QPushButton(self.groupBoxWaf)
        self.pushButtonWaf.setObjectName(u"pushButtonWaf")

        self.horizontalLayout_3.addWidget(self.pushButtonWaf)


        self.verticalLayout_2.addWidget(self.groupBoxWaf)

        self.groupBoxDie = QGroupBox(self.groupBox)
        self.groupBoxDie.setObjectName(u"groupBoxDie")
        self.groupBoxDie.setEnabled(True)
        self.horizontalLayout_4 = QHBoxLayout(self.groupBoxDie)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.lineEditDie = QLineEdit(self.groupBoxDie)
        self.lineEditDie.setObjectName(u"lineEditDie")

        self.horizontalLayout_4.addWidget(self.lineEditDie)

        self.pushButtonDie = QPushButton(self.groupBoxDie)
        self.pushButtonDie.setObjectName(u"pushButtonDie")

        self.horizontalLayout_4.addWidget(self.pushButtonDie)


        self.verticalLayout_2.addWidget(self.groupBoxDie)

        self.groupBoxTst = QGroupBox(self.groupBox)
        self.groupBoxTst.setObjectName(u"groupBoxTst")
        self.groupBoxTst.setEnabled(True)
        self.horizontalLayout_5 = QHBoxLayout(self.groupBoxTst)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.lineEditTst = QLineEdit(self.groupBoxTst)
        self.lineEditTst.setObjectName(u"lineEditTst")
        self.lineEditTst.setEnabled(True)

        self.horizontalLayout_5.addWidget(self.lineEditTst)

        self.pushButtonTst = QPushButton(self.groupBoxTst)
        self.pushButtonTst.setObjectName(u"pushButtonTst")

        self.horizontalLayout_5.addWidget(self.pushButtonTst)


        self.verticalLayout_2.addWidget(self.groupBoxTst)

        self.groupBoxPrb = QGroupBox(self.groupBox)
        self.groupBoxPrb.setObjectName(u"groupBoxPrb")
        self.groupBoxPrb.setEnabled(True)
        self.horizontalLayout_6 = QHBoxLayout(self.groupBoxPrb)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(-1, 0, -1, -1)
        self.lineEditPrb = QLineEdit(self.groupBoxPrb)
        self.lineEditPrb.setObjectName(u"lineEditPrb")
        self.lineEditPrb.setEnabled(True)

        self.horizontalLayout_6.addWidget(self.lineEditPrb)

        self.pushButtonPrb = QPushButton(self.groupBoxPrb)
        self.pushButtonPrb.setObjectName(u"pushButtonPrb")

        self.horizontalLayout_6.addWidget(self.pushButtonPrb)


        self.verticalLayout_2.addWidget(self.groupBoxPrb)

        self.groupBoxShotDie = QGroupBox(self.groupBox)
        self.groupBoxShotDie.setObjectName(u"groupBoxShotDie")
        self.horizontalLayout_10 = QHBoxLayout(self.groupBoxShotDie)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.lineEditShotDie = QLineEdit(self.groupBoxShotDie)
        self.lineEditShotDie.setObjectName(u"lineEditShotDie")

        self.horizontalLayout_10.addWidget(self.lineEditShotDie)

        self.pushButtonShotDie = QPushButton(self.groupBoxShotDie)
        self.pushButtonShotDie.setObjectName(u"pushButtonShotDie")

        self.horizontalLayout_10.addWidget(self.pushButtonShotDie)


        self.verticalLayout_2.addWidget(self.groupBoxShotDie)

        self.groupBoxLim = QGroupBox(self.groupBox)
        self.groupBoxLim.setObjectName(u"groupBoxLim")
        self.horizontalLayout_7 = QHBoxLayout(self.groupBoxLim)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.lineEditLim = QLineEdit(self.groupBoxLim)
        self.lineEditLim.setObjectName(u"lineEditLim")

        self.horizontalLayout_7.addWidget(self.lineEditLim)

        self.pushButtonLim = QPushButton(self.groupBoxLim)
        self.pushButtonLim.setObjectName(u"pushButtonLim")

        self.horizontalLayout_7.addWidget(self.pushButtonLim)


        self.verticalLayout_2.addWidget(self.groupBoxLim)

        self.groupBoxMapping = QGroupBox(self.groupBox)
        self.groupBoxMapping.setObjectName(u"groupBoxMapping")
        self.horizontalLayout_8 = QHBoxLayout(self.groupBoxMapping)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, 0, -1, -1)
        self.lineEditMapping = QLineEdit(self.groupBoxMapping)
        self.lineEditMapping.setObjectName(u"lineEditMapping")

        self.horizontalLayout_8.addWidget(self.lineEditMapping)

        self.pushButtonMapping = QPushButton(self.groupBoxMapping)
        self.pushButtonMapping.setObjectName(u"pushButtonMapping")

        self.horizontalLayout_8.addWidget(self.pushButtonMapping)


        self.verticalLayout_2.addWidget(self.groupBoxMapping)

        self.groupBoxTemplate = QGroupBox(self.groupBox)
        self.groupBoxTemplate.setObjectName(u"groupBoxTemplate")
        self.horizontalLayout_9 = QHBoxLayout(self.groupBoxTemplate)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.lineEditTemplate = QLineEdit(self.groupBoxTemplate)
        self.lineEditTemplate.setObjectName(u"lineEditTemplate")

        self.horizontalLayout_9.addWidget(self.lineEditTemplate)

        self.pushButtonTemplate = QPushButton(self.groupBoxTemplate)
        self.pushButtonTemplate.setObjectName(u"pushButtonTemplate")

        self.horizontalLayout_9.addWidget(self.pushButtonTemplate)


        self.verticalLayout_2.addWidget(self.groupBoxTemplate)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(importOtherTestPlanDlg)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.gridLayout = QGridLayout(self.groupBox_2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBoxSkipComment = QCheckBox(self.groupBox_2)
        self.checkBoxSkipComment.setObjectName(u"checkBoxSkipComment")
        self.checkBoxSkipComment.setLayoutDirection(Qt.LeftToRight)
        self.checkBoxSkipComment.setChecked(False)

        self.gridLayout.addWidget(self.checkBoxSkipComment, 0, 0, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButtonImport = QPushButton(importOtherTestPlanDlg)
        self.pushButtonImport.setObjectName(u"pushButtonImport")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonImport.sizePolicy().hasHeightForWidth())
        self.pushButtonImport.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButtonImport)

        self.pushButtonCancel = QPushButton(importOtherTestPlanDlg)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")
        sizePolicy.setHeightForWidth(self.pushButtonCancel.sizePolicy().hasHeightForWidth())
        self.pushButtonCancel.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.pushButtonCancel)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(importOtherTestPlanDlg)

        QMetaObject.connectSlotsByName(importOtherTestPlanDlg)
    # setupUi

    def retranslateUi(self, importOtherTestPlanDlg):
        importOtherTestPlanDlg.setWindowTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Import Other Test Plan", None))
        self.groupBox.setTitle("")
        self.groupBoxWaf.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Wafer Spec File:", None))
        self.pushButtonWaf.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxDie.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Die Spec File:", None))
        self.pushButtonDie.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxTst.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Test Spec File:", None))
        self.pushButtonTst.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxPrb.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Probe Spec File:", None))
        self.pushButtonPrb.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxShotDie.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Shot To Die File", None))
        self.pushButtonShotDie.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxLim.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Limit File:", None))
        self.pushButtonLim.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxMapping.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Mapping File:", None))
        self.pushButtonMapping.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBoxTemplate.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Template Test Spec File:", None))
        self.pushButtonTemplate.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"...", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("importOtherTestPlanDlg", u"Addtional Settings:", None))
        self.checkBoxSkipComment.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"Skip Comment", None))
        self.pushButtonImport.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"Import", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("importOtherTestPlanDlg", u"Cancel", None))
    # retranslateUi

