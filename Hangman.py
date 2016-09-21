from random import *

## A list of multi-line strings!
HANGMANPICS = ['''
   +----+
        |
        |
        |
        |
        |
 ==========''', '''
   +----+
   O    |
        |
        |
        |
        |
 ==========''', '''
   +----+
   O    |
   |    |
        |
        |
        |
 ==========''', '''
   +----+
   O    |
  /|    |
        |
        |
        |
 ==========''', '''
   +----+
   O    |
  /|\   |
        |
        |
        |
 ==========''', '''
   +----+
   O    |
  /|\   |
  /     |
        |
        |
 ==========''', '''
   +----+
   O    |
  /|\   |
  / \   |
        |
        |
 ==========''']

def main(secret_word, guess, already_used_letters, missed_letters):
    if guess == secret_word:
        print('\nCongratulations! You guessed the word!')
    elif len(missed_letters) >= len(HANGMANPICS)-1:
        print('No more guesses :(')
        print('The secret word was: %s' % secret_word)
    else:
        letter = input('\nPlease enter a letter to guess: ')
        while (not letter.isalpha()) or (len(letter) > 1) or (letter in already_used_letters):
            if not letter.isalpha():
                letter = input('Please enter a LETTER: ')
            elif len(letter) > 1:
                letter = input('Please enter only one letter: ')
            else:
                letter = input('Please enter a new letter: ')
        if letter in secret_word:
            print('You got a letter!')
            ## Originally had this: guess[:secret_word.index(letter)] + letter + guess[secret_word.index(letter)+1:]
            ## Much better to switch to list, then back to String
            list_guess = list(guess)
            for i in range(len(secret_word)):
                if secret_word[i] == letter:
                    list_guess[i] = letter
            guess = ''.join(list_guess)
        else:
            print('You missed.')
            missed_letters += letter
        print('Your progress: %s' % guess)
        already_used_letters += letter
        if guess != secret_word:
            print('Already used letters: %s' % already_used_letters)
            print(HANGMANPICS[len(missed_letters)])
        main(secret_word, guess, already_used_letters, missed_letters)

words = 'Kirk Picard Sisko Janeway Archer'
secret_word = choice(words.split()).lower()
guess = '_' * len(secret_word)  ## '_ ' doesn't work
already_used_letters = ''
missed_letters = ''

print('Welcome to Hangman!')
print('The length of the word is: %i' % len(secret_word))
main(secret_word, guess, already_used_letters, missed_letters)