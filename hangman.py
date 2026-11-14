# Import modules
import random

# Words selection
words = ["python", "computer", "keyboard", "program"]
secret_word = random.choice(words)

print("Welcome to Hangman!")
difficulty_level = input("Enter difficult level(Easy, Medium, or Hard): ").lower()

# Difficulty selection
while difficulty_level != "easy" and difficulty_level != "medium" and difficulty_level != "hard":
    difficulty_level = input("Enter difficult level(Easy, Medium, or Hard): ").lower()

if difficulty_level == "easy":
    attempts = 8

elif difficulty_level == "medium":
    attempts = 6

else:
    attempts = 4

# Game variables
number_of_attempts = attempts

print("_" * len(secret_word))

guessed_letters = set()

# Hangman drawings
empty_gallows = "+---+\n|   |\n    |\n    |\n========="

head_only = "+---+\n|   |\nO   |\n    |\n========="

head_body = "+---+\n|   |\nO   |\n|   |\n    |\n========="

one_arm = "+---+\n|   |\nO   |\n/|  |\n    |\n========="

both_arm = "+---+\n|   |\nO   |\n/|\\ |\n    |\n========="

one_leg = "+---+\n|   |\nO   |\n/|\\ |\n/  |\n========="

both_leg = "+---+\n|   |\nO   |\n/|\\ |\n/ \\ |\n========="

hangman_stages = [empty_gallows, head_only, head_body, one_arm, both_arm, one_leg, both_leg]
print(hangman_stages[0])

# Main game loop
while attempts > 0:
    guess_letter = input("Guess a letter: ").lower()
    if len(guess_letter)!= 1 or not guess_letter.isalpha():
        print("Please enter only one letter")
        continue
    
    if guess_letter in guessed_letters:
        print("You have already guessed the letter!")
        continue
    if guess_letter in secret_word:
        print("orrect guess!")
    else:
        print("Wrong guess!")
        attempts -= 1
    index = ((number_of_attempts - attempts)* 6) // number_of_attempts
    print(hangman_stages[index])    

    print(f"Attempts remaining: {attempts}")
    guessed_letters.add(guess_letter)
    print(sorted(guessed_letters))
    display = ""
    for i in secret_word:
        if i in guessed_letters:
            display += i
        else:
            display += "_"
        
    print(display)

    # Win and lose conditions
    if "_" not in display:
        print("You win!")
        break
    if attempts == 0:
        print("Game over!")
        print(f"Secret word: {secret_word}")
        break

    
