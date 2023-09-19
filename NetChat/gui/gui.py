from PyQt6.QtCore import QThread, pyqtSignal
from PyQt6.QtWidgets import *
from PyQt6 import uic

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/main.ui", self)
        
class Gui(QThread):
    sendMessage = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.window = MainWindow()
        self.window.show()
        
    def run(self):
        print("Gui is runnig")
        button = self.window.findChild(QPushButton, "pushButton")
        button.clicked.connect(self.send_message)
        
    def send_message(self):
        print("Button pressed")
        text = self.window.findChild(QTextEdit, "MessageToSend")
        message = text.toPlainText()
        self.sendMessage.emit(message)
        text.clear()        