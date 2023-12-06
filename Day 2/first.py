with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 2\\input.txt", "r") as inputFile:
    lines = inputFile.readlines()

possibleGames = 0

for line in lines:
    possible = True
    
    splitString = line.split(": ")
    splitId = int(splitString[0].split(" ")[1])
    
    splitCubes = splitString[1].split("; ")
    for cube in splitCubes:
        splitColors = cube.split(", ")
        for color in splitColors:
            splitNumber = color.split(" ")
            if splitNumber[1].rstrip() == "red" and int(splitNumber[0]) > 12:
                possible = False
                break
            elif splitNumber[1].rstrip() == "green" and int(splitNumber[0]) > 13:
                possible = False
                break
            elif splitNumber[1].rstrip() == "blue" and int(splitNumber[0]) > 14:
                possible = False
                break
        if not possible:
            break
    
    if possible:
        possibleGames += splitId

print(possibleGames)