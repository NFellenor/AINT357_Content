
#BF Interpreter:
#Take string value e.g. +++++
#Perform tasks depending on character in string specified by BF interpreter

# > inc data pointer
# < dec data pointer
# + inc value at pointer
# - dec value at  pointer
# . output byte at pointer
# , take one byte of input and store in data pointer
# [ if current pointer value = 0 jump to associated ] (skipping code inside, an IF statement
# ]

cellList = [0] #List to be manipulated

cellPointer = 0 #Pointer for cell list

pgmString = "." #Program instructions string

for x in pgmString: #For length of string, append list to ensure its minimum required size for program (will only be entirely used if pgmString is >>>>>>>...)
    cellList.append(0)

def showList():
    print(cellList)

for i in pgmString: #For each character in instructions string, loop through interpreter

    showList()

    #Actual interpreter part:
    if (i == ">"):
        cellPointer = cellPointer + 1 #WARNING: What happens at end of list?
    elif (i == "<"):
        cellPointer = cellPointer - 1 #WARNING: What happens at start of list?
    elif (i == "+"):
        cellList[cellPointer] = cellList[cellPointer] + 1 #Inc index value by 1
    elif (i == "+"):
        cellList[cellPointer] = cellList[cellPointer] - 1 #Dec index value by 1
    elif (i == "."):
        print(cellList[cellPointer]) #Print value at current index
    elif (i == ","):     
        a = input()     
        cellList[cellPointer] = a #What if a != 1 byte int?

showList() #Print final version of list







