topBoard = "7|8|9"
topLine = "-----"
midBoard = "4|5|6"
botLine = "-----"
botBoard = "1|2|3"

# while True:

while True:
    playerX = input("What is your move? ")
    if playerX == '1':
        botBoard = botBoard.replace('1', 'X')
        break
    if playerX == '2':
        botBoard = botBoard.replace('2', 'X')
        break
    if playerX == '3':
        botBoard = botBoard.replace('3', 'X')
        break
print(topBoard)
print(topLine)
print(midBoard)
print(botLine)
print(botBoard)