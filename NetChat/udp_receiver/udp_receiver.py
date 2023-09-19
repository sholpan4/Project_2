from PyQt6.QtCore import QThread

class UdpReceiver(QThread):
    def run(self):
        print("Receiver is running")