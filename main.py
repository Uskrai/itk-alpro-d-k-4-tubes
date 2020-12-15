from cli.interfaces import InterfacesCLI
from cli.controller import ControllerCLI
import modulfactory

import sys
from enum import Enum

class Mode(Enum):
    GUI = 1
    CLI = 2

def main( mode : Mode ):
    controller = ControllerCLI()
    controller.get_modul( modulfactory.get_all_modul() )
    controller.show()

    exit()

if "--cli" in sys.argv:
    main( Mode.CLI )
else:
    main( Mode.GUI )