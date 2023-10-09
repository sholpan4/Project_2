import socket
from PyQt6.QtCore import QThread, pyqtSignal
from logger import log
import threading #для установки lock 


# этот класс не делала)) 
class UdpSender(QThread):
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = 'localhost'
        self.port = 0
        self.runnning = False #?
   
    def run(self):
        log.d('DEBUG')
        self.running = True

        while self.running:
            message = input('')
            self.socket.sendto(message.encode(), self.address)


