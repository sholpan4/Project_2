import socket
from PyQt6.QtCore import QThread
from logger import log

#нужно проверить
class UdpReceiver(QThread):
    
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
            data, addr = self.socket.recvform(1024)
            message = data.decode(encoding= "utf-8")
            log.d(f'received message from {addr}: {message}')

    def stop(self):
        self.running = False
        super().stop()