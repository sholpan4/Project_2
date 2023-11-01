from PyQt6.QtCore import QThread, pyqtSignal
from logger import log
import json
import hashlib


class DataStorage(QThread):
    username = None
    password = None
    ready = pyqtSignal()
    authOk = pyqtSignal(str)
    authBad = pyqtSignal(str)

    def run(self):
        log.i("Data storage started")
        self.ready.emit()
       
    def auth(self, username, password):
            with open('data_storage/users.json', 'r') as jsn_file:
                for line in jsn_file:
                    user = json.loads(line)
                    if hashlib.md5(username.encode("UTF-8")).hexdigest() == user["username"] and hashlib.md5(password.encode("UTF-8")).hexdigest() == user["password"]:
                        self.authOk.emit(username)
                        return

            self.authBad.emit("Неправильное имя или пароль!")


    def reg(self, email, username, password): 
        email_hsh =  hashlib.md5(email.encode("UTF-8"))
        email_hsh_result = email_hsh.hexdigest()

        username_hsh = hashlib.md5(username.encode("UTF-8"))
        username_hsh_result = username_hsh.hexdigest()

        password_hsh = hashlib.md5(password.encode("UTF-8"))
        password_hsh_result = password_hsh.hexdigest()
        user = {"email": email_hsh_result, "username": username_hsh_result, "password": password_hsh_result}
        self.authOk.emit(username)

        with open('data_storage/users.json', 'a') as json_file:
            json_file.write('\n')
            json.dump(user, json_file)
