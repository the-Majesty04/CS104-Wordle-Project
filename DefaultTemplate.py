import random
import sys
def main():
    # Get a random word.
    answer = getRandomWord()

    # PUT YOUR CODE HERE.
    

# A helper method that prints the guess with the
# correct colors to the console.
def printGuessColors(guess, answer):
    return


# A helper method that determines the color
# of the letter in the guess.
def letterColor(index, guess, answer):
    return


# A method that gets a random word from a file.
def getRandomWord():
    # Choose the word to be the answer for testing purposes.
    if len(sys.argv) > 1:
        return sys.argv[1]
    else:
        file = open("words.txt", "r")
        # Strip removes the new line at the end of each word.
        words = [word.strip() for word in file.readlines()]

        return random.choice(words)

main()
