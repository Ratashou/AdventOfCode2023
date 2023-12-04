file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day4.txt", "r")

cardCopies = []
currentCard = 0
toAdd = 1

winningNumbers = []
yourNumbers = []

score = 0
value = 0
for line in file:
    cardCopies.append(1)
file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day4.txt", "r")
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
            score += 1

    while score > 0:
        cardCopies[currentCard + toAdd] += cardCopies[currentCard]
        score -= 1
        toAdd += 1
    toAdd = 1

    currentCard += 1

for number in cardCopies:
    value += number

print(value)

file.close()
