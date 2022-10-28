from cgitb import text
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
    convertVariable.clear()
    return solution

def convertIntegerToRoman(rInt):

    rInt=int(rInt)
    M = ["", "M", "MM", "MMM"]
    C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
    X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
    I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
    convertVariable.clear()
    return M[rInt // 1000] + C[(rInt % 1000) // 100] + X[(rInt % 100) // 10] + I[rInt % 10]


def swapFrame(frame):
    frame.tkraise()

def addToList(number):
    convertVariable.append(number)
    

convertVariable = []
displayRoot = Tk()  
startFrame = Frame(displayRoot)
integerToRomanFrame = Frame(displayRoot)
romanToIntFrame = Frame(displayRoot)
displayRoot.geometry("400x400")
displayRoot.minsize(400, 400)
displayRoot.maxsize(400, 400)


startFrame.grid(row=0, column=0, sticky='news')
integerToRomanFrame.grid(row=0, column=0, sticky='news')
romanToIntFrame.grid(row=0, column=0, sticky='news')

# Start Menu
Label(startFrame, text='Choose Calculation', height=8, width=15, fg='white', bg='black').grid(row=0,column=1)
Button(startFrame, text='Integer To Roman', command=lambda:swapFrame(integerToRomanFrame), height=8, width=19, fg='white', bg='black').grid(row=1,column=0)
Button(startFrame, text='Roman To Integer', command=lambda:swapFrame(romanToIntFrame), height=8, width=19, fg='white', bg='black').grid(row=1,column=2)

# Layout for Integer To Roman Frame
Label(integerToRomanFrame, text='Enter in your number',height=3,width=22, fg='white', bg='black').grid(row=0,column=1)
button1 = Button(integerToRomanFrame, text=' 1 ', fg='white', bg='black',
                command=lambda: addToList("1"), height=3, width=15)
button1.grid(row=1, column=0)
button2 = Button(integerToRomanFrame, text=' 2 ', fg='white', bg='black',
                command=lambda: addToList("2"), height=3, width=15)
button2.grid(row=1, column=1)
button3 = Button(integerToRomanFrame, text=' 3 ', fg='white', bg='black',
                command=lambda: addToList("3"), height=3, width=15)
button3.grid(row=1, column=2)

button4 = Button(integerToRomanFrame, text=' 4 ', fg='white', bg='black',
                command=lambda: addToList("4"), height=3, width=15)
button4.grid(row=2, column=0)
button5 = Button(integerToRomanFrame, text=' 5 ', fg='white', bg='black',
                command=lambda: addToList("5"), height=3, width=15)
button5.grid(row=2, column=1)
button6 = Button(integerToRomanFrame, text=' 6 ', fg='white', bg='black',
                command=lambda: addToList("6"), height=3, width=15)
button6.grid(row=2, column=2)

button7 = Button(integerToRomanFrame, text=' 7 ', fg='white', bg='black',
                command=lambda: addToList("7"), height=3, width=15)
button7.grid(row=3, column=0)
button8 = Button(integerToRomanFrame, text=' 8 ', fg='white', bg='black',
                command=lambda: addToList("8"), height=3, width=15)
button8.grid(row=3, column=1)

button9 = Button(integerToRomanFrame, text=' 9 ', fg='white', bg='black',
                command=lambda: addToList("9"), height=3, width=15)
button9.grid(row=3, column=2)
button0 = Button(integerToRomanFrame, text=' 0 ', fg='white', bg='black',
                command=lambda: addToList("0"), height=3, width=15)
button0.grid(row=4, column=1)
button0 = Button(integerToRomanFrame, text=' Calculate ', fg='white', bg='black',
                command=lambda: print(convertIntegerToRoman("".join(convertVariable))), height=3, width=15)
button0.grid(row=5, column=1)
Button(integerToRomanFrame, text='Return To Menu', command=lambda:swapFrame(startFrame), height=3, width=15, fg='white', bg='black').grid(row=6,column=1)

# Layout for Roman To Integer Frame
Label(romanToIntFrame, text='Type in your Roman numeral', height=3, width=22, fg='white', bg='black').grid(row=0,column=1)
button1 = Button(romanToIntFrame, text='I', fg='white', bg='black',
                command=lambda: addToList("I"), height=3, width=15)
button1.grid(row=1, column=0)
button2 = Button(romanToIntFrame, text='V', fg='white', bg='black',
                command=lambda: addToList("V"), height=3, width=15)
button2.grid(row=1, column=1)
button3 = Button(romanToIntFrame, text='X', fg='white', bg='black',
                command=lambda: addToList("X"), height=3, width=15)
button3.grid(row=1, column=2)

button4 = Button(romanToIntFrame, text='L', fg='white', bg='black',
                command=lambda: addToList("L"), height=3, width=15)
button4.grid(row=2, column=0)
button4 = Button(romanToIntFrame, text='C', fg='white', bg='black',
                command=lambda: addToList("C"), height=3, width=15)
button4.grid(row=2, column=1)

Button(romanToIntFrame, text='Calculate', command=lambda:print(convertRomanToInt("".join(convertVariable))),height=3,width=15, fg='white', bg='black').grid(row=2, column=2)
Button(romanToIntFrame, text='Return To Menu', command=lambda:swapFrame(startFrame), height=3, width=15, fg='white', bg='black').grid(row=3,column=1)


# Start on Menu Frame
# Begin Loop
swapFrame(startFrame)
displayRoot.mainloop()
    
