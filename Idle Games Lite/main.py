import os
import tkinter
from tkinter import *

root = Tk()
root.title('Idle Games LITE')
Label(text='Enter ID Game:').pack(side=TOP,padx=10,pady=10)
GameID = Entry(root, width=100)
GameID.pack(side=TOP,padx=10,pady=10)


def idle():
    GameIDSel  = str(GameID.get())
    #   Open .bat File
    ideling = open("StartIdling.bat","w")
    #   Write in .bat File
    ideling.write("@echo off\n")
    ideling.write("TITLE Execution IdleMode: ON You can close this\n")
    ideling.write("steam-idle.exe ")
    ideling.write(GameIDSel)

    #   Run .bat file
    os.system("start StartIdling.bat")

    # Closure Process
    os.system("exit")
    ideling.close()
    print("Indle Start!")
    print("Game ID: ", GameIDSel)

    

Button(root, text='Idle!', command=idle).pack(side=LEFT)
Button(root, text='Exit', command= root.destroy).pack(side= RIGHT)

root.mainloop()
