file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day4.txt", "r")

winningNumbers = ""
yourNumbers = []

score = 0
value = 0
for line in file:
    winningNumbers = line[line.find(":")+2:line.find("|")-1].split(" ")
    yourNumbers = line[line.find("|")+2:].split(" ")

    i=0
    while i < len(winningNumbers):
        winningNumbers[i] = winningNumbers[i].strip("\n")
        i+=1
    i=0
    while i < len(yourNumbers):
        yourNumbers[i] = yourNumbers[i].strip("\n")
        i+=1
        
    for number in yourNumbers:
        if number != "" and number in winningNumbers:
            if score == 0:
                score += 1
            else:
                score *= 2
    value += score
    score = 0

print(value)

file.close()
