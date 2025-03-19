import random
import sys
from DefaultGame import default_game
from TwoPlayer import two_player
from Color_Add import color_add
from HardMode import hard_mode

def main():
    status=True
    print("It's Time To Play Wordle!")
    print("\033[91mMade By Majesty Milligan \033[0m")
    print("""Wordle!
Menu Start
-------------------""")
    while status:
        select_answer=False
        user_input=input ("""Select A Game Mode
        -> Default Game 
        -> Two player
        -> Color Add
        -> Hard Mode!\n""").lower()
        if user_input== "default game":
            print("""\nDefault Game:
            Enjoy Clasic Wordle, With Six Guesses Before Games Over!""")
            select_answer=input("Select? \n").lower()
            if select_answer != 'yes' and select_answer != 'no':
                print("Sorry, Either Input Yes Or No. ")
            elif select_answer=="yes":
                default_game()
                status=False
            

        elif user_input=="two player":
            print("""\nTwo Player Game Mode:
            Have One Player Enter a Five Letter Word To Guess, and Have the Other Try and Guess It In Six Tries!""")
            select_answer=input("Select? \n").lower()
            if select_answer != 'yes' and select_answer != 'no':
                print("Sorry, Either Input Yes Or No. ")
            elif select_answer=='yes':
                two_player()
                status=False

        elif user_input=="color add":
            print("""\nColor Add:
            Tired of Plain Text? Spice Up The Classic Game Mode With Colorful Text That Inidcates Green, Yellow, Or Red!""")
            select_answer=input("Select? \n").lower()
            if select_answer != 'yes' and select_answer != 'no':
                print("Sorry, Either Input Yes Or No. ")
            elif select_answer=='yes':
                color_add()
                status=False

        elif user_input=="hard mode":
            print("""\nHard Mode? Okay Tough One :
            Enter A Custom Amount of Guesses, and Try To Beat Your Own Goal!""")
            select_answer=input("Select? \n").lower()
            if select_answer != 'yes' and select_answer != 'no':
                print("Sorry, Either Input Yes Or No. ")
            elif select_answer=='yes':
                color_add()
                status=False
        else:
            print("Please Enter One of The Given Game Modes")
    print("Thanks For Playing!")


if __name__=="__main__":
    main()
# Color the letters in the console output (link on how to do this). 
# Input validation (if the user’s guess isn’t 5 letters long, keep asking them to input a 5 letter guess until they do).
# Normal vs Hard Mode. Ask the user what mode they want to play. If they select Hard Mode, then they only have 5 guesses to get the answer instead of the usual 6
# Allow user to input upper case OR lower case guesses
# Make a 2 player version of the game. Have the first player type in a 5 letter word (or for more of a coding challenge, any length letter word), then print out a bunch of blank lines, and then have the 2nd player try to guess the word

#Colors [ON/OFF] Check 
#Normal vs Hard [Five Guesses ]

