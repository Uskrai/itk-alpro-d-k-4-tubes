import sys
import abc
from PyQt5.QtWidgets import QApplication,QMainWindow
from PyQt5.QtCore import Qt, QObject
from base.controller import ControllerBase
from .interfaces import InterfacesGUI
from .main_widget import MainWidget
from base.modul import Modul

class ControllerGUI(  ControllerBase, ):
    def __init__( self ):
        self.app = QApplication( sys.argv )

        self._window = QMainWindow()
        self._window.setWindowTitle("Rumus fisdas")
        self._window.setGeometry(300,300,400,400)

        self._widgets = MainWidget( self._window )
        self._window.setCentralWidget( self._widgets )
        self._label = []
        self._label_tree = {}
        self._modul = {}

        self._interfaces = InterfacesGUI
    
    def start(self, modul : dict ):
        self._modul = modul
        self._widgets.set_modul( modul )
        self._widgets.start()

        self._window.setCentralWidget( self._widgets )
        self._window.show()
        self.app.exec_()