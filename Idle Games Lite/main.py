# Version 1.1

import os
import tkinter
from tkinter import *

# Main Menu
root = Tk()
root.title('Idle Games Lite')
root.resizable(width=False, height=False)
Label(text='Enter ID Game:').pack(side=TOP,padx=10,pady=10)
GameID = Entry(root, width=100)
GameID.pack(side=TOP,padx=10,pady=10)


def idle():
    GameIDSel  = str(GameID.get())
    #   Open .bat File
    ideling = open("StartIdling.bat","w")
    #   Write in .bat File
    ideling.write("@echo off\n")
    ideling.write("TITLE You are on IdleMode, don't close this windows until the game idle doesn't run\n")
    ideling.write("color 0C\n")
    ideling.write("echo Hi, please don't close this window until the idle game that you have choose is not running \n")
    ideling.write("echo Steam should be already run\n")
    ideling.write("steam-idle.exe ")
    ideling.write(GameIDSel)

    #   Run .bat file
    os.system("start StartIdling.bat")

    # Closure Process
    os.system("exit")
    ideling.close()
    print("Indle Start!")
    print("Game ID: ", GameIDSel)

def last():
    print("You are running last idle game")
    os.system("start StartIdling.bat")

    

Button(root, text='Idle!', command=idle).pack(side=LEFT)
Button(root, text='Exit', command= root.destroy).pack(side= RIGHT)
Button(root, text='Idle Last Game', command =last).pack(side=BOTTOM)

root.mainloop()
