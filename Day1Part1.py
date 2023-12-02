file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day1.txt", "r")

allNumbers = ''
value = 0
for line in file:
    for i in line:
        if i.isnumeric():
            allNumbers += i

    if len(allNumbers) == 1:
        allNumbers += allNumbers
        value += int(allNumbers)
    else:
        value += int(allNumbers[0] + allNumbers[len(allNumbers) - 1])
    allNumbers = ''

print(value)

file.close()
