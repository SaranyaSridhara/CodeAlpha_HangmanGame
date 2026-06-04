import random

words = ["apple", "mango", "grape", "tiger", "house"]
word = random.choice(words)

guessed = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:

    # display word
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "

    print("\nWord:", display)

    # win condition
    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    # input
    guess = input("Enter a letter: ").strip().lower()

    # validation
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.")
        continue

    # already guessed check
    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    # check guess
    if guess in word:
        print("Correct!")
    else:
        attempts -= 1
        print("Wrong guess! Attempts left:", attempts)

# lose condition
if attempts == 0:
    print("\nGame Over! The word was:", word)
