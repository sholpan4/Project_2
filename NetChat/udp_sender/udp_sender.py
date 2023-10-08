import socket
from PyQt6.QtCore import QThread, pyqtSignal
from logger import log
import time
import datetime
import threading #для установки lock 
from message import Message


class UdpSender(QThread):
    _queue = []
    send = pyqtSignal(Message)
    
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', 9900)
        self.runnning = False
        self.lock = threading.Lock()
   
    def run(self):
        log.i('Sender is runnign')
        self.running = True
        msg : Message = None

        while self.running:
            if len(self._queue) > 0:
                self.lock.acquire()
                msg = self._queue.pop()
                self.lock.release()
                msg.time = datetime.datetime.now().strftime('%H:%M:%S')
                string_to_send = msg.toJson()
                self.socket.sendto(string_to_send.encode(), self.address)
                self.sent.emit(msg)
            else:
                time.sleep(0.025)
    def send(self, msg : Message):
        self.lock.acquire()
        self._queue.append(msg)
        self.lock.release()
        
    def stop(self):
        self.running = False
        super().stop()