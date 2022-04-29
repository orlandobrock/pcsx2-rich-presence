from pymem import *
from pymem.process import *
import time
class Emulador:
    def __init__(self):
            self.pm = Pymem("pcsx2.exe")
            self.baseAddress =  self.pm.base_address
            self.offsets = [0x54] # Segmento do texto do jogo (Não mexer)
            self.STRING_SIZE = 100 
    
    def calculateMemoryAddress(self, address):
        return self.pm.read_int(self.baseAddress + address)
    
    def getGameName(self):
        if(self.gameIsRunning):
            for offset in self.offsets:
                valor = self.pm.read_string(self.calculateMemoryAddress(0x23C08B0) + offset, self.STRING_SIZE)
            return valor

        
    def gameIsRunning(self):
        if (module_from_name(self.pm.process_handle, 'version.dll') != None):
            return True
        else:
            return False