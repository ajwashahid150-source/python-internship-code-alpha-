import random

words = ["apple", "python", "computer", "flower", "school"]

word = random.choice(words)

guessed = []

wrong = 0

while wrong < 6:

    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        print("Congratulations! You Won.")
        break

    guess = input("Enter a letter: ")

    if guess in word:
        guessed.append(guess)
        print("Correct Guess!")
    else:
        wrong += 1
        print("Wrong Guess!")

    print("Wrong Guesses:", wrong, "/6")

if wrong == 6:
    print("Game Over!")
    print("The word was:", word)