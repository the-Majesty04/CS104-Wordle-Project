def two_player():
    earlywin = False

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

    # If not exact match, or doesn't exist in answer -> Must exist somewhere in Answer therefore uses else

    # Game Set-up
    print("""Game Set-Up:
-------------------------""")
    status = False
    while status == False:
        answer = input("Enter Wordle Answer: ")
        if len(answer) != 5:
            print("Word Must Be Five Characters Or Less. Enter Again")
        else:
            response = input(f"You chose the answer, '{answer}', continue? Yes or No\n")
            if response == 'Yes':
                status = True
            else:
                status = False

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


