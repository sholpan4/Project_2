from PyQt6.QtCore import QThread, pyqtSignal
import socket
from logger import log
from message import Message


class UdpReceiver(QThread):
    message = pyqtSignal(Message)
    hello = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.addres = ('localhost', 9900)
        self.running = False


    def run(self):
        log.i("Ресивер запущен")
        self.socket.bind(self.addres)
        self.running = True
        while self.running:
            data, addr = self.socket.recvfrom(4096)
            received_string = data.decode(encoding= "utf-8")
            log.d(f'получено сообщение от {addr}: {received_string}')
            msg = Message(received_string)
            msg.senderIp = addr[0]
            if msg.type == 'serveice_request' and msg.text.lower() == 'hello':
                self.message.emit(msg)
            else:
                self.message.emit(msg)

    def stop(self):
        self.running = False
        super().stop()
