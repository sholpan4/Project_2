from PyQt6.QtCore import QThread

class UdpSender(QThread):
    def run(self):
        print("Sender is running")