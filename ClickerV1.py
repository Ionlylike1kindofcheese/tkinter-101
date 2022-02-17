import tkinter as tk
from functools import partial

window = tk.Tk()
window.title("Clicker V1")
window.config(bg='grey')

numberStatus = 0

def showNumberstatus():
    print('Het huidige nummer is:', str(numberStatus))


def update(commandAction):
    global numberStatus
    if commandAction == 'increase':
        print("increase comfirmed")
        numberStatus += 1
    elif commandAction == 'decrease':
        print("decrease comfirmed")
        numberStatus -= 1
    
    if numberStatus > 0:
        window.config(bg='green')
    elif numberStatus < 0:
        window.config(bg='red')
    elif numberStatus == 0:
        window.config(bg='grey')
    
    list[1].config(text=numberStatus)


list = []
textStrings = ["up", numberStatus, "down"]
for x in range(3):
    list.append(tk.Button(text=textStrings[x]))
    list[x].pack(ipadx=25, ipady=10)

list[0].config(command=partial(update, 'increase'))

list[1].config(command=showNumberstatus)

list[2].config(command=partial(update, 'decrease'))

window.mainloop()