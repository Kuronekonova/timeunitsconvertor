from tkinter import *
from tkinter import ttk, messagebox
import os
timeUnits = ["Second(s)", "Minute(s)", "Hour(s)", "Day(s)", "Week(s)", "Month(s)", "Year(s)", "Decade(s)", "Century(s)"]
tus_seconds = [1, 60, 3600, 86400, 604800, 2.628e+6, 3.154e+7, 3.154e+8, 3.154e+9]
spaceStrings = ["                                       ", "                                                                 "]
def findElement_index(array, num):
    if(num not in array):
        elementIndex = None
        return elementIndex
    else:
        for i in range(len(array)):
            if(array[i] == num):
                elementIndex = i
                return elementIndex
            else:
                continue
def leftside_conversion(event): 
    inputedAmount = leftSide_Entry.entryWidget.get()
    inputedAmount = inputedAmount.replace(",", ".")
    try:
        inputedAmount = float(inputedAmount)
    except:
        rightSide_Entry.entryWidget.delete(0, END)
    conversionResult = (inputedAmount * tus_seconds[findElement_index(timeUnits, str(leftSide_option.get()))]) / tus_seconds[findElement_index(timeUnits, str(rightSide_option.get()))]
    rightSide_Entry.entryWidget.delete(0, END)
    rightSide_Entry.entryWidget.insert(0, str(conversionResult))
def rightside_conversion(event):
    inputedAmount = rightSide_Entry.entryWidget.get()
    inputedAmount = inputedAmount.replace(",", ".")
    try:
        inputedAmount = float(inputedAmount)
    except:
        leftSide_Entry.entryWidget.delete(0, END)
    conversionResult = (inputedAmount * tus_seconds[findElement_index(timeUnits, str(rightSide_option.get()))]) / tus_seconds[findElement_index(timeUnits, str(leftSide_option.get()))]
    leftSide_Entry.entryWidget.delete(0, END)
    leftSide_Entry.entryWidget.insert(0, str(conversionResult))
class windowWidget():
    def __init__(self, mainWindow, windowTitle, windowHeight, windowWidth, trueState, falseState):
        self.mainWindow = mainWindow
        self.windowTitle = windowTitle
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.trueState = trueState
        self.falseState = falseState
        self.mainWindow.title(windowTitle)
        self.mainWindow.geometry(str(windowWidth) + "x" + str(windowHeight))
        self.mainWindow.resizable(trueState, falseState)
        self.mainWindow.focus_force() 
        self.mainWindow.mainloop = mainloop
class entryWidget():
    def __init__(self, entryWidget, entryY_coord, entryX_coord, entry_Width, entry_Height, entry_Command, allow_Focus, bindType):
        self.entryWidget = entryWidget
        self.entryY_coord = entryY_coord
        self.entryX_coord = entryX_coord
        self.entry_Width = entry_Width
        self.entry_Height = entry_Height
        self.entry_Command = entry_Command
        self.allow_Focus = allow_Focus
        self.bindType = bindType
        self.entryWidget.place(x=entryX_coord, y=entryY_coord, height=entry_Height)
        self.entryWidget.configure(width=entry_Width)
        if(allow_Focus == True):
            self.entryWidget.focus_force()
        else:
            pass
        if(self.bindType == "<Return>"):
            self.entryWidget.bind("<Return>", lambda event: self.entry_Command(self.entryWidget))
        elif(self.bindType == "<KeyRelease>"):
            self.entryWidget.bind("<KeyRelease>", lambda event: self.entry_Command(self.entryWidget))
        else:
            pass
class labelWidget(): 
    def __init__(self, labelWidget, labelX_coord, labelY_coord, label_text, label_font, label_bg, label_fg):
        self.labelWidget = labelWidget
        self.labelX_coord = labelX_coord
        self.labelY_coord = labelY_coord
        self.label_text = label_text
        self.label_font = label_font
        self.label_bg = label_bg
        self.label_fg = label_fg
        self.labelWidget.place(x=labelX_coord, y=labelY_coord)
        self.labelWidget.configure(text=self.label_text, font=self.label_font, background=self.label_bg, foreground=self.label_fg)
root = windowWidget(mainWindow=Tk(), windowTitle="Time Units Convertor", windowWidth=700, windowHeight=110, trueState=False, falseState=False)
equal_sign = labelWidget(labelWidget = ttk.Label(root.mainWindow), labelX_coord=330, labelY_coord=12, label_text="=", label_font=("Times New Roman", 45), label_bg=None, label_fg=None)
leftSide_Entry = entryWidget(entryWidget=ttk.Entry(root.mainWindow), entryY_coord=30, entryX_coord=5, entry_Width=45, entry_Height=30, entry_Command=lambda event: leftside_conversion(leftSide_Entry), allow_Focus=True, bindType="<KeyRelease>")
rightSide_Entry = entryWidget(entryWidget=ttk.Entry(root.mainWindow), entryY_coord=30, entryX_coord=420, entry_Width=45, entry_Height=30, entry_Command=lambda event: rightside_conversion(rightSide_Entry), allow_Focus=False, bindType="<KeyRelease>")
labelWidget(labelWidget = ttk.Label(root.mainWindow), labelX_coord=0, labelY_coord=0, label_text=spaceStrings[0] + "Select any unit you want, and input how much of that unit you want to convert on any side." + spaceStrings[1], label_font=None, label_bg="gray", label_fg=None)
leftSide_option = StringVar()
leftSide_option.set("Second(s)")
leftSide_Menu = OptionMenu(root.mainWindow, leftSide_option, *timeUnits, command=lambda event: leftside_conversion(leftSide_Entry))
leftSide_Menu.configure(width=39)
rightSide_option = StringVar()
rightSide_option.set("Second(s)")
rightSide_Menu = OptionMenu(root.mainWindow, rightSide_option, *timeUnits, command=lambda event: rightside_conversion(rightSide_Entry))
rightSide_Menu.configure(width=39)
leftSide_Menu.place(x=4, y=65)
rightSide_Menu.place(x=420, y=65)
root.mainWindow.mainloop()
