import random 
import sys
def hard_mode():
    earlywin = False
    answer= getRandomWord()
    Status=True 
    def letterColor(phrase, answer):
        nonlocal earlywin
        Green = 0
        Yellow = 0
        Red = 0

        for phrase_letter, answer_letter in zip(phrase, answer):
            # Pairs strings together into Pairs and goes through them as a pair
            if phrase_letter == answer_letter:
                print(phrase_letter + "-Green")
                Green += 1
                if Green == 5:
                    earlywin = True
                    return
            # If letter matches pair then print Green
            elif phrase_letter not in answer:
                print(phrase_letter + "-Red")
                Red += 1
            # Checks for just Phrase Letter in entire Answer
            else:
                print(phrase_letter + "-Yellow")
                Yellow += 1


    print("""Game Start
-------------------------""")
    ordinals = {0: "First", 1: "Second", 2: "Third", 3: "Fourth", 4: "Fifth", 5: "Sixth"}
    guesses=0
    print("Guess The 5-Letter Word In Five Guesses!")
    print("HARD MODE DETECTED: Input Custom Number of Guesses Must be Less Than Six.")
    while Status:
        attempts=int(input("Number of Attemps? -> "))
        if attempts < 6 and attempts > 0:
            print(f"You Entered {attempts}.")
            response= input("Sure You Wanna Continue? \n").lower()
            if response== 'yes':
                Status= False
        elif attempts <0 or attempts > 5:
            print("Must Be Less Than Six Numbers, or More Than Zero.")
            
    while guesses < attempts and earlywin == False:
        user1_guess = input(f"Enter Your {ordinals[guesses]} Guess: ")
        letterColor(user1_guess, answer)
        guesses += 1

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



