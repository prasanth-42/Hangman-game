import random
import nltk
from nltk.corpus import words

nltk.download('words')

def generate_random_words(num_words):
    word_list = words.words()
    return random.sample(word_list, num_words)

def display_word(word, guessed_letters):
    display = ''
    for letter in word:
        if letter in guessed_letters:
            display += letter
        else:
            display += '_'
    return display

def is_word_guessed(word, guessed_letters):
    for letter in word:
        if letter not in guessed_letters:
            return False
    return True

def hangman(word):
    print("Welcome to Hangman!")
    guessed_letters = []
    max_attempts = 6
    attempts_left = max_attempts
    
    while attempts_left > 0:
        print("\n")
        display = display_word(word, guessed_letters)
        print("Word:", display)
        
        if is_word_guessed(word, guessed_letters):
            print("You've guessed the word:", word)
            break
        
        print("Attempts left:", attempts_left)
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters:
            print("You've already guessed that letter.")
            continue
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in word:
            guessed_letters.append(guess)
            print("Good guess!")
        else:
            print("Oops! That letter is not in the word.")
            attempts_left -= 1
    
    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The word was:", word)
num_words = 10
random_words = generate_random_words(num_words)
chosen_word = random.choice(random_words)
hangman(chosen_word)