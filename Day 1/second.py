inputFile = open("C:\\Users\\User\\Desktop\\Projects\\AdventOfCode2023-24\\AdventOfCode2023-24\\Day 1\\input.txt", "r")
lines = inputFile.readlines()

firstNumber = -1
lastNumber = 0
allNumbers = 0

def addNumer(n):
    global firstNumber
    global lastNumber
    if firstNumber < 0:
        firstNumber = n
    lastNumber = n

for line in lines:
    for i in range(len(line)):
        if line[i].isdigit():
            addNumer(int(line[i]))
        else:
            if line[i:i+3] == "one":
                addNumer(1)
            elif line[i:i+3] == "two":
                addNumer(2)
            elif line[i:i+5] == "three":
                addNumer(3)
            elif line[i:i+4] == "four":
                addNumer(4)
            elif line[i:i+4] == "five": 
                addNumer(5)
            elif line[i:i+3] == "six":
                addNumer(6)
            elif line[i:i+5] == "seven":
                addNumer(7)
            elif line[i:i+5] == "eight":
                addNumer(8)
            elif line[i:i+4] == "nine":
                addNumer(9)
    allNumbers += firstNumber * 10 + lastNumber
    firstNumber = -1

print(allNumbers)