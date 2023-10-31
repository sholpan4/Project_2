from PyQt6.QtCore import QThread, pyqtSignal
from logger import log


class DataStorage(QThread):
    username = None
    password = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)
    def_user = "Dauren"
    def_password = "123"

    def run(self):
        log.i("Data storage started")
        self.ready.emit()
       
    def auth(self, username, password):
        with open("data_storage/user.db", "r", encoding="UTF-8") as user_file:
            user_data = user_file.read().split()

        if username == user_data[0] and password == user_data[1]:
            self.authOk.emit(username)
        else:
            self.authBad.emit("Неправльное имя или пароль!")
