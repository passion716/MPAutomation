from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5.QtCore import QThread
import loggingMd as lggMd

class Worker(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self):
        super().__init__()
        self.nCnt = 0
        self.nPer = 0
        self.nAll = 0

        self.Progressdlg = QtWidgets.QProgressDialog()
        self.Progressdlg.setAutoClose(True)
        self.Progressdlg.setRange(0, 100)
        self.Progressdlg.setWindowModality(QtCore.Qt.NonModal)
        self.Progressdlg.setWindowTitle('File Read')
        lggMd.LogObj.info('Init Work')

    def SetAllCnt(self, nAll):
        self.nAll = nAll
        lggMd.LogObj.info(f'Work All cnt : {self.nAll}')
    
    def SetIncreate(self, nSet = 0):

        if nSet is not 0:
            self.nCnt = 0
            self.nAll = 0
            self.nPer = 0
            lggMd.LogObj.info('SetIncreate Reset')
            return;

        self.nCnt +=1
        self.nPer = int((self.nCnt / self.nAll) * 100)
        self.run()
        
    def run(self):
        self.Progressdlg.show()
        self.Progressdlg.setValue(self.nPer)