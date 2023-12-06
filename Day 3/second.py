def checkIfStar(x):
    return x == "*"

def checkForSymbol(index, lines, firstLine, secondLine, thirdLine, maxIndex):
    setOfStars = set()
    if index - 1 >= 0:
        if checkIfStar(lines[firstLine][index - 1]):
            setOfStars.add((index - 1, firstLine))
        if checkIfStar(lines[secondLine][index - 1]):
            setOfStars.add((index - 1, secondLine))
        if checkIfStar(lines[thirdLine][index - 1]):
            setOfStars.add((index - 1, thirdLine))
    if index + 1 <= maxIndex:
        if checkIfStar(lines[firstLine][index + 1]):
            setOfStars.add((index + 1, firstLine))
        if checkIfStar(lines[secondLine][index + 1]):
            setOfStars.add((index + 1, secondLine))
        if checkIfStar(lines[thirdLine][index + 1]):
            setOfStars.add((index + 1, thirdLine))
    
    if checkIfStar(lines[firstLine][index]):
            setOfStars.add((index, firstLine))
    if checkIfStar(lines[thirdLine][index]):
            setOfStars.add((index, thirdLine))
    
    return setOfStars

with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 3\\input.txt", "r") as inputFile:
    lines = [line.rstrip() for line in inputFile]

sizeOfline = len(lines[0])
fillerLine = "." * len(lines[0])

lines.append(fillerLine)
lines.insert(0, fillerLine)

allStars = {}

i = 1
while i < len(lines) - 1:
    index = 0
    while index < sizeOfline:
        if lines[i][index].isdigit():
            firstIndex = index
            stars = set()
            while(index < sizeOfline and lines[i][index].isdigit()):
                stars.update(checkForSymbol(index, lines, i - 1, i, i + 1, sizeOfline - 1))
                index += 1
            lastIndex = index
            for star in stars:
                if star not in allStars:
                    allStars[star] = set()
                allStars[star].add(int(lines[i][firstIndex:lastIndex]))
        else:
            index += 1
    i += 1

sumOfStars = 0

for key in allStars:
    product = 0
    if len(allStars[key]) == 2:
        print(key, allStars[key])
        product = 1
        for x in allStars[key]:
            product *= x
    sumOfStars += product

print(sumOfStars)