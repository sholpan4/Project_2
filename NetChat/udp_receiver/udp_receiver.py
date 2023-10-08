import socket
from PyQt6.QtCore import QThread, pyqtSignal
from logger import log
from message import Message


class UdpReceiver(QThread):
    message = pyqtSignal(Message)
    hello = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.address = ('localhost', 9900)
        self.running = False  

    def run(self):
        log.i("Receiver is running")
        self.socket.bind(self.address)
        self.running = True

        while self.running:
            data, addr = self.socket.recvform(4096)
            received_string = data.decode(encoding= "utf-8")
            log.d(f'received message from {addr}: {received_string}')
            msg = Message(received_string)
            self.message.emit(msg)
            
    def stop(self):
        self.running = False
        super().stop()