with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 2\\input.txt", "r") as inputFile:
    lines = inputFile.readlines()

sumPowerSets = 0

for line in lines:
    red = 0
    green = 0
    blue = 0
    
    splitString = line.split(": ")
    splitId = int(splitString[0].split(" ")[1])
    
    splitCubes = splitString[1].split("; ")
    for cube in splitCubes:
        splitColors = cube.split(", ")
        for color in splitColors:
            splitNumber = color.split(" ")
            if splitNumber[1].rstrip() == "red":
                red = max(int(splitNumber[0]), red)
            elif splitNumber[1].rstrip() == "green":
                green = max(int(splitNumber[0]), green)
            elif splitNumber[1].rstrip() == "blue":
                blue= max(int(splitNumber[0]), blue)
    
    sumPowerSets += red * green * blue

print(sumPowerSets)