file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day2.txt", "r")

theGame = ""
toCheck = []
eachPull = []
colourPosition = 0
value = 0
invalidGame = False
for line in file:
    theGame = line[line.find(":")+1:]
    toCheck = theGame.split(";")

    for pulls in toCheck:
        eachPull = pulls.split(",")
        for balls in eachPull:
            colourPosition = balls.find("red")
            if colourPosition != -1 and int(balls.strip(" red\n")) > 12:
                invalidGame = True

            colourPosition = balls.find("green")
            if colourPosition != -1 and int(balls.strip(" gren\n")) > 13:
                invalidGame = True

            colourPosition = balls.find("blue")
            if colourPosition != -1 and int(balls.strip(" blue\n")) > 14:
                invalidGame = True
        if invalidGame:
            break
    if invalidGame == False:
        value += int(line[:line.find(":")].strip(":Game "))

    invalidGame = False

print(value)
                
file.close()
