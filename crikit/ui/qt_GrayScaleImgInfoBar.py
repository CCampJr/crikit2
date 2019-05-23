# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_GrayscaleImgInfoBar.ui'
#
# Created by: PyQt5 UI code generator 5.8.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_formWidgetGrayScaleImgInfoBar(object):
    def setupUi(self, formWidgetGrayScaleImgInfoBar):
        formWidgetGrayScaleImgInfoBar.setObjectName("formWidgetGrayScaleImgInfoBar")
        formWidgetGrayScaleImgInfoBar.resize(522, 134)
        self.verticalLayout = QtWidgets.QVBoxLayout(formWidgetGrayScaleImgInfoBar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.mainFrame = QtWidgets.QFrame(formWidgetGrayScaleImgInfoBar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainFrame.sizePolicy().hasHeightForWidth())
        self.mainFrame.setSizePolicy(sizePolicy)
        self.mainFrame.setMinimumSize(QtCore.QSize(500, 0))
        self.mainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.mainFrame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.mainFrame.setObjectName("mainFrame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.mainFrame)
        self.horizontalLayout.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayoutFixedCutCompress = QtWidgets.QVBoxLayout()
        self.verticalLayoutFixedCutCompress.setSpacing(2)
        self.verticalLayoutFixedCutCompress.setObjectName("verticalLayoutFixedCutCompress")
        self.checkBoxFixed = QtWidgets.QCheckBox(self.mainFrame)
        self.checkBoxFixed.setChecked(False)
        self.checkBoxFixed.setObjectName("checkBoxFixed")
        self.verticalLayoutFixedCutCompress.addWidget(self.checkBoxFixed)
        self.labelBelowMin = QtWidgets.QLabel(self.mainFrame)
        self.labelBelowMin.setObjectName("labelBelowMin")
        self.verticalLayoutFixedCutCompress.addWidget(self.labelBelowMin)
        self.comboBoxBelowMin = QtWidgets.QComboBox(self.mainFrame)
        self.comboBoxBelowMin.setObjectName("comboBoxBelowMin")
        self.comboBoxBelowMin.addItem("")
        self.comboBoxBelowMin.addItem("")
        self.verticalLayoutFixedCutCompress.addWidget(self.comboBoxBelowMin)
        self.labelAboveMax = QtWidgets.QLabel(self.mainFrame)
        self.labelAboveMax.setObjectName("labelAboveMax")
        self.verticalLayoutFixedCutCompress.addWidget(self.labelAboveMax)
        self.comboBoxAboveMax = QtWidgets.QComboBox(self.mainFrame)
        self.comboBoxAboveMax.setObjectName("comboBoxAboveMax")
        self.comboBoxAboveMax.addItem("")
        self.comboBoxAboveMax.addItem("")
        self.verticalLayoutFixedCutCompress.addWidget(self.comboBoxAboveMax)
        self.horizontalLayout.addLayout(self.verticalLayoutFixedCutCompress)
        self.verticalLayoutMinValue = QtWidgets.QVBoxLayout()
        self.verticalLayoutMinValue.setSpacing(2)
        self.verticalLayoutMinValue.setObjectName("verticalLayoutMinValue")
        self.labelMinValue = QtWidgets.QLabel(self.mainFrame)
        self.labelMinValue.setObjectName("labelMinValue")
        self.verticalLayoutMinValue.addWidget(self.labelMinValue)
        self.spinBoxMin = QtWidgets.QDoubleSpinBox(self.mainFrame)
        self.spinBoxMin.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBoxMin.setDecimals(6)
        self.spinBoxMin.setSingleStep(0.001)
        self.spinBoxMin.setObjectName("spinBoxMin")
        self.verticalLayoutMinValue.addWidget(self.spinBoxMin)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutMinValue.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayoutMinValue)
        self.verticalLayoutMaxValue = QtWidgets.QVBoxLayout()
        self.verticalLayoutMaxValue.setSpacing(2)
        self.verticalLayoutMaxValue.setObjectName("verticalLayoutMaxValue")
        self.labelMaxValue = QtWidgets.QLabel(self.mainFrame)
        self.labelMaxValue.setObjectName("labelMaxValue")
        self.verticalLayoutMaxValue.addWidget(self.labelMaxValue)
        self.spinBoxMax = QtWidgets.QDoubleSpinBox(self.mainFrame)
        self.spinBoxMax.setMinimumSize(QtCore.QSize(0, 25))
        self.spinBoxMax.setDecimals(6)
        self.spinBoxMax.setMaximum(101.0)
        self.spinBoxMax.setProperty("value", 0.9)
        self.spinBoxMax.setObjectName("spinBoxMax")
        self.verticalLayoutMaxValue.addWidget(self.spinBoxMax)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutMaxValue.addItem(spacerItem1)
        self.horizontalLayout.addLayout(self.verticalLayoutMaxValue)
        self.frameSpacer = QtWidgets.QFrame(self.mainFrame)
        self.frameSpacer.setFrameShape(QtWidgets.QFrame.VLine)
        self.frameSpacer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frameSpacer.setObjectName("frameSpacer")
        self.horizontalLayout.addWidget(self.frameSpacer)
        self.verticalLayoutOutlierRemoval = QtWidgets.QVBoxLayout()
        self.verticalLayoutOutlierRemoval.setSpacing(2)
        self.verticalLayoutOutlierRemoval.setObjectName("verticalLayoutOutlierRemoval")
        self.checkBoxRemOutliers = QtWidgets.QCheckBox(self.mainFrame)
        self.checkBoxRemOutliers.setObjectName("checkBoxRemOutliers")
        self.verticalLayoutOutlierRemoval.addWidget(self.checkBoxRemOutliers)
        self.labelStdDevs = QtWidgets.QLabel(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelStdDevs.sizePolicy().hasHeightForWidth())
        self.labelStdDevs.setSizePolicy(sizePolicy)
        self.labelStdDevs.setObjectName("labelStdDevs")
        self.verticalLayoutOutlierRemoval.addWidget(self.labelStdDevs)
        self.spinBoxStdDevs = QtWidgets.QDoubleSpinBox(self.mainFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.spinBoxStdDevs.sizePolicy().hasHeightForWidth())
        self.spinBoxStdDevs.setSizePolicy(sizePolicy)
        self.spinBoxStdDevs.setMaximumSize(QtCore.QSize(16777215, 25))
        self.spinBoxStdDevs.setMaximum(100.0)
        self.spinBoxStdDevs.setSingleStep(0.1)
        self.spinBoxStdDevs.setProperty("value", 3.0)
        self.spinBoxStdDevs.setObjectName("spinBoxStdDevs")
        self.verticalLayoutOutlierRemoval.addWidget(self.spinBoxStdDevs)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOutlierRemoval.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayoutOutlierRemoval)
        self.verticalLayout.addWidget(self.mainFrame)

        self.retranslateUi(formWidgetGrayScaleImgInfoBar)
        QtCore.QMetaObject.connectSlotsByName(formWidgetGrayScaleImgInfoBar)

    def retranslateUi(self, formWidgetGrayScaleImgInfoBar):
        _translate = QtCore.QCoreApplication.translate
        formWidgetGrayScaleImgInfoBar.setWindowTitle(_translate("formWidgetGrayScaleImgInfoBar", "Form"))
        self.checkBoxFixed.setText(_translate("formWidgetGrayScaleImgInfoBar", "Fixed"))
        self.labelBelowMin.setText(_translate("formWidgetGrayScaleImgInfoBar", "Below Minimum"))
        self.comboBoxBelowMin.setItemText(0, _translate("formWidgetGrayScaleImgInfoBar", "Cut"))
        self.comboBoxBelowMin.setItemText(1, _translate("formWidgetGrayScaleImgInfoBar", "Compress"))
        self.labelAboveMax.setText(_translate("formWidgetGrayScaleImgInfoBar", "Above Maximum"))
        self.comboBoxAboveMax.setItemText(0, _translate("formWidgetGrayScaleImgInfoBar", "Cut"))
        self.comboBoxAboveMax.setItemText(1, _translate("formWidgetGrayScaleImgInfoBar", "Compress"))
        self.labelMinValue.setText(_translate("formWidgetGrayScaleImgInfoBar", "Minimum"))
        self.labelMaxValue.setText(_translate("formWidgetGrayScaleImgInfoBar", "Maximum"))
        self.checkBoxRemOutliers.setText(_translate("formWidgetGrayScaleImgInfoBar", "Outlier Removal"))
        self.labelStdDevs.setText(_translate("formWidgetGrayScaleImgInfoBar", "Std. Dev\'s"))
