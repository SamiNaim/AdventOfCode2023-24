with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 4\\input.txt", "r") as inputFile:
    lines = [line.rstrip() for line in inputFile]

listOfInstances = []
totalinstances = 0

for line in lines:
    if len(listOfInstances) == 0:
        instances = 1
    else:
        instances = 1 + listOfInstances.pop(0)
    totalinstances += instances
    print(listOfInstances)
    while instances > 0:
        dotSplit = line.split(":")
        lineSplit = dotSplit[1].split("|")
        winningSplit = lineSplit[0].split()
        possessionSplit = lineSplit[1].split()
    
        index = 0
        winningSet = set()
        for winningNumber in winningSplit:
            winningSet.add(int(winningNumber))
        for possessionNumber in possessionSplit:
            if int(possessionNumber) in winningSet:
                if len(listOfInstances) > index:
                    listOfInstances[index] += 1
                else:
                    listOfInstances.append(1)
                index += 1
        instances -= 1

print(totalinstances)