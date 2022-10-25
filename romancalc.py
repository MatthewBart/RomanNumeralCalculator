from tkinter import *
from tkinter.ttk import LabeledScale 

def convertRomanToInt(rString):    
    romanKeyMap = dict({'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000,})

    
    solution = romanKeyMap[(rString[(len(rString)-1)])]

    for x in reversed(range(len(rString)-1)):
        if romanKeyMap[rString[x]] < romanKeyMap[rString[x+1]]:
            solution -= romanKeyMap[rString[x]]
        else:
            solution += romanKeyMap[rString[x]]


    return solution


def convertIntegerToRoman(rInt):
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    
    return M[rInt // 1000] + C[(rInt % 1000) // 100] + X[(rInt % 100) // 10] + I[rInt % 10]


def swapFrame(frame):
    frame.tkraise()

def addToInt(number):
    
    intToConvert += + str(number)

global intToConvert
displayRoot = Tk()  
startFrame = Frame(displayRoot)
integerToRomanFrame = Frame(displayRoot)
romanToIntFrame = Frame(displayRoot)
displayRoot.geometry("400x400")
displayRoot.minsize(400, 400)
displayRoot.maxsize(400, 400)



for frame in (startFrame, integerToRomanFrame, romanToIntFrame):
    frame.grid(row=0, column=0, sticky='news')

Label(startFrame, text='Choose Calculation').pack()
Button(startFrame, text='Integer To Roman', command=lambda:swapFrame(integerToRomanFrame)).pack(side="top")
Button(startFrame, text='Roman To Integer', command=lambda:swapFrame(romanToIntFrame)).pack(side="top")

Label(integerToRomanFrame, text='Enter in your value to convert').pack()
Button(integerToRomanFrame, text='Calculate', command=lambda:swapFrame(romanToIntFrame)).pack()
button1 = Button(displayRoot, text=' 1 ', fg='black', bg='red',
                command=lambda: addToInt(1), height=1, width=7)
button1.grid(row=2, column=0)

button2 = Button(displayRoot, text=' 2 ', fg='black', bg='red',
                command=lambda: addToInt(2), height=1, width=7)
button2.grid(row=2, column=1)

button3 = Button(displayRoot, text=' 3 ', fg='black', bg='red',
                command=lambda: addToInt(3), height=1, width=7)
button3.grid(row=2, column=2)

button4 = Button(displayRoot, text=' 4 ', fg='black', bg='red',
                command=lambda: addToInt(4), height=1, width=7)
button4.grid(row=3, column=0)

button5 = Button(displayRoot, text=' 5 ', fg='black', bg='red',
                command=lambda: addToInt(5), height=1, width=7)
button5.grid(row=3, column=1)

button6 = Button(displayRoot, text=' 6 ', fg='black', bg='red',
                command=lambda: addToInt(6), height=1, width=7)
button6.grid(row=3, column=2)

button7 = Button(displayRoot, text=' 7 ', fg='black', bg='red',
                command=lambda: addToInt(7), height=1, width=7)
button7.grid(row=4, column=0)

button8 = Button(displayRoot, text=' 8 ', fg='black', bg='red',
                command=lambda: addToInt(8), height=1, width=7)
button8.grid(row=4, column=1)

button9 = Button(displayRoot, text=' 9 ', fg='black', bg='red',
                command=lambda: addToInt(9), height=1, width=7)
button9.grid(row=4, column=2)

button0 = Button(displayRoot, text=' 0 ', fg='black', bg='red',
                command=lambda: addToInt(0), height=1, width=7)
button0.grid(row=5, column=0)
Label(romanToIntFrame, text='Type in your Roman numeral to convert').pack(side='top')
Button(romanToIntFrame, text='Calculate', command=lambda:swapFrame(startFrame)).pack(side='left')

swapFrame(startFrame)
displayRoot.mainloop()
print("Input 1 for Roman to Integer\nInput 2 for Integer to Roman")
x= input()
if x=="1":
    print("Input Roman Numerals")
    r=input()
    print(convertRomanToInt(r))
elif x=="2":
    print("Input Integer")
    r=int(input())
    print(convertIntegerToRoman(r))
else:
    print("Invalid answer")

    
