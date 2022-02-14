from datetime import datetime
import tkinter as tk
from time import sleep
import time

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

root = tk.Tk()
root.title('Clock')

label = tk.Label(root)

programkilled = False
seperatedList = []

def disassemblevalues():
    unitList = ["hour", "minute", "second"]
    splitunits = current_time.split(":")
    unitDict = {}
    for index, item in enumerate(splitunits):
        if item.isdigit() == True:
            intUnit = item
        unitDict[unitList[index]] = intUnit
    for position in range(3):
        splitting(unitDict[unitList[position]])
    seperatedDict = {}
    for listItem in unitList:
        for number in range(1,3):
            seperatedDict[(str(listItem) + "_" + str(number))] = int(seperatedList[0])
            del seperatedList[0]
    return seperatedDict


def splitting(string):
    first_half  = string[:len(string)//2]
    second_half = string[len(string)//2:]
    seperatedList.append(first_half)
    seperatedList.append(second_half)


def updateClock(clockDict):
    clockDict['second_2'] += 1
    if clockDict['second_2'] == 10:
        clockDict['second_2'] = 0
        clockDict['second_1'] += 1
        if clockDict['second_1'] == 6:
            clockDict['second_1'] = 0
            clockDict['minute_2'] += 1
            if clockDict['minute_2'] == 10:
                clockDict['minute_2'] = 0
                clockDict['minute_1'] += 1
                if clockDict['minute_1'] == 6:
                    clockDict['minute_1'] = 0
                    clockDict['hour_2'] += 1
                    if clockDict['hour_2'] == 10:
                        clockDict['hour_2'] = 0
                        clockDict['hour_1'] += 1
                    elif clockDict['hour_1'] == 2:
                        if clockDict['hour_2'] == 4:
                            clockDict['hour_2'] = 0
                            clockDict['hour_1'] = 0
    return clockDict


def reassembleClock(clockParts):
    assembledClock = str(clockParts['hour_1']) + str(clockParts['hour_2']) + ':' + str(clockParts['minute_1']) + str(clockParts['minute_2']) + ':' + str(clockParts['second_1']) + str(clockParts['second_2'])
    return assembledClock


def my_mainloop():
    global current_time
    stringVar = tk.StringVar(value=current_time)
    label.config(textvariable=stringVar)
    label.pack()
    print(current_time)

    disassembledClock = disassemblevalues()
    updatedClock = updateClock(disassembledClock)
    current_time = reassembleClock(updatedClock)
    root.after(1000, my_mainloop)

root.after(0, my_mainloop)
root.mainloop()