# REDACTED
# Created 2015-09-25
# Updated 2015-09-30
# Simple Hangman game

# To-Do:
    # Once there are any letters in the wrong list, it repeats 'you already tried that'
    # *The list of letters in game word can only be unique letters*
    # Victory Check
    # Counting number of right and wrong answers
    # Multiple  Guesses
    # Try again, restart program

import random
alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
words = 'apple banana kiwi kangaroo presentation jazz elephant lily october north south east west internship national state government problem albania albatross computer python program burn fire title monk shell internet door portal screen board phone rotary mouse lion indigo window process'.split()
#print words
words.sort()
#print words
r_lett_list = [ ]
w_lett_list = [ ]

# We determine what word to use by generating a random number and applying it to the list

def get_word(word_list):
    word_num = random.randint(0, len(word_list)+1)
    print(word_num)
    game_word = word_list[word_num]
    return game_word

# Now we get a letter from the user
# A while statement keeps user in until they input a letter
# Then function checks guessed letter against other guesses
# to make sure guess is unique

def guess_letter():
    while 1==1:
        user_lett = input('Guess a letter: ')
        if user_lett not in alphabet:
            print('A LETTER, PLEASE')
        elif user_lett in r_lett_list or w_lett_list:
            print('You already tried that')
        else:
            return user_lett
            break

# Now we check if their letter is in the word
# Then the letter goes into a list of right and wrong guessed letters
# I might make a master list, unclear if needed

def check_letter(user_guess, game_word):
    if user_guess in game_word:
        print('good')
        global r_lett_list
        r_lett_list.extend(user_guess)
        print(r_lett_list)
    else:
        print('bad')
        global w_lett_list
        w_lett_list.extend(user_guess)
        print(w_lett_list)

# This will check if user won by comparing number of correct letters
# against length of secret word
def victory_check(r_lett_lens):
    print('hi')


# The central function
def hang_func():
    game_word = get_word(words)
    game_word_list = list(game_word)
    game_word_list.sort()
    print(game_word_list)
    print(game_word + ' Word Length is ' + str(len(game_word)))
    while r_lett_list.sort != game_word_list:
        user_letter = guess_letter()
        print('" ' + user_letter + ' "')
        check_letter(user_letter, game_word_list)
    

    
hang_func()

game_word = get_word(words)
print(game_word)
user_letter = guess_letter()
print('" ' + user_letter + ' "')
check_letter(user_letter)
user_letter = guess_letter()
print('" ' + user_letter + ' "')
check_letter(user_letter)
