import tkinter as tk
from tkinter import ttk
import random
from time import sleep

grabbelList = ["laptop", "toetsenbord", "muis", "muismat", "headset", "telefoon", "tas", "brooddoos", "waterfles", "opladers", "stroopwafelpakje", "pennen", "schriften", "portomonee", "stoel"]
ammoutItems = len(grabbelList)

window = tk.Tk()
window.title('De grabbelton')
button = tk.Button(text="grabbelen", bg="white", fg="black")
button.pack(pady = 20, padx = 20)
label = ttk.Label(window, text=('Aantal grabbeltjes: {}'.format(ammoutItems)), font=('Helvetica', 14))
label.pack(ipadx= 10, ipady= 10)

def updateTon():
    global ammoutItems
    chosenIndex = random.randrange(0,ammoutItems)
    ammoutItems -= 1
    print("U hebt het volgende gegrabbelt:", grabbelList[chosenIndex])
    del grabbelList[chosenIndex]
    label.config(text=('Aantal grabbeltjes: {}'.format(ammoutItems)))
    if ammoutItems == 0:
        sleep(1)
        print("Gefeliciteerd!!! U hebt alles gebrabbelt wat er gegrabbelt kon worden.")
        sleep(4)
        print("Maar wist je dat je helemaal niks gebrabbelt hebt...")
        sleep(3)
        print("maar dat je eigenlijk iemands huis heb beroofd?")
        sleep(4)
        print("En nu gauw wegwezen voordat je aangehouden wordt :)")
        sleep(3)
        window.destroy()

button.config(command=updateTon)

window.mainloop()