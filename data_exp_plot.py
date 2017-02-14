import sys
from PyQt4 import QtGui, QtCore
import ConfigParser
import numpy as np
#from analyser import Analyser
#from fit_config_Widget import CfgWidget

from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)


class MainWindow(QtGui.QWidget):
    def __init__(self,title):
        super(MainWindow,self).__init__()
        self.initUI(title)

    def initUI(self,title): 
        QtGui.QToolTip.setFont(QtGui.QFont('SansSerif', 10))        
        
        self.mplvl = QtGui.QVBoxLayout() 
        self.mplwindow = QtGui.QWidget()
        self.data_exp_btn = QtGui.QPushButton(self)
        self.data_exp_btn.setText('Save data')
        self.data_exp_btn.clicked.connect(self.save_line)        
        
        self.mplvl.addWidget(self.data_exp_btn)
        self.setLayout(self.mplvl)   
        
        self.setGeometry(500, 400, 600, 400)
        self.setWindowTitle(title)   
        self.show()
#        x = np.linspace(0,10)
#        y = np.linspace(0,20)
#        f = Figure()
#        self.ax1 = f.add_subplot(111)
#        self.ax1.plot(x,y)
#        self.addmpl(f)
        
    def addmpl(self, fig):
        self.canvas = FigureCanvas(fig)
        
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, 
                        self.mplwindow, coordinates=True)
        self.mplvl.addWidget(self.toolbar)    
        self.mplvl.addWidget(self.canvas)
        
    def save_line(self):
        axes = self.canvas.figure.get_axes()
        for i1,ax in enumerate(axes):
            for i2, line in enumerate(ax.get_lines()):
                xy = line.get_xydata()
                np.savetxt(str(i1)+str(i2)+'.txt',xy,delimiter = '\t')

        

        
def main():


    # Start application    
    app = QtGui.QApplication(sys.argv)
    ex = MainWindow()
    ret = app.exec_()
#    sys.exit(app.exec_())

    
if __name__ == '__main__':
    main()
    










    
