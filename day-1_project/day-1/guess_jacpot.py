def guess_jacpot():
    import random
    jackpot = random.randint(1, 100)
    guess = int(input("Guess the jackpot number between 1 and 100: "))
    while guess != jackpot:
        print("Sorry, that's not the jackpot number. Try again!")
        guess = int(input("Guess the jackpot number between 1 and 100: "))
    print("Congratulations! You guessed the jackpot!")  