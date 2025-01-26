import random

# Dictionary for hangman images
hangman = {
    0: '''
        ____________
         |
         ''',
    1: '''
        ____________
         |
         O
         ''',
    2: '''
        ____________
         |
         O
        /''',
    3: '''
        ____________
         |
         O
        / \\ ''',
    4: '''
        ____________
         |
         O
        / \\
         |''',
    5: '''
        ____________
         |
         O
        / \\
         |
        /''',
    6: '''
        ____________
         |
         O
        / \\
         |
        / \\'''
}

# List of possible words
word_list = ["ANALYST", "DEVELOPER", "MANAGER", "DATA", "SCIENTIST", "PYTHON"]
answer_word = random.choice(word_list)

# Create a hidden_word
hidden_word = "_ " * len(answer_word)
hidden_word = hidden_word.strip()

# Initialize variables
remaining_mistakes = 6
failed_letters = []

# Welcome message
print("\nWelcome to HANGMAN GAME!")

# Main game loop
while remaining_mistakes > 0 and "_" in hidden_word:
    print(f"{hangman[6 - remaining_mistakes]}")
    print(f"\nHidden word is: {hidden_word}")
    print(f"Failed letters: {', '.join(failed_letters)}")
    print(f"==================================================")

    # Input validation loop
    picked_letter = ""
    while not (picked_letter.isupper() and len(picked_letter) == 1):
      picked_letter = input("\nPick a letter: ").upper()
      if not ('A' <= picked_letter <= 'Z'):
          print("Invalid input. Please enter only alphabetic letters.")
      elif len(picked_letter) != 1:
          print("Invalid input. Please enter only one letter at a time.")

    # Check if the guessed letter is in the word:
    index_count = 0  # Reset index count for each iteration
    if picked_letter in answer_word:
        print(f"CORRECT! The word contains the letter {picked_letter}!")
        for letter in answer_word:
            if letter == picked_letter:
                hidden_word = hidden_word[:index_count] + picked_letter + hidden_word[index_count + 1:]
            index_count += 2  # Move index count for spaced underscores
    else:
        if picked_letter not in failed_letters:
            failed_letters.append(picked_letter)
            remaining_mistakes -= 1
            print(f"WRONG! Number of mistakes left: {remaining_mistakes}")
        else:
            print(f"You already guessed the letter {picked_letter}.")

# End of game
if remaining_mistakes == 0:
    print(hangman[6])  # Print the final hangman figure
    print("\nHANGED!! Better luck next time!")
    print(f"\nThe correct word is: {answer_word}")
    print(f"\n==================================================")
else:
    print("\nCONGRATULATIONS!🎉🎉🎉")
    print("\nYou guessed the word!\n")