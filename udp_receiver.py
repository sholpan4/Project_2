import socket
from PyQt6.QtCore import pyqtSignal
from logger import log
from PyQt6.QtCore import QThread

class UdpReceiver(QThread):
    message = pyqtSignal(str, str)
    hello = pyqtSignal(str)
    def __init__(self):
        super().__init__()
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False


    def run(self):
        print("Udp Receiver started")
        self.server_socket.bind(self.addres)
        while True:
            data, addr = self.server_socket.recvfrom(1024)
            message = data.decode(encoding="UTF-8")
            log.d(f'Получено сообщение от {addr} : {message}')
            self.message.emit(message, 'public')

    def message_reciever(self,message_text,message_type):
        log.d(f"Получено сообщение от {message_text} {message_type}")
    def stop(self):
        self.running = False
        super().stop()