from PyQt5 import QtCore
from PyQt5.QtCore import QThread

import Wrap_asyncIo
import globalValue

import loggingMd as lggMd

class FileReadWorker(QThread):
    #parent = MainWidget을 상속 받음.
    def __init__(self):
        super().__init__()
        
    def SetFile(self, file_name):
        self.file_name = file_name
    
    def run(self):
        lggMd.LogObj.info('run File Read Worker')
        globalValue.loop.run_until_complete(Wrap_asyncIo.get_spec(self.file_name))
        globalValue.loop.close()