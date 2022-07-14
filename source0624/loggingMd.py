from asyncio.log import logger
from cgitb import handler
import logging as lg
import sys

import datetime as dt

import os

from threading import Thread

def StartLoggging():
    initlogginObj()
    # t = Thread(target= ThreadDayChange)
    # t.start()

def InitFolder():
    
    global strLogPathRoot
     
    try:
        strLogPathRoot = os.path.join(os.getcwd(), "logs")
        if os.path.isdir(strLogPathRoot) is False:
            os.makedirs(strLogPathRoot)
    
        return True
    
    except Exception as Ex:
        return False

import logging.handlers as handlers

def initlogginObj():
    global strLogPathRoot
    global Curtime
    # global logger
    global LogObj
    
    if InitFolder() is False:
        os.abort()
    
    lg.shutdown()
    
    LogFormatter = lg.Formatter("%(asctime)s [%(levelname)s] %(message)s")
  
    strlogFile = os.path.join(strLogPathRoot , "log.txt")
    
    logHandler = handlers.TimedRotatingFileHandler(filename=strlogFile, when='midnight', interval=1, encoding='utf-8')
    logHandler.setFormatter(LogFormatter)
    logHandler.suffix = "%Y%m%d"
    
    LogObj = lg.getLogger()
    LogObj.setLevel(lg.INFO)
    LogObj.addHandler(logHandler)
    
    consolHandler = lg.StreamHandler(sys.stdout)
    consolHandler.setFormatter(LogFormatter)
    
    LogObj.addHandler(consolHandler)

    LogObj.info("Logging Init")
    
   
import time

def ThreadDayChange():
    global Curtime
    
    while(True):
        readTime = dt.datetime.now()
        bChange = readTime.day != Curtime.day
        
        if bChange is True:
            initlogginObj()
        
        time.sleep(1)
    
    
        