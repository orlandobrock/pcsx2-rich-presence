from pypresence import Presence
import emulador
from time import sleep, time
from os import system
system("color 0a")
system("cls")
RPC = Presence("DEVELOPER TOKEN DISCORD")
RPC.connect()



def setStatusEmulator(emulatorState):
    RPC.update(state=emulatorState, large_image="logo", large_text="PCSX2")

def setStatus(gameName, counter):
    RPC.update(state=gameName, start=counter ,large_image="logo", large_text="PCSX2")


emulator = emulador.Emulador()  
updatedRPC = False
while True:
    if(emulator.startEmulator()):
        system("cls")
        updatedRPC = False
        print("="*59)
        print("|            Rich Presence PCSX2 inicializado             |")
        print("="*59)
        
        if(emulator.gameIsRunning() and emulator.getGameName() != emulator.getActualGame()):
            setStatus(emulator.getGameName(), time())
            emulator.setActualGame(emulator.getGameName())
        elif(not emulator.gameIsRunning() and (emulator.getActualGame() == "" or emulator.getActualGame() != "Main Menu")):
            setStatusEmulator("Main Menu")
            print(emulator.getActualGame())
            emulator.setActualGame("Main Menu")
        
    else:
        system("cls")
        if(not updatedRPC):
            RPC.update()
            updatedRPC = True

        print("="*59)
        print("|            PCSX2 não está em execução!               |")
        print("="*59)

    sleep(5)
