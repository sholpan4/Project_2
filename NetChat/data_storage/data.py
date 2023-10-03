from PyQt6.QtCore import QThread
from logger import log


class DataStorage(QThread):
    username = None
    password = None
    
    def run(self):
        log.i("Data storage is running")
        
    def auth(self, username):
        self.username = username
        
    def login(self), username, password):
        if self.username == username:
            if self.password == password:
                pass