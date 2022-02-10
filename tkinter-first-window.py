import tkinter as tk
import random

grootte = 50
countdown = 6

window = tk.Tk()
window.geometry('50x50')
window.title('My First Window')
button = tk.Button(text=str(countdown), bg="white", fg="black")
button.pack(pady = 20, padx = 20)

colourList = ['red', 'orange', 'yellow', 'green', 'blue', 'pink']

def updateWindow():
    global countdown
    global grootte
    print(countdown)
    listIndex = random.randrange(0,6)
    window.config(bg=colourList[listIndex])
    countdown -= 1
    if countdown == 0:
        print("Boom!!!")
        window.destroy()
    else:
        button.config(text=str(countdown))
        grootte += 50
        size = str(grootte) + 'x' + str(grootte)
        window.geometry(size)


button.config(command=updateWindow)

window.mainloop() 