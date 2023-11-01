from logger import log
from PyQt6.QtWidgets import *
from PyQt6 import uic
from PyQt6.QtCore import pyqtSignal
import re 


class RegisterWindow(QDialog):
    registerUser = pyqtSignal(str, str, str)
    loginWindow = pyqtSignal()#

    def __init__(self):
        super().__init__()
        uic.loadUi("gui/register_window.ui", self)
        
    def show(self):
        super().show()
        button = self.findChild(QPushButton, "Register")
        button.clicked.connect(self.register_user)
        log_button = self.findChild(QPushButton, "Auth")#
        log_button.clicked.connect(self.show_auth_window)#

        self.email_input = self.findChild(QLineEdit, "Email")
        self.name_input = self.findChild(QLineEdit, "Nickname")
        self.password_input = self.findChild(QLineEdit, "Password")
        self.confirmPassword_input = self.findChild(QLineEdit, "Confirm_pass")
    
    def check_password(self, password):
        if len(password) < 7:
            return False
        return re.match(r'^(?=.*[A-Za-z])(?=.*\d)(?=.*[@#$%^!&*])[A-Za-z\d@#$%^!&*]+$', password)


    def check_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email)
    

    def show_auth_window(self):
        self.loginWindow.emit()#


    def register_user(self):
        user_email = self.email_input.text()
        user_name = self.name_input.text()
        user_password = self.password_input.text()
        user_confirm_pass = self.confirmPassword_input.text()

        if user_email and user_name and user_password and user_confirm_pass: 
            if not self.check_email(user_email):
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 15px;'>Некорректный формат электронной почты!</p>")
            elif not self.check_password(user_password):
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 15px;'>Пароль не соответствует необходимым критериям безопасности!</p>")
            elif user_password != user_confirm_pass:
                QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 15px;'>Пароли не совпадают!</p>")
            else:
                self.registerUser.emit(user_email, user_name, user_password)
        else:
            QMessageBox.critical(None, "Ошибка", "<p style='color: red; font-size: 15px;'>Заполните все данные!</p>")