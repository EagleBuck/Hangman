import random

# Created 2015-09-25
# Updated 2020-09-08
# Simple Hangman game

# The computer picks a word and the user tries to guess the word

#alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
#words = 'apple banana kiwi kangaroo presentation jazz elephant lily october north south east west internship national state government problem albania albatross computer python program burn fire title monk shell internet door portal screen board phone rotary mouse lion indigo window process'.split()




def main():
    guys = [' _________\n|         |\n|          \n|           \n|           \n|\n|______', ' _________\n|         |\n|         0\n|           \n|           \n|\n|______', ' _________\n|         |\n|         0\n|         | \n|           \n|\n|______', ' _________\n|         |\n|         0\n|        /| \n|           \n|\n|______', ' _________\n|         |\n|         0\n|        /|\\\n|           \n|\n|______', ' _________\n|         |\n|         0\n|        /|\\\n|        / \n|\n|______', ' _________\n|         |\n|         0\n|        /|\\\n|        / \\\n|\n|______']
    alphabet = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    words = 'apple banana kiwi kangaroo presentation jazz elephant lily october north south east west internship national state government problem albania albatross computer python program burn fire title monk shell internet door portal screen board phone rotary mouse lion indigo window process'.split()
    wrong = []
    right = []
    print('Welcome to... HANGMAN')
    print('The computer will select a word and you can try to guess it')

    gameWord = selectWord(words)

    while(True):
        print(guys[len(wrong)])
        for letter in gameWord:
            if letter in right:
                print(letter, end = ' ')
            else:
                print('_',end = ' ')
        print('')
        if len(right) == len(gameWord):
            print('YOU WIN!!')
            break
        elif len(wrong) == 6:
            print('YOU LOSE   :(')
            break
        guess = input('Guess a letter: ')
        if guess not in alphabet:
            print('A LETTER, PLEASE')
        else:
            if guess not in wrong and guess not in right:
                if guess in gameWord:
                    for letter in gameWord:
                        if letter == guess:
                            right.append(letter)
                else:
                    print('wrong')
                    wrong.append(guess)
            else:
                print('You already guessed that')

  
            


def selectWord(words):
    wordInt = random.randint(0, len(words)-1)
    #print(words[wordInt])
    return words[wordInt]
     


main()
