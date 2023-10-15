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
        hostname = socket.gethostname()
        ip_adr = socket.gethostbyname(hostname)
        self.address = (ip_adr, 9900)
        self.running = False
    
    def run(self):
        log.i("Receiver is running")
        self.socket.bind(self.address)
        self.running = True

        while self.running:
            data, addr = self.socket.recvfrom(4096)
            received_string = data.decode(encoding="utf-8")
            log.d(f'received message from {addr}: {received_string}')
            msg = Message(received_string)
            msg.senderIp = addr[0]
            if msg.type == 'service_request' and msg.text.lower() == 'hello':
                self.hello.emit(msg)
            else:
                self.message.emit(msg) 

    def stop(self):
        self.running = False
        super().stop()