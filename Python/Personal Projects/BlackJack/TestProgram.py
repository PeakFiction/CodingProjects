import random
playerMoney = 1000
gameStart = True
playername = input("What is your name? ")
print(f"Welcome to Rock Paper Scissors (but with Gambling), {playername} ")


def endGame():
    global gameStart
    gameStart = False

while gameStart:
    print("Get Ready for The Next Battle")
    playerBet = int(input("What Will Be Your Bet?"))
    print(f"You put {playerBet} on the line")
    playerChoice = input("Rock, Paper, or Scissors? ")
    if playerChoice == 'EXIT':
        endGame()
        break
    if random.randint(1, 3) == 1:
        print("You Won")
        playerMoney = playerBet + playerMoney
        continueCheck = input("Continue? Y/N ")
        if continueCheck == "N":
            print("GAME OVER")
            break
    else:
        print("You Lose")
        continueCheck2 = input("Continue? Y/N ")
        if continueCheck2 == "N":
            print("GAME OVER")
            break
        playerMoney = playerMoney - playerBet

    
    
    
    