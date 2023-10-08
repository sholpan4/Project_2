from PyQt6.QtCore import QThread, pyqtSignal
from logger import log


class DataStorage(QThread):
    username = None
    password = None # ?
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)

    def run(self):
        log.i("Data storage started")
        self.ready.emit()
       
    def auth(self, username):
        self.username = username
        self.authOk.emit(username)
        
    def login(self, username, password):
        if self.username == username:
            if self.password == password:
                pass # нужно доработать