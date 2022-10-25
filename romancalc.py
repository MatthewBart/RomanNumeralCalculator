
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

    
