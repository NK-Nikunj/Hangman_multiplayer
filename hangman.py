from time import sleep
from os import system
from getpass import getpass
import string

def print_screen(guess_word, guess, incorrect_guess_made, correct_guess_made, secret_word):
    """
    If guess_word is same as secret_word this function will show the screen wwith all details
    and also sleep the the program so that the user can see and also shows user2 as winner
    """
    system('cls')
        
    print "Here is the guessed word: ", guess_word
    print "Number of guesses available: ", guess
    print "Incorrect guesses of letters made: ", incorrect_guess_made
    print "Correct guesses of letters made: ", correct_guess_made
    
    sleep(2)
    
    print "\n\nYay! User2 won"
    sleep(1.5)
    print "\nGoing back to home screen"
    sleep(3)
    start_interface()
        


def check_length_letter(guess_let, secret_word, guess_word):
    """
    Checks whether letter entered is string or char 
    """    
    
    if len(guess_let) == 1:
        return guess_letter
    else:
        print("\nInvalid input. Try again")
        sleep(1)
        secret_word = list(secret_word)
        guess_word = list(guess_word)
        return guess_letter(secret_word, guess_word)


def check_letter(guess_let, secret_word, guess_word):
    """
    Checks whether input character is a letter or not
    """    
    
    if guess_let in string.ascii_lowercase:
        return guess_letter
    else:
        print("\nInvalid type. Use only letters")
        sleep(1)
        return guess_letter(secret_word, guess_word)
        

def check_loss(guess_word, guess, incorrect_guess_made, correct_guess_made, secret_word):
    """
    To display that user1 has won
    """    
    system('cls')
        
    print "Here is the guessed word: ", guess_word
    print "Number of guesses available: ", guess
    print "Incorrect guesses of letters made: ", incorrect_guess_made
    print "Correct guesses of letters made: ", correct_guess_made
    
    sleep(2)
    
    print("\n\nYay! User1 won")
    sleep(2)
    print("\nGoing back to main screen.")
    sleep(4)
    start_interface()        


def guess_letter(secret_word, guess_word):
    """
    Main framework of the program. Prompts user2 to input guesses
    """
    global incorrect_guess_made
    global correct_guess_made
    global guess

    incorrect_guess_made = ''
    correct_guess_made = ''
    guess = 6
    
    while secret_word != guess_word and guess > 0:
        system('cls')
        
        print "Here is the guessed word: ", guess_word
        print "Number of guesses available: ", guess
        print "Incorrect guesses of letters made: ", incorrect_guess_made
        print "Correct guesses of letters made: ", correct_guess_made
        guess_let = raw_input("\nGuess letter: ")
        
        guess_let.lower()
        """        
        if guess_letter in incorrect_guess_made:
            print "You have already used this guess, try another"
            sleep(3)
            guess_letter(secret_word, guess_word)
        
        if guess_letter in correct_guess_made:
            print "You have already used this guess, try another"
            sleep(3)
            guess_letter(secret_word, guess_word)
        """                
        
        check_length_letter(guess_let, secret_word, guess_word)
        check_letter(guess_let, secret_word, guess_word)
        
        if guess_let in secret_word:
            correct_guess_made = correct_guess_made + guess_let + " "        
        
        if guess_let not in secret_word:
            incorrect_guess_made = incorrect_guess_made + guess_let + " "

        for i in range(len(secret_word)):
            if guess_let == secret_word[i]:
                guess_word[i] = guess_let
        
        if guess_let not in secret_word:
            guess -= 1
    
    if secret_word == guess_word:
        print_screen(guess_word, guess, incorrect_guess_made, correct_guess_made, secret_word)
    else:
        check_loss(guess_word, guess, incorrect_guess_made, correct_guess_made, secret_word)
        
        
def user2(secret_word):
    """
    Starts the game and prompts user2 to start guessing
    """
    system('cls')

    print "User2, User1 has selected a word with", len(secret_word), "letters"

    guess_word = "-"*len(secret_word)    

    print "\nHere is the word:", guess_word
    
    guess_word = list(guess_word)
    guess_letter(secret_word, guess_word)

def check_validity(secret_word):
    """
    Checks whether the input word is genuine
    """   
    x = 0
    for i in range(len(secret_word)):   
        if secret_word[i] in string.ascii_lowercase:
            x += 1
    if x == len(secret_word):
        return True
            

def multiplayer():
    """
    Welcomes you to multiplayer screen
    """    
    system('cls')
    
    print("Welcome to Multiplayer in Hangman")
    print("-------------------------------------")

    secret_word = getpass("User1, select a word: ")
    
    secret_word.lower()
    val = check_validity(secret_word)
    secret_word = list(secret_word)
    
    if val:
        user2(secret_word)
    else:
        print("\nInvalid input, try again!")
        sleep(2.5)
        multiplayer()
    
    user2(secret_word)

def instruction():
    """
    Prints the required instructions of the game
    """
    system('cls')    

    print("INSTRUCTIONS:")

    print("\nFor multiplayer: One of the user will add a word of his/her choice (Note: The" +
    " word will be hidden so type correctly the first time). Once the word is typed the other" +
    " user will have to guess the word. He will get 6 guesses. For each correct guess" +
    " letter corresponding to that guess will be displayed. Do not type more than one letter" +
    " at a time as it will prompt you to type again. If you guess the word before you lose your" +
    " guesses you win, else you lose.")

    print("\nFor single player: single player is under construction, should be here soon!")

    inp = raw_input("\nTo go back type 'back': ")
    inp.lower()
    
    if inp == "back":
        start_interface()
    else:
        print("\ninvalid input, try again")
        sleep(1.5)
        instruction()
        

def start_interface():
    """
    Prints the initial screen and takes input to go to next screen
    """
    system('cls')
    
    print("Welcome to HANGMAN")
    print("-----------------------")
    print("Choose one of the following")
    print("1. Play the game as multiplayer")
    print("2. Play the game as single player")
    print("3. Instruction")
    print("4. Quit")
    
    inp = raw_input("\n-> ")
    
    if inp == "1":
        multiplayer()
    elif inp == "2":
        print("\n\nSingle player is under construction, should be here soon!")
        sleep(4)
        start_interface()
    elif inp == "3":
        instruction()
    elif inp == "4":
        quit()
    else:
        print("Invalid input, try again.")
        sleep(1)
        start_interface()     

correct_guess_made = ''
incorrect_guess_made = ''
guess = 6
start_interface()
