import random

def guess_the_number():
    print("Welcome to Guess the Number!")
    random_number = random.randint(1, 100)
    num_guesses = 0
    
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        num_guesses += 1
        
        if guess < random_number:
            print("Too low! Guess higher.")
        elif guess > random_number:
            print("Too high! Guess lower.")
        else:
            print("Congratulations! You guessed the number in", num_guesses, "guesses.")
            play_again = input("Do you want to play again? (y/n) ")
            if play_again.lower() == "y":
                random_number = random.randint(1, 100)
                num_guesses = 0
            else:
                print("Thanks for playing!")
                break

guess_the_number()
