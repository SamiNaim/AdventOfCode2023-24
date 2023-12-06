with open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 1\\input.txt", "r") as inputFile:
    lines = inputFile.readlines()

firstNumber = -1
lastNumber = 0
allNumbers = 0

for line in lines:
    for char in line:
        if char.isdigit():
            lastNumber = int(char)
            if firstNumber < 0:
                firstNumber = int(char)
    allNumbers += firstNumber * 10 + lastNumber
    firstNumber = -1
    
print(allNumbers)