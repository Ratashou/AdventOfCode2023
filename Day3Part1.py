file = open(r"C:\Users\hoodm_000\Documents\Python Projects\AdventOfCode2023\Day3.txt", "r")

numbers = ["0","1","2","3","4","5","6","7","8","9"]
value = 0

fullText = []
for line in file:
    fullText.append(line.strip("\n"))

#First space is for the number to check, 2nd is for its leftmost character's position, 3rd for rightmost
numberToCheck = ["",0,0]
hasASymbol = False

i=0
#Loop through every line
while i < len(fullText):
    j = 0
    #Loop through every character in line i
    while j < len(fullText[i]):
        #Check 3 times if it's a number. Figure out which position the final digit is as well
        if fullText[i][j].isnumeric():
            numberToCheck[0] = fullText[i][j]
            numberToCheck[1] = j
            if j+1 < len(fullText[i]) and fullText[i][j+1].isnumeric():
                numberToCheck[0] += fullText[i][j+1]
                j+=1
                if j+1 < len(fullText[i]) and fullText[i][j+1].isnumeric():
                    numberToCheck[0] += fullText[i][j+1]
                    numberToCheck[2] = j+1
                    j+=1
                else:
                    numberToCheck[2] = j
            else:
                numberToCheck[2] = j

        #Check all 6 positions a symbol could be in, top left to bottom right
        if numberToCheck[0] != "":
            #TopLeft
            if i-1 >= 0 and numberToCheck[1]-1 >= 0 and not fullText[i-1][numberToCheck[1]-1].isnumeric() and fullText[i-1][numberToCheck[1]-1] != ".":
                hasASymbol = True
            #TopRight
            if i-1 >= 0 and numberToCheck[2]+1 < len(fullText[i]) and not fullText[i-1][numberToCheck[2]+1].isnumeric() and fullText[i-1][numberToCheck[2]+1] != ".":
                hasASymbol = True
            #Above1
            if i-1 >= 0 and not fullText[i-1][numberToCheck[1]].isnumeric() and fullText[i-1][numberToCheck[1]] != ".":
                hasASymbol = True
            #Above 2
            if len(numberToCheck[0]) == 3 and i-1 >= 0 and not fullText[i-1][numberToCheck[1]+1].isnumeric() and fullText[i-1][numberToCheck[1]+1] != ".":
                hasASymbol = True
            #Above3:
            if i-1 >= 0 and not fullText[i-1][numberToCheck[2]].isnumeric() and fullText[i-1][numberToCheck[2]] != ".":
                hasASymbol = True
            #CentreLeft
            if numberToCheck[1]-1 >= 0 and not fullText[i][numberToCheck[1]-1].isnumeric() and fullText[i][numberToCheck[1]-1] != ".":
                hasASymbol = True
            #CentreRight
            if numberToCheck[2]+1 < len(fullText[i]) and not fullText[i][numberToCheck[2]+1].isnumeric() and fullText[i][numberToCheck[2]+1] != ".":
                hasASymbol = True
            #BottomLeft
            if i+1 < len(fullText) and numberToCheck[1]-1 >= 0 and not fullText[i+1][numberToCheck[1]-1].isnumeric() and fullText[i+1][numberToCheck[1]-1] != ".":
                hasASymbol = True
            #BottomRight
            if i+1 < len(fullText) and numberToCheck[2]+1 < len(fullText[i]) and not fullText[i+1][numberToCheck[2]+1].isnumeric() and fullText[i+1][numberToCheck[2]+1] != ".":
                hasASymbol = True
            #Below1
            if i+1 < len(fullText) and not fullText[i+1][numberToCheck[1]].isnumeric() and fullText[i+1][numberToCheck[1]] != ".":
                hasASymbol = True
            #Below2
            if len(numberToCheck[0]) == 3 and i+1 < len(fullText) and not fullText[i+1][numberToCheck[1]+1].isnumeric() and fullText[i+1][numberToCheck[1]+1] != ".":
                hasASymbol = True
            #Below3
            if i+1 < len(fullText) and not fullText[i+1][numberToCheck[2]].isnumeric() and fullText[i+1][numberToCheck[2]] != ".":
                hasASymbol = True

            if hasASymbol:
                value += int(numberToCheck[0])
                #print(numberToCheck[0])
                hasASymbol = False

        numberToCheck = ["",0,0]
        j+=1
        
    i+=1

print(value)

file.close()
