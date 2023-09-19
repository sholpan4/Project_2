import sys
from PyQt6.QtWidgets import QApplication
from router import Router
from udp_receiver import *
from udp_sender import *
# from logger import Logger

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # log = Logger(Logger.DEBUG)
    
    route = Router()
    route.start()
    
    app.exec()