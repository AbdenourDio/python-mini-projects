import random
from art import gues_the_number_logo

print(gues_the_number_logo)

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
choose_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

difficulty = {
    "easy": 10,
    "hard": 5,
}
def decrease_attempts():
    global attempts
    attempts -= 1

correct_answer = random.randrange(100)

attempts = difficulty[choose_difficulty]
while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("make a guess : "))

    if guess > correct_answer:
        print("too high")
        decrease_attempts()
    elif guess < correct_answer:
        print("too low")
        decrease_attempts()
    else:
        print("YOU WIN!")
        break

if attempts == 0:
    print("BAHAHA YOU LOSE, You've run out of guesses")

