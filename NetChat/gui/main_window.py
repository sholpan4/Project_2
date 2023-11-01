from PyQt6.QtWidgets import *
from PyQt6.QtCore import pyqtSignal, Qt
from PyQt6 import uic
from logger import log
from message import Message
from PyQt6.QtGui import QTextCursor

class MainWindow(QMainWindow):
    sendMessage = pyqtSignal(str, str)


    def __init__(self, username):
        super().__init__()
        uic.loadUi("gui\main_window.ui", self)
        self.username = username
        self.contact_list = []

    def show(self):
        super().show()
        self.menu = QMenu(self)
        self.grid = QGridLayout()
        self.menu.setStyleSheet('border-radius: 10px;')
        button = self.findChild(QPushButton, "Send")
        button.clicked.connect(self.send_message)
        self.add_contact("General")
        self.button_e = self.findChild(QPushButton, "emoji")
        self.open_menu()
        self.textedit = self.findChild(QTextEdit, "MessageToSend")
        self.textedit.keyPressEvent = self.my_keyPressEvent
        self.menu.setLayout(self.grid)
  
 
        

    def send_message(self):
        self.message = self.textedit.toPlainText()
        self.sendMessage.emit(self.message, "public")
        self.textedit.clear()


    def process_key_event(self, event):
            modifiers = event.modifiers()
            key = event.key()

            if key not in [Qt.Key.Key_Enter, Qt.Key.Key_Return, Qt.Key.Key_Backspace]:
                text = self.textedit.toPlainText()
                text += event.text()
                self.textedit.setText(text)
                cursor = self.textedit.textCursor()
                cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.MoveAnchor, len(text) + 1)
                self.textedit.setTextCursor(cursor)
            elif key in [Qt.Key.Key_Enter, Qt.Key.Key_Return]:
                if modifiers == Qt.KeyboardModifier.ShiftModifier:
                    self.insert_newline()
                else:
                    self.send_message()
            elif key == Qt.Key.Key_Backspace:
                if modifiers == Qt.KeyboardModifier.NoModifier:
                    self.remove_last_character()
                else:
                    self.move_cursor_to_end_of_word()

    def insert_newline(self):
            text = self.textedit.toPlainText()
            text += "\n"
            self.textedit.setText(text)
            cursor = self.textedit.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.Down, QTextCursor.MoveMode.MoveAnchor, len(text) + 1)
            self.textedit.setTextCursor(cursor)

    def remove_last_character(self):
            text = self.textedit.toPlainText()
            text = text[:-1]
            self.textedit.setText(text)
            cursor = self.textedit.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.EndOfWord, QTextCursor.MoveMode.MoveAnchor, len(text) + 1)

    def move_cursor_to_end_of_word(self):
            cursor = self.textedit.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.EndOfWord, QTextCursor.MoveMode.MoveAnchor)
            self.textedit.setTextCursor(cursor)
            

    def send_message(self):
            self.message = self.textedit.toPlainText()
            self.sendMessage.emit(self.message, "public")
            self.textedit.clear()

    def my_keyPressEvent(self, event):
            self.process_key_event(event)

    def create_button(self, emoji_code):
        button = QPushButton(chr(emoji_code))
        button.setFixedSize(15, 15)
        button.setStyleSheet(' border: none;')
        button.clicked.connect(lambda _, code=emoji_code: self.textedit.insertPlainText(chr(code)))
        return button

    def open_menu(self):
        smiles = [["\U0001F600", 0x1F600, 0, 0], ["\U0001F601", 0x1F601, 0, 1], ["\U0001F602", 0x1F602, 0, 2],
                  ["\U0001F603", 0x1F603, 0, 3], ["\U0001F604", 0x1F604, 0, 4],
                  ["\U0001F605", 0x1F605, 1, 0], ["\U0001F606", 0x1F606, 1, 1], ["\U0001F607", 0x1F607, 1, 2],
                  ["\U0001F608", 0x1F608, 1, 3], ["\U0001F609", 0x1F609, 1, 4],
                  ["\U0001F60A", 0x1F60A, 2, 0], ["\U0001F60B", 0x1F60B, 2, 1], ["\U0001F60C", 0x1F60C, 2, 2],
                  ["\U0001F60D", 0x1F60D, 2, 3], ["\U0001F60E", 0x1F60E, 2, 4],
                  ["\U0001F60F", 0x1F60F, 3, 0], ["\U0001F610", 0x1F610, 3, 1], ["\U0001F611", 0x1F611, 3, 2],
                  ["\U0001F612", 0x1F612, 3, 3], ["\U0001F613", 0x1F613, 3, 4],
                  ["\U0001F614", 0x1F614, 4, 0], ["\U0001F615", 0x1F615, 4, 1], ["\U0001F616", 0x1F616, 4, 2],]



        for emoji, code, row, col in smiles:
            button = self.create_button(code)
            self.grid.addWidget(button, row, col)


    def show_message(self, message: Message):
        display = self.findChild(QTextBrowser, "MessageDisplay")
        text = f'[{message.time}]  <{message.senderName}>:    {message.text}     '
        display.append(text)

    def add_contact(self, name_contact):
        contactList: QVBoxLayout = self.findChild(QVBoxLayout, "ContactList")
        new_contact = QLabel(text=name_contact)
        contactList.addWidget(new_contact)
        self.contact_list.append(new_contact)

