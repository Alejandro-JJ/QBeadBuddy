# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QBeadBuddy_v2_designer.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 590)
        MainWindow.setStyleSheet("background-color: rgb(130, 130, 130);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(60, 460, 121, 81))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_threshold = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_threshold.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_threshold.setObjectName("label_threshold")
        self.gridLayout_2.addWidget(self.label_threshold, 1, 0, 1, 1)
        self.INPUT_BGnoise = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.INPUT_BGnoise.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_BGnoise.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_BGnoise.setObjectName("INPUT_BGnoise")
        self.gridLayout_2.addWidget(self.INPUT_BGnoise, 0, 1, 1, 1)
        self.label_BGnoise = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_BGnoise.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_BGnoise.setObjectName("label_BGnoise")
        self.gridLayout_2.addWidget(self.label_BGnoise, 0, 0, 1, 1)
        self.INPUT_Threshold = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.INPUT_Threshold.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Threshold.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_Threshold.setObjectName("INPUT_Threshold")
        self.gridLayout_2.addWidget(self.INPUT_Threshold, 1, 1, 1, 1)
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(210, 460, 121, 81))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_Outline = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Outline.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_Outline.setObjectName("label_Outline")
        self.gridLayout_3.addWidget(self.label_Outline, 1, 0, 1, 1)
        self.INPUT_Spot = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.INPUT_Spot.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Spot.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_Spot.setObjectName("INPUT_Spot")
        self.gridLayout_3.addWidget(self.INPUT_Spot, 0, 1, 1, 1)
        self.label_Spot = QtWidgets.QLabel(self.gridLayoutWidget_3)
        self.label_Spot.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_Spot.setObjectName("label_Spot")
        self.gridLayout_3.addWidget(self.label_Spot, 0, 0, 1, 1)
        self.INPUT_Outline = QtWidgets.QLineEdit(self.gridLayoutWidget_3)
        self.INPUT_Outline.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Outline.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_Outline.setObjectName("INPUT_Outline")
        self.gridLayout_3.addWidget(self.INPUT_Outline, 1, 1, 1, 1)
        self.Slider_1 = QtWidgets.QSlider(self.centralwidget)
        self.Slider_1.setGeometry(QtCore.QRect(30, 420, 400, 16))
        self.Slider_1.setStyleSheet("QSlider::handle:horizontal {\n"
"background-color: rgb(135, 203, 203);\n"
"border: 1px solid #5c5c5c;\n"
"width: 10px;\n"
"border-radius: 3px;\n"
"}")
        self.Slider_1.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_1.setObjectName("Slider_1")
        self.BUTTON_Segment = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_Segment.setGeometry(QtCore.QRect(350, 480, 81, 41))
        self.BUTTON_Segment.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(90, 90, 90);\n"
"font-weight: bold\n"
"")
        self.BUTTON_Segment.setObjectName("BUTTON_Segment")
        self.Slider_2 = QtWidgets.QSlider(self.centralwidget)
        self.Slider_2.setGeometry(QtCore.QRect(450, 420, 400, 16))
        self.Slider_2.setStyleSheet("QSlider::handle:horizontal {\n"
"background-color: rgb(135, 203, 203);\n"
"border: 1px solid #5c5c5c;\n"
"width: 10px;\n"
"border-radius: 3px;\n"
"}")
        self.Slider_2.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_2.setObjectName("Slider_2")
        self.ProgressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.ProgressBar.setGeometry(QtCore.QRect(870, 480, 200, 23))
        self.ProgressBar.setStyleSheet("selection-background-color: rgb(135, 203, 203);\n"
"color:rgb(0,0,0)")
        self.ProgressBar.setProperty("value", 0)
        self.ProgressBar.setObjectName("ProgressBar")
        self.Canvas_1 = QtWidgets.QLabel(self.centralwidget)
        self.Canvas_1.setGeometry(QtCore.QRect(30, 0, 400, 400))
        self.Canvas_1.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Canvas_1.setText("")
        self.Canvas_1.setObjectName("Canvas_1")
        self.Canvas_2 = QtWidgets.QLabel(self.centralwidget)
        self.Canvas_2.setGeometry(QtCore.QRect(450, 0, 400, 400))
        self.Canvas_2.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Canvas_2.setText("")
        self.Canvas_2.setObjectName("Canvas_2")
        self.Canvas_3 = QtWidgets.QLabel(self.centralwidget)
        self.Canvas_3.setGeometry(QtCore.QRect(870, 0, 200, 200))
        self.Canvas_3.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.Canvas_3.setText("")
        self.Canvas_3.setObjectName("Canvas_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(490, 440, 111, 104))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.INPUT_pxy = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.INPUT_pxy.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_pxy.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_pxy.setObjectName("INPUT_pxy")
        self.gridLayout_4.addWidget(self.INPUT_pxy, 0, 1, 1, 1)
        self.INPUT_Threshold_2 = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.INPUT_Threshold_2.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_Threshold_2.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_Threshold_2.setObjectName("INPUT_Threshold_2")
        self.gridLayout_4.addWidget(self.INPUT_Threshold_2, 1, 1, 1, 1)
        self.label_pz = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_pz.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_pz.setObjectName("label_pz")
        self.gridLayout_4.addWidget(self.label_pz, 1, 0, 1, 1)
        self.label_pxy = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_pxy.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_pxy.setObjectName("label_pxy")
        self.gridLayout_4.addWidget(self.label_pxy, 0, 0, 1, 1)
        self.INPUT_SH_Order = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
        self.INPUT_SH_Order.setStyleSheet("background-color: rgb(255,255,255);")
        self.INPUT_SH_Order.setAlignment(QtCore.Qt.AlignCenter)
        self.INPUT_SH_Order.setObjectName("INPUT_SH_Order")
        self.gridLayout_4.addWidget(self.INPUT_SH_Order, 2, 1, 1, 1)
        self.label_SH_order = QtWidgets.QLabel(self.gridLayoutWidget_4)
        self.label_SH_order.setStyleSheet("color: rgb(255, 255, 255);\n"
"font-weight: bold")
        self.label_SH_order.setObjectName("label_SH_order")
        self.gridLayout_4.addWidget(self.label_SH_order, 2, 0, 1, 1)
        self.BUTTON_Analyze_BEAD = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_Analyze_BEAD.setGeometry(QtCore.QRect(630, 470, 81, 51))
        self.BUTTON_Analyze_BEAD.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(90, 90, 90);\n"
"font-weight: bold\n"
"")
        self.BUTTON_Analyze_BEAD.setObjectName("BUTTON_Analyze_BEAD")
        self.BUTTON_Analyze_ALL = QtWidgets.QPushButton(self.centralwidget)
        self.BUTTON_Analyze_ALL.setGeometry(QtCore.QRect(720, 470, 81, 51))
        self.BUTTON_Analyze_ALL.setStyleSheet("color: rgb(255,255,255);\n"
"background-color: rgb(90, 90, 90);\n"
"background-color: rgb(40, 100, 150);\n"
"font-weight: bold\n"
"")
        self.BUTTON_Analyze_ALL.setObjectName("BUTTON_Analyze_ALL")
        self.widget = plotCanvas(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(870, 220, 200, 200))
        self.widget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.widget.setObjectName("widget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1098, 20))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.Button_Open = QtWidgets.QAction(MainWindow)
        self.Button_Open.setObjectName("Button_Open")
        self.menuFile.addAction(self.Button_Open)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QBeadBuddy"))
        self.label_threshold.setText(_translate("MainWindow", "Threshold"))
        self.INPUT_BGnoise.setText(_translate("MainWindow", "20"))
        self.label_BGnoise.setText(_translate("MainWindow", "BG noise"))
        self.INPUT_Threshold.setText(_translate("MainWindow", "200"))
        self.label_Outline.setText(_translate("MainWindow", "Outline S"))
        self.INPUT_Spot.setText(_translate("MainWindow", "1"))
        self.label_Spot.setText(_translate("MainWindow", "Spot S"))
        self.INPUT_Outline.setText(_translate("MainWindow", "1"))
        self.BUTTON_Segment.setText(_translate("MainWindow", "SEGMENT"))
        self.INPUT_pxy.setText(_translate("MainWindow", "1"))
        self.INPUT_Threshold_2.setText(_translate("MainWindow", "1"))
        self.label_pz.setText(_translate("MainWindow", "pz (um)"))
        self.label_pxy.setText(_translate("MainWindow", "pxy (um)"))
        self.INPUT_SH_Order.setText(_translate("MainWindow", "5"))
        self.label_SH_order.setText(_translate("MainWindow", "SH order"))
        self.BUTTON_Analyze_BEAD.setText(_translate("MainWindow", "Analyze \n"
" BEAD"))
        self.BUTTON_Analyze_ALL.setText(_translate("MainWindow", "Analyze \n"
" ALL"))
        self.menuFile.setTitle(_translate("MainWindow", "File..."))
        self.Button_Open.setText(_translate("MainWindow", "Open TIFF"))
from plotcanvas import plotCanvas


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
