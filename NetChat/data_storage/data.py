from PyQt6.QtCore import QThread

class DataStorage(QThread):
    def auth(self, username):
        self.username = username