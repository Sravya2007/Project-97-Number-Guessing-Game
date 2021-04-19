import random

#Getting a random number within the range 1-9
randInt = random.randrange(1, 9)
chanceCount = 0

while chanceCount < 5:
    guess = int(input("Enter your guess: "))
    chanceCount = chanceCount + 1

    if guess < randInt:
        print("Too low! Guess a number higher than ", guess)
        
    if guess > randInt:
        print("Too high! Guess a number lower than ", guess)

    if guess == randInt:
        print("You win!!!")
        break

    if not chanceCount < 5:
        print("You lose! The number is ", randInt)