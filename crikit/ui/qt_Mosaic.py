# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ui_Mosaic.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1200, 915)
        MainWindow.setMaximumSize(QtCore.QSize(2000, 16777215))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setContentsMargins(0, -1, -1, -1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QtCore.QSize(500, 0))
        self.frame.setMaximumSize(QtCore.QSize(500, 16777215))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(3, 3, 3, 3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.verticalLayoutOptions = QtWidgets.QVBoxLayout()
        self.verticalLayoutOptions.setSpacing(1)
        self.verticalLayoutOptions.setObjectName("verticalLayoutOptions")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 0, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.frame)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5, 0, QtCore.Qt.AlignRight)
        self.spinBoxMRows = QtWidgets.QSpinBox(self.frame)
        self.spinBoxMRows.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxMRows.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxMRows.setMinimum(1)
        self.spinBoxMRows.setObjectName("spinBoxMRows")
        self.verticalLayout.addWidget(self.spinBoxMRows, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.frame)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignRight)
        self.spinBoxNCols = QtWidgets.QSpinBox(self.frame)
        self.spinBoxNCols.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxNCols.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxNCols.setMinimum(1)
        self.spinBoxNCols.setMaximum(300)
        self.spinBoxNCols.setProperty("value", 1)
        self.spinBoxNCols.setObjectName("spinBoxNCols")
        self.verticalLayout_3.addWidget(self.spinBoxNCols, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayoutOptions.addLayout(self.horizontalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOptions.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.verticalLayoutOptions.addWidget(self.label, 0, QtCore.Qt.AlignRight)
        self.spinBoxStartRow = QtWidgets.QSpinBox(self.frame)
        self.spinBoxStartRow.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxStartRow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxStartRow.setMaximum(500)
        self.spinBoxStartRow.setObjectName("spinBoxStartRow")
        self.verticalLayoutOptions.addWidget(self.spinBoxStartRow, 0, QtCore.Qt.AlignRight)
        spacerItem1 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOptions.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setObjectName("label_2")
        self.verticalLayoutOptions.addWidget(self.label_2, 0, QtCore.Qt.AlignRight)
        self.spinBoxEndRow = QtWidgets.QSpinBox(self.frame)
        self.spinBoxEndRow.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxEndRow.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxEndRow.setMaximum(500)
        self.spinBoxEndRow.setObjectName("spinBoxEndRow")
        self.verticalLayoutOptions.addWidget(self.spinBoxEndRow, 0, QtCore.Qt.AlignRight)
        spacerItem2 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOptions.addItem(spacerItem2)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.verticalLayoutOptions.addWidget(self.label_3, 0, QtCore.Qt.AlignRight)
        self.spinBoxStartCol = QtWidgets.QSpinBox(self.frame)
        self.spinBoxStartCol.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxStartCol.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxStartCol.setMaximum(500)
        self.spinBoxStartCol.setObjectName("spinBoxStartCol")
        self.verticalLayoutOptions.addWidget(self.spinBoxStartCol, 0, QtCore.Qt.AlignRight)
        spacerItem3 = QtWidgets.QSpacerItem(20, 15, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOptions.addItem(spacerItem3)
        self.label_4 = QtWidgets.QLabel(self.frame)
        self.label_4.setObjectName("label_4")
        self.verticalLayoutOptions.addWidget(self.label_4, 0, QtCore.Qt.AlignRight)
        self.spinBoxEndCol = QtWidgets.QSpinBox(self.frame)
        self.spinBoxEndCol.setMinimumSize(QtCore.QSize(50, 0))
        self.spinBoxEndCol.setMaximumSize(QtCore.QSize(50, 16777215))
        self.spinBoxEndCol.setMaximum(500)
        self.spinBoxEndCol.setObjectName("spinBoxEndCol")
        self.verticalLayoutOptions.addWidget(self.spinBoxEndCol, 0, QtCore.Qt.AlignRight)
        self.checkBoxCompress = QtWidgets.QCheckBox(self.frame)
        self.checkBoxCompress.setObjectName("checkBoxCompress")
        self.verticalLayoutOptions.addWidget(self.checkBoxCompress, 0, QtCore.Qt.AlignRight)
        spacerItem4 = QtWidgets.QSpacerItem(20, 5, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayoutOptions.addItem(spacerItem4)
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setObjectName("label_8")
        self.verticalLayoutOptions.addWidget(self.label_8, 0, QtCore.Qt.AlignLeft)
        self.comboBoxRowCol = QtWidgets.QComboBox(self.frame)
        self.comboBoxRowCol.setMaximumSize(QtCore.QSize(100, 16777215))
        self.comboBoxRowCol.setObjectName("comboBoxRowCol")
        self.comboBoxRowCol.addItem("")
        self.comboBoxRowCol.addItem("")
        self.verticalLayoutOptions.addWidget(self.comboBoxRowCol, 0, QtCore.Qt.AlignLeft)
        self.checkBoxFlipH = QtWidgets.QCheckBox(self.frame)
        self.checkBoxFlipH.setMaximumSize(QtCore.QSize(120, 16777215))
        self.checkBoxFlipH.setObjectName("checkBoxFlipH")
        self.verticalLayoutOptions.addWidget(self.checkBoxFlipH, 0, QtCore.Qt.AlignLeft)
        self.checkBoxFlipV = QtWidgets.QCheckBox(self.frame)
        self.checkBoxFlipV.setMaximumSize(QtCore.QSize(110, 16777215))
        self.checkBoxFlipV.setObjectName("checkBoxFlipV")
        self.verticalLayoutOptions.addWidget(self.checkBoxFlipV, 0, QtCore.Qt.AlignLeft)
        self.checkBoxTranspose = QtWidgets.QCheckBox(self.frame)
        self.checkBoxTranspose.setMaximumSize(QtCore.QSize(110, 16777215))
        self.checkBoxTranspose.setObjectName("checkBoxTranspose")
        self.verticalLayoutOptions.addWidget(self.checkBoxTranspose, 0, QtCore.Qt.AlignLeft)
        self.verticalLayout_4.addLayout(self.verticalLayoutOptions)
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.pushButtonMoveUp = QtWidgets.QPushButton(self.frame)
        self.pushButtonMoveUp.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButtonMoveUp.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/arrow-circle-top-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMoveUp.setIcon(icon)
        self.pushButtonMoveUp.setObjectName("pushButtonMoveUp")
        self.horizontalLayout_3.addWidget(self.pushButtonMoveUp)
        self.pushButtonMoveDown = QtWidgets.QPushButton(self.frame)
        self.pushButtonMoveDown.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButtonMoveDown.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/arrow-circle-bottom-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonMoveDown.setIcon(icon1)
        self.pushButtonMoveDown.setObjectName("pushButtonMoveDown")
        self.horizontalLayout_3.addWidget(self.pushButtonMoveDown)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem6)
        self.pushButtonDeleteDataset = QtWidgets.QPushButton(self.frame)
        self.pushButtonDeleteDataset.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButtonDeleteDataset.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/minus-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonDeleteDataset.setIcon(icon2)
        self.pushButtonDeleteDataset.setObjectName("pushButtonDeleteDataset")
        self.horizontalLayout_3.addWidget(self.pushButtonDeleteDataset)
        self.pushButtonAddDataset = QtWidgets.QPushButton(self.frame)
        self.pushButtonAddDataset.setMaximumSize(QtCore.QSize(50, 16777215))
        self.pushButtonAddDataset.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/plus-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonAddDataset.setIcon(icon3)
        self.pushButtonAddDataset.setObjectName("pushButtonAddDataset")
        self.horizontalLayout_3.addWidget(self.pushButtonAddDataset)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_3)
        self.verticalLayout_5.addWidget(self.frame, 0, QtCore.Qt.AlignRight)
        spacerItem8 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem8)
        self.gridLayout_2.addLayout(self.verticalLayout_5, 0, 2, 1, 1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.labelWavenumber_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.labelWavenumber_2.sizePolicy().hasHeightForWidth())
        self.labelWavenumber_2.setSizePolicy(sizePolicy)
        self.labelWavenumber_2.setMinimumSize(QtCore.QSize(120, 20))
        self.labelWavenumber_2.setMaximumSize(QtCore.QSize(1000, 20))
        self.labelWavenumber_2.setTextFormat(QtCore.Qt.AutoText)
        self.labelWavenumber_2.setAlignment(QtCore.Qt.AlignCenter)
        self.labelWavenumber_2.setObjectName("labelWavenumber_2")
        self.gridLayout_3.addWidget(self.labelWavenumber_2, 1, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lineEditPix = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditPix.sizePolicy().hasHeightForWidth())
        self.lineEditPix.setSizePolicy(sizePolicy)
        self.lineEditPix.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEditPix.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lineEditPix.setFont(font)
        self.lineEditPix.setStyleSheet("font: 14pt \"Arial\";")
        self.lineEditPix.setObjectName("lineEditPix")
        self.gridLayout_3.addWidget(self.lineEditPix, 0, 0, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.lineEditFreq = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEditFreq.setEnabled(True)
        self.lineEditFreq.setMinimumSize(QtCore.QSize(100, 30))
        self.lineEditFreq.setMaximumSize(QtCore.QSize(100, 30))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(198, 198, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(198, 198, 198))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(240, 240, 240))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        self.lineEditFreq.setPalette(palette)
        self.lineEditFreq.setText("")
        self.lineEditFreq.setReadOnly(True)
        self.lineEditFreq.setObjectName("lineEditFreq")
        self.gridLayout_3.addWidget(self.lineEditFreq, 0, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 1, 1, 1, 1, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.sliderFreq = QtWidgets.QScrollBar(self.centralwidget)
        self.sliderFreq.setMinimumSize(QtCore.QSize(200, 30))
        self.sliderFreq.setProperty("value", 10)
        self.sliderFreq.setOrientation(QtCore.Qt.Horizontal)
        self.sliderFreq.setObjectName("sliderFreq")
        self.gridLayout_3.addWidget(self.sliderFreq, 2, 0, 1, 2, QtCore.Qt.AlignBottom)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_3.addItem(spacerItem9, 3, 0, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout_3, 2, 0, 1, 1)
        self.frameMosaicImg = QtWidgets.QFrame(self.centralwidget)
        self.frameMosaicImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frameMosaicImg.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frameMosaicImg.setObjectName("frameMosaicImg")
        self.gridLayout = QtWidgets.QGridLayout(self.frameMosaicImg)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayoutMPL = QtWidgets.QVBoxLayout()
        self.verticalLayoutMPL.setObjectName("verticalLayoutMPL")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayoutMPL.addItem(spacerItem10)
        self.gridLayout.addLayout(self.verticalLayoutMPL, 0, 0, 1, 1)
        spacerItem11 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 1, 0, 1, 1)
        self.gridLayout_2.addWidget(self.frameMosaicImg, 0, 0, 1, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(500, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(500, 16777215))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.frame_2 = QtWidgets.QFrame(self.tab_3)
        self.frame_2.setMaximumSize(QtCore.QSize(400, 16777215))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_10 = QtWidgets.QLabel(self.frame_2)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        self.spinBoxIntercept = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spinBoxIntercept.setDecimals(10)
        self.spinBoxIntercept.setMinimum(-100000000.0)
        self.spinBoxIntercept.setMaximum(100000000.0)
        self.spinBoxIntercept.setProperty("value", 832.551012)
        self.spinBoxIntercept.setObjectName("spinBoxIntercept")
        self.verticalLayout_2.addWidget(self.spinBoxIntercept)
        spacerItem12 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem12)
        self.label_11 = QtWidgets.QLabel(self.frame_2)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        self.spinBoxSlope = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spinBoxSlope.setDecimals(10)
        self.spinBoxSlope.setMinimum(-100000000.0)
        self.spinBoxSlope.setMaximum(100000000.0)
        self.spinBoxSlope.setProperty("value", -0.165956)
        self.spinBoxSlope.setObjectName("spinBoxSlope")
        self.verticalLayout_2.addWidget(self.spinBoxSlope)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem13)
        self.label_12 = QtWidgets.QLabel(self.frame_2)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_2.addWidget(self.label_12)
        self.spinBoxProbe = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spinBoxProbe.setDecimals(5)
        self.spinBoxProbe.setMinimum(-1000000000.0)
        self.spinBoxProbe.setMaximum(1000000000.0)
        self.spinBoxProbe.setProperty("value", 771.461)
        self.spinBoxProbe.setObjectName("spinBoxProbe")
        self.verticalLayout_2.addWidget(self.spinBoxProbe)
        self.label_13 = QtWidgets.QLabel(self.frame_2)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_2.addWidget(self.label_13)
        self.spinBoxCalibWL = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spinBoxCalibWL.setDecimals(10)
        self.spinBoxCalibWL.setMinimum(-100000000.0)
        self.spinBoxCalibWL.setMaximum(10000000.0)
        self.spinBoxCalibWL.setProperty("value", 700.0)
        self.spinBoxCalibWL.setObjectName("spinBoxCalibWL")
        self.verticalLayout_2.addWidget(self.spinBoxCalibWL)
        spacerItem14 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem14)
        self.label_14 = QtWidgets.QLabel(self.frame_2)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_2.addWidget(self.label_14)
        self.spinBoxCenterWL = QtWidgets.QDoubleSpinBox(self.frame_2)
        self.spinBoxCenterWL.setDecimals(10)
        self.spinBoxCenterWL.setMinimum(-100000000.0)
        self.spinBoxCenterWL.setMaximum(10000000.0)
        self.spinBoxCenterWL.setProperty("value", 700.0)
        self.spinBoxCenterWL.setObjectName("spinBoxCenterWL")
        self.verticalLayout_2.addWidget(self.spinBoxCenterWL)
        spacerItem15 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem15)
        self.verticalLayout_6.addWidget(self.frame_2, 0, QtCore.Qt.AlignLeft)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_2.addWidget(self.tabWidget, 2, 2, 1, 1, QtCore.Qt.AlignRight)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1200, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionAddFromHDF = QtWidgets.QAction(MainWindow)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/envelope-open-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionAddFromHDF.setIcon(icon4)
        self.actionAddFromHDF.setObjectName("actionAddFromHDF")
        self.actionSaveToHDF5 = QtWidgets.QAction(MainWindow)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/envelope-closed-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.actionSaveToHDF5.setIcon(icon5)
        self.actionSaveToHDF5.setObjectName("actionSaveToHDF5")
        self.actionExit = QtWidgets.QAction(MainWindow)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/open-iconic-master/png/account-logout-4x.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.actionExit.setIcon(icon6)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionAddFromHDF)
        self.menuFile.addAction(self.actionSaveToHDF5)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.toolBar.addAction(self.actionAddFromHDF)
        self.toolBar.addAction(self.actionSaveToHDF5)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionExit)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Make Mosaic Dataset"))
        self.label_5.setText(_translate("MainWindow", "M Rows"))
        self.label_6.setText(_translate("MainWindow", "N Cols"))
        self.label.setText(_translate("MainWindow", "Trim Row Start"))
        self.label_2.setText(_translate("MainWindow", "Trim Row End"))
        self.label_3.setText(_translate("MainWindow", "Trim Col Start"))
        self.label_4.setText(_translate("MainWindow", "Trim Col End"))
        self.checkBoxCompress.setText(_translate("MainWindow", "Compress"))
        self.label_8.setText(_translate("MainWindow", "Row / Column First"))
        self.comboBoxRowCol.setItemText(0, _translate("MainWindow", "Row"))
        self.comboBoxRowCol.setItemText(1, _translate("MainWindow", "Column"))
        self.checkBoxFlipH.setText(_translate("MainWindow", "Flip Horizontally"))
        self.checkBoxFlipV.setText(_translate("MainWindow", "Flip Vertically"))
        self.checkBoxTranspose.setText(_translate("MainWindow", "Transpose"))
        self.label_7.setText(_translate("MainWindow", "Order of Inputs (Drag to Move)"))
        self.labelWavenumber_2.setText(_translate("MainWindow", "Frequency Pixel"))
        self.label_9.setText(_translate("MainWindow", "Estimated Frequency (cm-1)"))
        self.label_10.setText(_translate("MainWindow", "Wavelength Intercept (nm)"))
        self.label_11.setText(_translate("MainWindow", "Wavelength Slope (nm/pix)"))
        self.label_12.setText(_translate("MainWindow", "Probe Wavelength (nm)"))
        self.label_13.setText(_translate("MainWindow", "Calibration Wavelength (nm)"))
        self.label_14.setText(_translate("MainWindow", "Current Center Wavelength (nm)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Spectral Calibration"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "Spatial Calibration"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionAddFromHDF.setText(_translate("MainWindow", "Add from HDF5"))
        self.actionAddFromHDF.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionSaveToHDF5.setText(_translate("MainWindow", "Save to HDF5"))
        self.actionSaveToHDF5.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

from . import icons_all_rc
