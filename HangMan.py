import random

# List of words to choose from
words = ['python', 'hangman', 'computer', 'code', 'programming']

# Select a random word
word = random.choice(words)

# Initialize the guessed letters & used wrong letters lists
guessed_letters = []
used_wrong_letters = []

# Set the maximum number of allowed incorrect guesses
max_guesses = 6

# Function to display the current state of the word
def display_word(word, guessed_letters):


    # Create a list of underscores with the same length as the word
    displayed_word = ['_' for _ in range(len(word))]

    # Replace the underscores with guessed letters
    for i, letter in enumerate(word):
        if letter in guessed_letters:
            displayed_word[i] = letter

    # Return the displayed word as a string
    return ' '.join(displayed_word)

# Game loop
while True:

    # Display the current state of the word
    print(display_word(word, guessed_letters))

    # Ask the user to guess a letter
    guess = input('Guess a letter: ').lower()

    # Check if the letter has already been guessed
    if guess in guessed_letters:
        print('You already guessed that letter')

    else:

        # Add the letter to the guessed letters list
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            print('Correct!')

            print('wrong letters used:', ' '.join(used_wrong_letters))

        else:
            print('Incorrect')

            # Decrement the number of remaining guesses
            max_guesses -= 1
            print('You have', max_guesses, 'guesses left')

            #insert the wrong letter into the used_wrong_letters list
            used_wrong_letters.append(guess)
            print('wrong letters used:', ' '.join(used_wrong_letters))

            # Check if the player has run out of guesses
            if max_guesses == 0:
                print('You lose! The word was', word)
                break
            
    # Check if the player has guessed all the letters in the word
    if set(word) <= set(guessed_letters):
        print('You guessed the word', word,'!!')
        break
