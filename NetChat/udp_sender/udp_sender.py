import socket
from PyQt6.QtCore import QThread

# этот класс черновик-пример ))
class UdpSender(QThread):
    address = 'localhost'
    port = 0
    is_running = False

    my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def __init__(self, address, port):
        
        self.address = address
        self.port = port

    def start(self):
        self.run()

    def run(self, is_running, message):
        is_running = True #здесь устанавливаем флаг

        while is_running:
            message = input('')
            my_socket.sendto(message.encode(), server_address)
            # if message =='exit':
            #     is_running = False  эту часть нужно как то в стор передать

    def stop(self):
        super().__stop()
        # здесь убираем флаг, останавливаем только цикл ран с флажком
