from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal
from PyQt6 import uic
from logger import log
from message import Message

class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str)

    def __init__(self, username):
        super().__init__()
        uic.loadUi("gui\main_window.ui", self)
        self.username = username
        self.contact_list = []

    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)
        self.add_contact("General")

    def send_message(self):
        log.d("Кнопка нажата")
        textEdit = self.findChild(QTextEdit, "MessageToSend")
        message = textEdit.toPlainText()
        self.sendMessage.emit(message)
        textEdit.clear()

    def show_message(self, message: Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        display.append(f"[{message.time}]  <{message.senderName}>:    {message.text}")

    def add_contact(self, name_contact):
        contactList: QVBoxLayout = self.findChild(QVBoxLayout, "ContactList")
        new_contact = QLabel(text=name_contact)
        contactList.addWidget(new_contact)
        self.contact_list.append(new_contact)