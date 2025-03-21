In the code I utilized several key Python techniques to structure my game logic .

I used loops to control iteration, such as a for loop together with a zip() function  in TwoPlayer.py: “for phrase_letter, answer_letter in zip(phrase, answer):”, which allows simultaneous iteration through both phrase and answer. Additionally, I implemented a while loop in Wordle.py: “while status: print("It’s Time To Play Wordle!")”, ensuring the game always runs while status remains True.

For the decision-making element I  used conditionals like an if statement in Color_Add.py: “if phrase_letter == answer_letter: Green += 1”, which first checks for correct letter matches and then updates a counter after.

To maintain modularity, I structured my code with functions, such as the one in DefaultGame.py: “def default_game(): earlywin = False answer = getRandomWord()”, encapsulating the game logic for reuse.

I worked with data structures like lists to store game words, as seen in words.txt: “words = [word.strip() for word in open("words.txt").readlines()]”, where words are read and stored efficiently. I also used tuples in Color_Add.py: “color_counts = (Green, Yellow, Red)”, ensuring immutable storage of color counts.

String manipulation played a key role in handling input, demonstrated in DefaultTemplate.py: “answer = getRandomWord().strip().lower()”, which standardizes formatting by removing whitespace and converting words to lowercase.

To manage external files, I used file handling, such as in Wordle.py: “with open("words.txt", "r") as file: words = file.readlines()”, reading words from a file into a list for use in the game.

This is a Sophomore Year Project, Please download every file to ensure smooth game performance! 

Thanks : )
