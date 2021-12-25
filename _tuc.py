from tkinter import *
from tkinter import ttk, messagebox
timeUnits, tus_seconds, spaceStrings = ["Second(s)", "Minute(s)", "Hour(s)", "Day(s)", "Week(s)", "Month(s)", "Year(s)", "Decade(s)", "Century(s)"], [1, 60, 3600, 86400, 604800, 2419200, 29030400, 290304000, 2903040000], ["                                       ", "                                                                 "]
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
def leftside_conversion(event): # Put the converted amount into the right side.
    try:
        inputedAmount = float(leftSide_Entry.get())
    except:
        pass
    conversionResult = (inputedAmount * tus_seconds[findElement_index(timeUnits, str(leftSide_option.get()))]) / tus_seconds[findElement_index(timeUnits, str(rightSide_option.get()))]
    rightSide_Entry.delete(0, END)
    rightSide_Entry.insert(0, str(conversionResult))
def rightside_conversion(event): # Put the converted amount into the left side.
    try:
        inputedAmount = float(rightSide_Entry.get())
    except:
        pass
    conversionResult = (inputedAmount * tus_seconds[findElement_index(timeUnits, str(rightSide_option.get()))]) / tus_seconds[findElement_index(timeUnits, str(leftSide_option.get()))]
    leftSide_Entry.delete(0, END)
    leftSide_Entry.insert(0, str(conversionResult))
root = Tk()
root.geometry("700x110")
root.resizable(False, False)
root.title("Time Units Convertor")
equal_sign = ttk.Label(root, text="=")
equal_sign.configure(font=("Times New Roman", 45))
equal_sign.place(x=330, y=12)
ttk.Label(root, text=spaceStrings[0] + "Select any unit you want, and input how much of that unit you want to convert on any side." + spaceStrings[1], background="gray").place(x=0)
leftSide_Entry = ttk.Entry(root, width=45)
leftSide_Entry.focus_force()
leftSide_Entry.bind("<Return>", lambda event: leftside_conversion(leftSide_Entry))
leftSide_Entry.place(x=5, y=30, height=30)
rightSide_Entry = ttk.Entry(root, width=45)
rightSide_Entry.bind("<Return>", lambda event: rightside_conversion(rightSide_Entry))
rightSide_Entry.place(x=420, y=30, height=30)
leftSide_option = StringVar()
leftSide_option.set("Second(s)")
leftSide_Menu = OptionMenu(root, leftSide_option, *timeUnits, command=lambda event: leftside_conversion(leftSide_Entry))
leftSide_Menu.configure(width=39)
leftSide_Menu.place(x=4, y=65)
rightSide_option = StringVar()
rightSide_option.set("Second(s)")
rightSide_Menu = OptionMenu(root, rightSide_option, *timeUnits, command=lambda event: rightside_conversion(rightSide_Entry))
rightSide_Menu.configure(width=39)
rightSide_Menu.place(x=420, y=65)
root.mainloop()
