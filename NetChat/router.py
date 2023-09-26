from PyQt6.QtCore import QObject
from logger import log
from gui import Gui
from data_storage import DataStorage
from udp_receiver import UdpReceiver
from udp_sender import UdpSender
from controller import Controller


class Router(QObject):
    def __init__(self):
        super().__init__()
        self.data_storage = DataStorage()
        self.gui = Gui()
        self.udp_receiver = UdpReceiver()
        self.udp_sender = UdpSender()
        self.controller = Controller()
        # Здесь будем роутить сигналы
        
        # сигналы GUI 
        # self.gui.sendMessage.connect(lambda s: print(s))
        self.gui.loginUser.connect(self.data_storage.auth)
        self.gui.loginUser.connect(self.controller.login)
        
        # сигналы Controller
        self.controller.switchWindow.connect(self.gui.set_window)
        
        # сигналы UdpReceiver
        self.udp_receiver.message.connect(self.controller.message_received)
        self.gui.sendMessage.connect(self.udp_sender.send)
        
        self.udp_receiver.message.connect(self.gui.show_message)

    def start(self):
        log.i("Стартуем роутер")
        self.data_storage.start()
        self.gui.start()
        self.udp_receiver.start()
        self.udp_sender.start()

    def stop(self):
        self.udp_sender.stop()
        self.udp_receiver.stop()
        self.gui.stop()
        self.data_storage.stop()