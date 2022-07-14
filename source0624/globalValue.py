from asyncore import loop
import asyncio
import Work

def initloop():
    global loop
    loop = asyncio.get_event_loop()

def initResult():
    global results
    results = []

def InitProgressDia():
    global proDlg
    proDlg = Work.Worker()