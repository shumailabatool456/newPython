import random

# List of words to choose from
word_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

stages = ['''
  +---+
  |   |
  0   |
 /|\  |
 / \  |
      |
''', '''
  +---+
  |   |
  0   |
 /|\  |
 /    |
      |
''', '''
  +---+
  |   |
  0   |
 /|\  |
      |
      |
''', '''
  +---+
  |   |
  0   |
 /|   |
      |
      |
''', '''
  +---+
  |   |
  0   |
  |   |
      |
      |
''', '''
  +---+
  |   |
  0   |
      |
      |
      |
''', '''
  +---+
  |   |
      |
      |
      |
      |
''']


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = ['_'] * word_length
lives = 6

print("Let's play Hangman!")

while '_' in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please guess a single letter.")
        continue

    if guess in display:
        print(f"You've already guessed {guess}.")
        continue

    for position, letter in enumerate(chosen_word):
        if letter == guess:
            display[position] = guess

    if guess not in chosen_word:
        lives -= 1
        print(f"Wrong guess. You have {lives} lives left.")
        print(stages[lives])
    else:
        print(' '.join(display))

if '_' not in display:
    print("Congratulations! You won!")
else:
    print("You lost. The word was " + chosen_word) 

