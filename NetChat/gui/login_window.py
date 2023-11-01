from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal


class LoginWindow(QDialog):
    loginUser = pyqtSignal(str, str)
    registerWindow = pyqtSignal()

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/login_window.ui", self)

    def show(self):
        super().show()
        log_button = self.findChild(QPushButton, "Login")
        log_button.clicked.connect(self.login_user)
        reg_button = self.findChild(QPushButton, "Register")
        reg_button.clicked.connect(self.show_reg_window)

        

    def login_user(self):
        name_input = self.findChild(QLineEdit, "Nickname")
        login_input = self.findChild(QLineEdit, "Password")
        user_name = name_input.text()
        user_password = login_input.text()
        if user_name and user_password:
            self.loginUser.emit(user_name, user_password)
        elif user_name == "" or user_password == "":
            self.show_error("Заполните все данные!")
        

    def show_reg_window(self): 
        self.registerWindow.emit()
        log.i("Открытие окна регистрации!")

    def show_error(self, error_message):
        QMessageBox.critical(None, "Ошибка", f"<p style='color: red; font-size: 15px;'>{error_message}</p>")