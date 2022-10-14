#Lab Guessing Game

#ProgramGoal: client guesses a number between 1 and 10.
#They have three tries

def instructions():
    print("Hello! Welcome to Guessing Game.")
    print("The point of this game is to guess a number")
    print("between 1 and 10.")
    print("You have three chances.")
    print("Good Luck!")

def checkValidInput():
    print()
    print("Your guess is outside the correct range.")
    print("It is either less than 1 or greater than 10.")

def giveHint(playerGuess,correctAnswer):
    if playerGuess < correctAnswer:
        print()
        print("Your guess is too low.")
    elif playerGuess > correctAnswer:
        print()
        print("Your guess is too high.")
    else:
        print()
        print("Congratulations", playerName, "you guessed correctly!")

playerName=input("Enter your name:")

def main():
    instructions()
    correctAnswer = 2

    for games in range (3):
        print()
        playerGuess = int(input("Enter your guess:"))
        if playerGuess < 1 or playerGuess > 10:
            checkValidInput()
        elif playerGuess < correctAnswer or playerGuess > correctAnswer:
            giveHint(playerGuess,correctAnswer)
        else:
            giveHint(playerGuess,correctAnswer)
            break
    print("Game Over! You ran out of guesses.")

main()

