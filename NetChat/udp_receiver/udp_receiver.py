import socket
from PyQt6.QtCore import QThread

# этот класс черновик-пример ))
class UdpReceiver(QThread):
    
    def __init__(self):
        super().__init__
        my_address = ('localhost', 9900)
        my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        my_socket.bind(my_address)

   

    def run(self, my_socket):
        is_running = True

        while is_running:
            data, addr = my_socket.recvform(1024)
            message = data.decode(encoding="utf-8")
            print(f'received message from {addr}: {message}')
            if message == 'exit':
                is_running = False

    def stop(self):
        pass