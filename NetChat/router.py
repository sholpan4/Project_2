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
        self.gui.sendMessage.connect(self.controller.send_message)
        self.gui.ChangeChat.connect(self.controller.change_chat) #нужно создать ChangeChat() change_chat()

        
        # сигналы Controller
        self.controller.switchWindow.connect(self.gui.set_window)
        self.controller.addContact.connect(self.gui.add_contact) #создать add_contact()
        self.controller.showMessage.connect(self.gui.show_message)
        self.controller.sendMessage.connect(self.udp_sender.send)
        self.controller.setChat.connect(self.gui.set_chat)

        # сигналы UdpReceiver
        self.udp_receiver.message.connect(self.controller.recived_message)
        self.udp_receiver.hello.connect(self.controller.recived_hello)

        # self.udp_receiver.message.connect(self.gui.show_message)
        # self.gui.sendMessage.connect(self.udp_sender.send)
        
        self.data_storage.ready.connect(self.controller.database_ready)
        self.data_storage.authOk.connect(self.controller.database_auth_ok)
        self.data_storage.authBad.connect(self.controller.database_auth_bad)
        

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