import random

number = random.randint(1, 9)
chances = 0

print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("Enter your guess:- "))
    if guess == number:
        print("Congratulations!!")
        break
    elif guess < number:
        print("Your guess is less! Guess a number higher than", guess)
    else:
        print("Your guess is high! Guess a number lower than", guess)
    chances += 1

if not chances < 5:
    print("YOU LOSE! The number is", number)