import warnings
warnings.filterwarnings('ignore')
import sys
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QMainWindow, QFileDialog
import PyQt5.QtGui as QtGui
from PyQt5.QtGui import qRgb, QImage, QColor
from skimage import io
import numpy as np
import os
import pyclesperanto_prototype as cle
from plotcanvas import PlotCanvas
from termcolor import colored
import colorcet as cc
import qimage2ndarray as q2a
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from MasterSegmenter import MasterSegmenter
from F_C20_Optimization import C20_optimization, C20_rotation, C20_rotation_outputs
from F_INITIALIZATION import TransparentAxes


class Ui_MainWindow(QMainWindow):
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
            self.Canvas_1.setScaledContents(True) # to make QImages adjust to label size
            self.Canvas_2.setScaledContents(True) 
            self.Canvas_3.setScaledContents(True) 
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
            self.INPUT_pz = QtWidgets.QLineEdit(self.gridLayoutWidget_4)
            self.INPUT_pz.setStyleSheet("background-color: rgb(255,255,255);")
            self.INPUT_pz.setAlignment(QtCore.Qt.AlignCenter)
            self.INPUT_pz.setObjectName("INPUT_pz")
            self.gridLayout_4.addWidget(self.INPUT_pz, 1, 1, 1, 1)
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
            self.widget = PlotCanvas(self.centralwidget)
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
        self.label_pz.setText(_translate("MainWindow", "pz (um)"))
        self.INPUT_pxy.setText(_translate("MainWindow", "1"))
        self.label_pxy.setText(_translate("MainWindow", "pxy (um)"))
        self.INPUT_pz.setText(_translate("MainWindow", "1"))
        self.BUTTON_Analyze_BEAD.setText(_translate("MainWindow", "Analyze \n"" BEAD"))
        self.BUTTON_Analyze_ALL.setText(_translate("MainWindow", "Analyze \n"" ALL"))
        self.menuFile.setTitle(_translate("MainWindow", "File..."))
        self.Button_Open.setText(_translate("MainWindow", "Open TIFF"))
        self.label_SH_order.setText(_translate("MainWindow", "SH Order"))
        self.INPUT_SH_Order.setText(_translate("MainWindow", "5"))
        
        '''
        Initial disable of buttons
        '''
        self.BUTTON_Segment.setEnabled(False)
        self.BUTTON_Analyze_BEAD.setEnabled(False)
        self.BUTTON_Analyze_ALL.setEnabled(False)
        self.Slider_1.setEnabled(False)
        self.Slider_2.setEnabled(False)
        '''
        GPU Initialization for Esperanto
        '''
        GPUs = cle.available_device_names()
        cle.select_device(GPUs[0])
        print('-'*60)
        print(colored('The GPU ' + GPUs[0] + ' has been selected for MasterSegmenter', 'cyan'))
        print('-'*60)
        '''
        Custom colormaps for plots
        '''
        self.cmap_viridis = plt.get_cmap('viridis')
        self.mycmap2 = cc.glasbey_bw_minc_20_minl_30
        self.mycmap2[0]=[0,0,0] # add black as first value
        self.cmap_glasbey = LinearSegmentedColormap.from_list('cmap_glasbey', self.mycmap2)
        
        '''
        Button-function connections
        '''
        self.Button_Open.triggered.connect(self.OpenDialogTIFF)
        self.Slider_1.valueChanged.connect(self.Slide_Canvas_1)
        self.Slider_2.valueChanged.connect(self.Slide_Canvas_2)
        self.BUTTON_Segment.clicked.connect(self.Segment)
        self.Canvas_2.mousePressEvent = self.GetClick
        self.pixvalue = 0
        self.BUTTON_Analyze_BEAD.clicked.connect(self.AnalyzeBEAD)
        

##########################################################################################        
    
    def apply_colormap(self, img_array, colormap):
        '''
        Applies a colormap to an array and converts it to Qimage for fast plotting in QLabels
        '''
        normalized_img = (img_array - np.min(img_array)) / (np.max(img_array) - np.min(img_array))
        rgba_img = (colormap(normalized_img) * 255).astype(np.uint8)
        height, width = rgba_img.shape[:2]
        bytes_per_line = width * 4
        QIm_colored = QImage(rgba_img.data, width, height, bytes_per_line, QImage.Format_RGBA8888)
        return QIm_colored
        
    def OpenDialogTIFF(self):
        '''
        Open Load dialog, import tiff and plot its first frame
        '''
        fileNameTIFF = QFileDialog.getOpenFileName(self, 'Open File', '/media/alejandro/Coding/MyGits/', ('Image Files(*.tiff, *.tif)') )   
        if fileNameTIFF[0] == '':
            return None
        else:    
            self.fileNameTIFF = fileNameTIFF[0]
            self.FolderName = os.path.dirname(self.fileNameTIFF)
        #print('Loading Image...')
        # Load, pick frame, plot
        self.OriginalTIFF = io.imread(self.fileNameTIFF)
        self.Layers, self.Height, self.Width = np.shape(self.OriginalTIFF)
        
        Qimg_colored = self.apply_colormap(self.OriginalTIFF[0,:,:], self.cmap_viridis)
        self.Canvas_1.setPixmap(QtGui.QPixmap.fromImage(Qimg_colored))
       
        # Activate sliders and buttons
        self.Slider_1.setEnabled(True)
        self.Slider_1.setMinimum(0)
        self.Slider_1.setMaximum(self.Layers-1)
        self.BUTTON_Segment.setEnabled(True)
        
    def Slide_Canvas_1(self):
        '''
        Reads position of Slider_1 and scrolls through the TIFF
        '''
        Qimg_colored = self.apply_colormap(self.OriginalTIFF[self.Slider_1.value(),:,:], self.cmap_viridis)
        self.Canvas_1.setPixmap(QtGui.QPixmap.fromImage(Qimg_colored))


    def Segment(self):
        print('Segmenting...')
        self.backg_r = int(self.INPUT_BGnoise.text())
        self.thr = int(self.INPUT_Threshold.text())
        self.s_spot = int(self.INPUT_Spot.text())
        self.s_outl = int(self.INPUT_Outline.text())
        self.imbeads, self.n, self.radii = MasterSegmenter(self.fileNameTIFF,
                                                   backg_r = self.backg_r, 
                                                   threshold = self.thr, 
                                                   spot_sigma = self.s_spot, 
                                                   outline_sigma = self.s_outl)
        print(f'# Found {self.n} beads')
        print(colored('SEGMENTED \n', 'green'))
        
        # Plot middle frame, and force first canvas to do the same
        midlayer = int(self.Layers/2)
        
        Qimg_segmented_colored = self.apply_colormap(self.imbeads[midlayer,:,:], self.cmap_glasbey)
        self.Canvas_2.setPixmap(QtGui.QPixmap.fromImage(Qimg_segmented_colored))
        self.Slider_1.setValue(midlayer)
        
        Qimg_colored = self.apply_colormap(self.OriginalTIFF[midlayer,:,:], self.cmap_viridis)
        self.Canvas_1.setPixmap(QtGui.QPixmap.fromImage(Qimg_colored))
        self.Slider_2.setValue(midlayer)
        
        # Activate slider and update
        self.Slider_2.setEnabled(True)
        self.Slider_2.setMinimum(0)
        self.Slider_2.setMaximum(self.Layers-1)
        
        # Activate the analysis, and prepare a dummy value for the pixel size
        self.BUTTON_Analyze_BEAD.setEnabled(True)
        self.BUTTON_Analyze_ALL.setEnabled(True)
        self.pixvalue = 0
    
    def Slide_Canvas_2(self):
        '''
        Reads position of Slider_2 and scrolls through the segmented picture
        forcing the first plot to follow it
        '''
        Qimg_segment_colored = self.apply_colormap(self.imbeads[self.Slider_2.value(),:,:], self.cmap_glasbey)
        self.Canvas_2.setPixmap(QtGui.QPixmap.fromImage(Qimg_segment_colored))
        
        self.Slider_1.setValue(self.Slider_2.value())
        Qimg_colored = self.apply_colormap(self.OriginalTIFF[self.Slider_2.value(),:,:], self.cmap_viridis)
        self.Canvas_1.setPixmap(QtGui.QPixmap.fromImage(Qimg_colored))
        
    def GetClick(self, event):
        '''
        Calls a click event in Canvas_2 (segmentation) and stores the pixel value
        thet should be analyzed upon pushing a button
        '''
        x, y, z = event.x(), event.y(), self.Slider_2.value()
        Qx, Qy, Qz = int((x/400)*self.Width), int((y/400)*self.Height), z
        self.pixvalue = self.imbeads[Qz, Qy, Qx]
        
        if self.pixvalue==0:
            print(colored(f'Clicked on the background', 'red'))
        else:
            print(colored(f'Clicked on bead # {self.pixvalue}', 'green'))
                          
    def AnalyzeBEAD(self):
        '''
        Takes a pixel value of the binary picture, crops the corresponding bead
        plots its cross section in Canvas_3 and calls ExpandAndSave
        
        '''
        if self.pixvalue==0:
            print(colored('You have not clicked on a bead yet!', 'red'))
        else:
            # crop picture to only contain our desired bead
            buffer=5
            coords = np.where(self.imbeads==self.pixvalue)
            lim_z = [np.min(coords[0])-buffer, np.max(coords[0])+buffer]
            lim_y = [np.min(coords[1])-buffer, np.max(coords[1])+buffer]
            lim_x = [np.min(coords[2])-buffer, np.max(coords[2])+buffer]
            
            # cropped, masked, segmented and binary versions 
            crop = self.imbeads[lim_z[0]:lim_z[1], lim_y[0]:lim_y[1], lim_x[0]:lim_x[1]]
            self.masked = (crop==self.pixvalue)*1
            
            # show central slice
            Qimg_cropped = self.apply_colormap(self.masked[int(np.shape(crop)[0]/2),:,:], self.cmap_glasbey)
            self.Canvas_3.setPixmap(QtGui.QPixmap.fromImage(Qimg_cropped))
            
            # Expand and save the SHTable, using the current masked picture
            self.ExpandAndSave()
            
            # Load the table and do magic:
            '''
            To be implemented
            '''
            print('The stress is being calculated')
                  
    def ExpandAndSave(self):
        '''
        Takes the current surface picture (as per the last bead clicked),
        calculates its SH expansion,and saves the SHTable
        It should also generate the 2D and 3D plots, to which ANALYZEBEAD will call back 
        '''
        surface = cle.detect_label_edges(self.masked)
        im_binary = cle.pull(surface).astype(bool)   
        
        px, pz = float(self.INPUT_pxy.text()), float(self.INPUT_pz.text())
        SHOrd = int(self.INPUT_SH_Order.text())

        self.OptimalRotation = C20_optimization(im_binary, SHOrd, px, pz)
        self.Coord, self.Coord_orig, self.SHTable, self.FitCoord = C20_rotation_outputs(self.OptimalRotation, im_binary, SHOrd, px, pz)

        # Save SHTable as .npy
        self.FolderSaveName = self.FolderName + '/SH_Analysis/'
        if not os.path.exists(self.FolderSaveName):
            os.mkdir(self.FolderSaveName)
        
        self.ArraySaveName = self.FolderSaveName+'/'+'SH_Array_Bead_'+str(self.pixvalue).zfill(4)+'.npy'
        np.save(self.ArraySaveName, self.SHTable)
        



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
