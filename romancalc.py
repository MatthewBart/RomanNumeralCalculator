# Import Tkinter
from cgitb import text
from tkinter import *
from tkinter.ttk import LabeledScale 


# Functions
# Conversion of Roman Numerals to Integer
def convertRomanToInt(rString):    
    romanKeyMap = dict({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,})
    solution = romanKeyMap[(rString[(len(rString)-1)])]
    # Loop through and compare each letter to determine if it will be placed before or after the current letter
    for x in reversed(range(len(rString)-1)):
        if romanKeyMap[rString[x]] < romanKeyMap[rString[x+1]]:
            solution -= romanKeyMap[rString[x]]
        else:
            solution += romanKeyMap[rString[x]]
    # Clear the current variable
    # Dynamically display the solution
    convertVariable.clear()
    result2.configure(text="Result: %s" % solution)

# Function to convert Integer to Roman
def convertIntegerToRoman(rInt):
    rInt=int(rInt)
    # Define arrays for each type of letter
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    # Clear the current variable
    convertVariable.clear()
    # Compare the converting integer to each array and convert
    solution=(M[rInt // 1000] + C[(rInt % 1000) // 100] + X[(rInt % 100) // 10] + I[rInt % 10])
    # Dynamically update the result
    result.configure(text="Result: %.10s" % solution)

# Swap Frame by raising the next window/frame
def swapFrame(frame):
    frame.tkraise()

# Append the number/letter to the variable to convert
def addToList(number):
    convertVariable.append(number)
    

# Define the input variable and tkinter root
convertVariable = []
displayRoot = Tk()  

# Define frames
startFrame = Frame(displayRoot)
integerToRomanFrame = Frame(displayRoot)
romanToIntFrame = Frame(displayRoot)
displayRoot.geometry("400x400")
displayRoot.minsize(400, 400)
displayRoot.maxsize(400, 400)

startFrame.grid(row=0, column=0, sticky='news')
integerToRomanFrame.grid(row=0, column=0, sticky='news')
romanToIntFrame.grid(row=0, column=0, sticky='news')

# Set background
startFrame.configure(bg='black')
integerToRomanFrame.configure(bg='black')
romanToIntFrame.configure(bg='black')

# Start Menu
Label(startFrame, text='Choose Calculation', height=8, width=15, fg='white', bg='black').grid(row=0,column=1)
Button(startFrame, text='Integer To Roman', command=lambda:swapFrame(integerToRomanFrame), height=8, width=19, fg='white', bg='black').grid(row=1,column=0)
Button(startFrame, text='Roman To Integer', command=lambda:swapFrame(romanToIntFrame), height=8, width=19, fg='white', bg='black').grid(row=1,column=2)

# Layout for Integer To Roman Frame
# Each button calls the addToList function to add the current number to the input
Label(integerToRomanFrame, text='Enter in your number',height=3,width=22, fg='white', bg='black').grid(row=0,column=1)
Button(integerToRomanFrame, text=' 1 ', fg='white', bg='black',
                command=lambda: addToList("1"), height=3, width=15).grid(row=1, column=0)
Button(integerToRomanFrame, text=' 2 ', fg='white', bg='black',
                command=lambda: addToList("2"), height=3, width=15).grid(row=1, column=1)
Button(integerToRomanFrame, text=' 3 ', fg='white', bg='black',
                command=lambda: addToList("3"), height=3, width=15).grid(row=1, column=2)
Button(integerToRomanFrame, text=' 4 ', fg='white', bg='black',
                command=lambda: addToList("4"), height=3, width=15).grid(row=2, column=0)
Button(integerToRomanFrame, text=' 5 ', fg='white', bg='black',
                command=lambda: addToList("5"), height=3, width=15).grid(row=2, column=1)
Button(integerToRomanFrame, text=' 6 ', fg='white', bg='black',
                command=lambda: addToList("6"), height=3, width=15).grid(row=2, column=2)
Button(integerToRomanFrame, text=' 7 ', fg='white', bg='black',
                command=lambda: addToList("7"), height=3, width=15).grid(row=3, column=0)
Button(integerToRomanFrame, text=' 8 ', fg='white', bg='black',
                command=lambda: addToList("8"), height=3, width=15).grid(row=3, column=1)
Button(integerToRomanFrame, text=' 9 ', fg='white', bg='black',
                command=lambda: addToList("9"), height=3, width=15).grid(row=3, column=2)
Button(integerToRomanFrame, text=' 0 ', fg='white', bg='black',
                command=lambda: addToList("0"), height=3, width=15).grid(row=4, column=1)

# Buttons to all the convert function and convert to a roman numeral,
# return to the menu via frame swap and clear the current variable
Button(integerToRomanFrame, text=' Calculate ', fg='white', bg='black',command=lambda: print(convertIntegerToRoman("".join(convertVariable))), height=3, width=15).grid(row=5, column=1)
Button(integerToRomanFrame, text='Return To Menu', command=lambda:swapFrame(startFrame), height=3, width=15, fg='white', bg='black').grid(row=6,column=0)
Button(integerToRomanFrame, text='Clear', command=lambda:convertVariable.clear(), height=3, width=15, fg='white', bg='black').grid(row=6,column=2)
# Dynamically updating label when calculate is called
result=Label(integerToRomanFrame, text="",height=3,width=22, fg='white', bg='black')
result.grid(row=6,column=1)

# Layout for Roman To Integer Frame
# Each button calls the addToList function to add the current letter to the input
Label(romanToIntFrame, text='Type in your Roman numeral', height=3, width=22, fg='white', bg='black').grid(row=0,column=1)
Button(romanToIntFrame, text='I', fg='white', bg='black',
                command=lambda: addToList("I"), height=3, width=15).grid(row=1, column=0)
Button(romanToIntFrame, text='V', fg='white', bg='black',
                command=lambda: addToList("V"), height=3, width=15).grid(row=1, column=1)
Button(romanToIntFrame, text='X', fg='white', bg='black',
                command=lambda: addToList("X"), height=3, width=15).grid(row=1, column=2)
Button(romanToIntFrame, text='L', fg='white', bg='black',
                command=lambda: addToList("L"), height=3, width=15).grid(row=2, column=0)
Button(romanToIntFrame, text='C', fg='white', bg='black',
                command=lambda: addToList("C"), height=3, width=15).grid(row=2, column=1)

# Buttons to all the convert function and convert to an integer,
# return to the menu via frame swap and clear the current variable
Button(romanToIntFrame, text='Calculate', command=lambda:convertRomanToInt("".join(convertVariable)),height=3,width=15, fg='white', bg='black').grid(row=2, column=2)
Button(romanToIntFrame, text='Return To Menu', command=lambda:swapFrame(startFrame), height=3, width=15, fg='white', bg='black').grid(row=3,column=0)
Button(romanToIntFrame, text='Clear', command=lambda:convertVariable.clear(), height=3, width=15, fg='white', bg='black').grid(row=3,column=2)
# Dynamically updating label when calculate is called
result2=Label(romanToIntFrame, text="",height=3,width=22, fg='white', bg='black')
result2.grid(row=3,column=1)

# Start on Menu Frame
# Begin Loop
swapFrame(startFrame)
displayRoot.mainloop()
    
