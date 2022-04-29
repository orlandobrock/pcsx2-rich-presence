from pypresence import Presence
import emulador
from time import sleep, time
from os import system


RPC = Presence("YOUR_CLIENT_ID")
RPC.connect()

def setStatusEmulator(emulatorState):
    RPC.update(state=emulatorState, large_image="logo", large_text="PCSX2")

def setStatus(gameName, counter):
    RPC.update(state=gameName, start=counter ,large_image="logo", large_text="PCSX2")




ActualGame = ""
isRunningEmulator = False        
while True:
    try:
        system("cls")
        print("===========================================================")
        print("|            Rich Presence PCSX2 inicializado             |")
        print("===========================================================")
        emulator = emulador.Emulador()
        if(emulator.gameIsRunning() and emulator.getGameName() != ActualGame):
            setStatus(emulator.getGameName(), time())
            ActualGame = emulator.getGameName()
        elif(not emulator.gameIsRunning() and not isRunningEmulator):
            setStatusEmulator("Main Menu")
            ActualGame = ""
        isRunningEmulator = True
    except:
        if(isRunningEmulator):
            RPC.update()
        isRunningEmulator = False
        system("color 0a")
        system("cls")
        print("===========================================================")
        print("|   o PCSX2 não está em execução ou não está em memória   |")
        print("===========================================================")
    sleep(5)