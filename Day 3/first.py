def checkIfSymbol(x):
    if x.isdigit() or x == ".":
        return False
    else:
        return True

def checkForSymbol(index, firstLine, secondLine, thirdLine, maxIndex):
    if index - 1 >= 0:
        if checkIfSymbol(firstLine[index - 1]):
            return True
        if checkIfSymbol(secondLine[index - 1]):
            return True
        if checkIfSymbol(thirdLine[index - 1]):
            return True
    if index + 1 <= maxIndex:
        if checkIfSymbol(firstLine[index + 1]):
            return True
        if checkIfSymbol(secondLine[index + 1]):
            return True
        if checkIfSymbol(thirdLine[index + 1]):
            return True
    
    if checkIfSymbol(firstLine[index]):
        return True
    if checkIfSymbol(thirdLine[index]):
        return True
    
    return False

with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 3\\input.txt", "r") as inputFile:
    lines = [line.rstrip() for line in inputFile]

sizeOfline = len(lines[0])
fillerLine = "." * len(lines[0])

sumOfPartNumbers = 0

for i in range(len(lines)):
    index = 0
    while index < sizeOfline:
        if lines[i][index].isdigit():
            partNumber = False
            firstIndex = index
            while(index < sizeOfline and lines[i][index].isdigit()):
                if partNumber:
                    index += 1
                elif i > 0 and i < sizeOfline - 1:
                    if checkForSymbol(index, lines[i - 1], lines[i], lines[i + 1], sizeOfline - 1):
                        partNumber = True
                    index += 1
                elif i == 0:
                    if checkForSymbol(index, fillerLine, lines[i], lines[i + 1], sizeOfline - 1):
                        partNumber = True
                    index += 1
                elif i == sizeOfline - 1:
                    if checkForSymbol(index, lines[i - 1], lines[i], fillerLine, sizeOfline - 1):
                        partNumber = True
                    index += 1
            lastIndex = index
            if partNumber:
                sumOfPartNumbers += int(lines[i][firstIndex:lastIndex])
        else:
            index += 1

print(sumOfPartNumbers)