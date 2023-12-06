with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 4\\input.txt", "r") as inputFile:
    lines = [line.rstrip() for line in inputFile]

totalPoints = 0

for line in lines:
    dotSplit = line.split(":")
    lineSplit = dotSplit[1].split("|")
    winningSplit = lineSplit[0].split()
    possessionSplit = lineSplit[1].split()
    
    matches = -1
    winningSet = set()
    for winningNumber in winningSplit:
        winningSet.add(int(winningNumber))
    for possessionNumber in possessionSplit:
        if int(possessionNumber) in winningSet:
            matches += 1
    
    if matches >= 0:
        totalPoints += pow(2, matches)

print(totalPoints)