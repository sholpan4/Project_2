from PyQt6.QtCore import QThread, pyqtSignal
import socket
import time
import datetime
from logger import log
import threading
from message import Message


class UdpSender(QThread):
    _queue = []
    sent = pyqtSignal(Message)


    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False
        self.lock = threading.Lock()

    def run(self):
        log.i("Сэндер запущен")
        self.running = True
        msg : Message = None
        while self.running:
            if len(self._queue) > 0:
                self.lock.acquire()
                msg = self._queue.pop()
                self.lock.release()
                msg.time = datetime.datetime.now().strftime('%H:%M:%S')
                string_to_send = msg.toJson()
                self.socket.sendto(string_to_send.encode(), self.addres)
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
