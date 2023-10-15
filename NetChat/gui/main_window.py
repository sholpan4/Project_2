from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
from message import Message


class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        uic.loadUi("gui/main_window.ui", self)
        self.username = username

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)

    def send_message(self):
        log.d("button is pushed")
        textedit = self.findChild(QTextEdit, "MessageToSend")
        message = textedit.toPlainText()
        self.sendMessage.emit(message)
        textedit.clear()

    def show_message(self, msg : Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        display.append(f"{msg.time}| {msg.senderName}:  {msg.text}")