"""Module providing a function printing python version."""

guess = 0
answer = 5

while answer != guess:
    guess = int(input("Guess: "))
else:
    print("Correct!")
