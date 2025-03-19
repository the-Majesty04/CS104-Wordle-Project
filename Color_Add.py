import random 
import sys
def  color_add():
    earlywin = False
    answer= getRandomWord()

    def letterColor(phrase, answer):
        nonlocal earlywin
        Green = 0
        Yellow = 0
        Red = 0

        for phrase_letter, answer_letter in zip(phrase, answer):
            # Pairs strings together into Pairs and goes through them as a pair
            if phrase_letter == answer_letter:
                print("\033[92m"+phrase_letter+" \033[0m")
                Green += 1
                if Green == 5:
                    earlywin = True
                    return
            # If letter matches pair then print Green
            elif phrase_letter not in answer:
                print("\033[91m"+phrase_letter + "\033[0m")
                Red += 1
            # Checks for just Phrase Letter in entire Answer
            else:
                print("\033[93m"+phrase_letter + "\033[0m")
                Yellow += 1


    print("""Game Start
-------------------------""")
    ordinals = {0: "First", 1: "Second", 2: "Third", 3: "Fourth", 4: "Fifth", 5: "Sixth"}
    attempts = 0
    print("Guess The 5-Letter Word In Six Guesses!")
    while attempts < 6 and earlywin == False:
        user1_guess = input(f"Enter Your {ordinals[attempts]} Guess: ")
        letterColor(user1_guess, answer)
        attempts += 1

    if earlywin == True:
        print(f"You Won! You were on your {ordinals[attempts - 1]} Try!")
    else:
        print(f"You Lost, the answer was {answer}.")




# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("/Users/majesty/Python Projects/Wordle Project/words.txt")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)


