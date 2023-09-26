from PyQt6.QtCore import QObject, pyqtSignal
from logger import log

# state, signal, transition

class Controller(QObject):
    _state = "INIT"
    _transitions = (
        {'from': "INIT", 'to': "LOGIN", 'by': "DB_READY"},
        {'from': "LOGIN", 'to': "AUTH", 'by': "GUI_LOGIN"},
        {'from': "AUTH", 'to': "MAIN_WINDOW", 'by': "DB_AUTH_OK"},
        {'from': "AUTH", 'to': "LOGIN", 'by': "DB_AUTH_BAD"},
        
        {'from': "MAIN_WINDOW", 'to': "ADD_FRIEND", 'by': "UR_HELLO"},
        {'from': "ADD_FRIEND", 'to': "MAIN_WINDOW", 'by': "IMMEDIATELY"},
        
        {'from': "MAIN_WINDOW", 'to': "CHECK_MESSAGE", 'by': "UR_MESSAGE"},
        {'from': "CHECK_MESSAGE", 'to': "MAIN_WINDOW", 'by': "IMMEDIATELY"},
        
        {'from': "MAIN_WINDOW", 'to': "SEND_MESSAGE", 'by': "GUI_SEND"},
        {'from': "GUI_SEND", 'to': "MAIN_WINDOW", 'by': "IMMEDIATELY"},
        
        {'from': "MAIN_WINDOW", 'to': "CHANGING_CHAT", 'by': "GUI_CHAT_CHANGE"},
        {'from': "CHANGING_CHAT", 'to': "MAIN_WINDOW", 'by': "IMMEDIATELY"},
    )
    
    def process_state(self):
        match self._state:
            case "INIT":
                pass
            case "LOGIN":
                pass
            case "AUTH":
                pass
            case "MAIN_WINDOW":
                pass
            case _:
                log.w("Unknown state!")
                
    def process_signal(self, signal_name):
        pass
    
    
    switchWindow = pyqtSignal(str, str)

    def login(self, username):
        if username:
            self.switchWindow.emit('MainWindow', username)
            
    def message_received(self, message_text, message_type):
        log.d(f'Message received: {message_text} type: {message_type}')
            