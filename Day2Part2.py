file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day2.txt", "r")

theGame = ""
toCheck = []
eachPull = []
colourPosition = 0

mostRed = 0
mostGreen = 0
mostBlue = 0

value = 0

for line in file:
    theGame = line[line.find(":")+1:]
    toCheck = theGame.split(";")

    for pulls in toCheck:
        eachPull = pulls.split(",")
        for balls in eachPull:
            colourPosition = balls.find("red")
            if colourPosition != -1 and int(balls.strip(" red\n")) > mostRed:
                mostRed = int(balls.strip(" red\n"))

            colourPosition = balls.find("green")
            if colourPosition != -1 and int(balls.strip(" gren\n")) > mostGreen:
                mostGreen = int(balls.strip(" gren\n"))

            colourPosition = balls.find("blue")
            if colourPosition != -1 and int(balls.strip(" blue\n")) > mostBlue:
                mostBlue = int(balls.strip(" blue\n"))

    value += mostRed * mostBlue * mostGreen
    mostRed = 0
    mostBlue = 0
    mostGreen = 0

print(value)
                
file.close()
