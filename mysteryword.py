# Mystery Word
# kp - my first draft is breaking down the requriements of the game into tiny steps
# kp - turning this in now so I don't have the mad rush to upload before class. I will update my code and resumbit later this morning. 

# from README.md
# You will implement the game Mystery Word. In your game, you will be playing against the computer.

# The computer must select a word at random from the list of words in the file `words.txt` from this repository.

# The game must be interactive;
# the flow of the game should go as follows:

# 1. Let the user choose a level of difficulty at the beginning of the program.
#   Easy mode only has words of 4-6 characters; normal mode only has words of 6-8 characters; hard mode only has words of 8+ characters. 
# kp - you have to select categories of characters that don't overlap

# kp - verify each variable and function along the way

# kp - breaking tasks into tiny, verifiable steps

# simplementation - with same word to ensure coding works (using coder selected word)

# code version where computer picks same word from words.txt

# code version where computer selects *any* random word in words.txt

# code version where computer selects random word in words.txt with:
#       if easy mode:  kp = less than 6 characters (easy mode)
#       if normal mode: kp = 6 to 8 characters  (normal mode)
#       if hard mode: kp = more than 8 characters  (hard mode)

#   TODO - may need to switch order of some of these steps

# user selects easy mode vs normal mode vs hard mode

# In Mystery Word, user plays against the computer so computer will greet user at start of game.
# 
# TODO - secondary tasks
#   code a greeting - "Hello Friend! Let's Get started with Mystery Word game.  Hit [something] so we can get started."
#   code a guess counter. A user is allowed 8 guesses. Remind the user of how many guesses they have left after each round.
#   code user loses quess only if guess incorrectly.  if user guesses correctly, user does not lose a guess 
#   code -- If the user guesses the same letter twice, do not take away a guess. Instead, print a message letting them know they've already guessed that letter and ask them to try again.
#   code - Hard Mode: 

#       use the following: Implement the [evil version of this game](http://nifty.stanford.edu/2011/schwarz-evil-hangman/).
#       Put it in a new Python program called "demon_words.py".

# TODO computer selects a word at random from words.txt

# 2. At the start of the game, let the user know how many letters the computer's word contains.
#   TODO - display blanks representing each character of the word

#   secondary
#       TODO - after greeting, ask user to choose mode (dificulty level)

#   kp - levels show no overlap in characters for words in word.text

#       if easy mode:  kp = less than 6 characters (easy mode)
#       if normal mode: kp = 6 to 8 characters  (normal mode)
#       if hard mode: kp = more than 8 characters  (hard mode) 

# 3. Ask the user to supply one guess (i.e. letter) per round. This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.
#   A user is allowed 8 guesses.

#   simplementation - to break down requirements into tiny steps

#   General game format, regardless of difficulty or pre-selected or random selected word

#   step 1 - User initiates the game and gets a greeting to get started ('go' or select difficulty level)
#   step 2 - Computer selects a word  (kp: given a word, pick word (i.e. word with characteristic x from words.txt from a list I assume exists), select any random word, select random word with particular character limit)
#   step 3 - Computer tells user how many characters in mystery word and tells user how many quesses she has. When computer prompts user to start guessing

#   kp - (secondary) include a round countdown so user knows how many quessses she has left
#   A user is allowed 8 guesses.
#      
#   step 4 - Ask the user to supply one guess (i.e. letter) per round.

#   kp - input is one upper or lowercase letter
#   kp - if input is more than one letter -- NO - "Invalid! Try Again."
#   kp - if input is non-letter -- NO - "Invalid! Try Again." 

#   TODO: insert loop for user round of questions
#   TODO: once user's number of quesses is up -- "Sorry!"
#   TODO: insert loop for user to restart game

#  This letter can be upper or lower case and it should not matter. If a user enters more than one letter, tell them the input is invalid and let them try again.

#   step 5 - compare user guessed letter to computer's selected word
#   step 6 - tell user
#        'no' if letter not in word
#        'yes' if letter is in word
#        if yes, show where letter appears in word among blanks for in guessed characters - e.g. ___ ____ ____ ____ ____ ____

#   TODO:   Let the user know *if* their guess appears in the computer's word. 

#   kp: simplementation version

#   TODO: Computer returns either Yes or No if guessed letter is in computer's word.
#   TODO:   Let the user know where the guessed character appears in computer's word
#   TODO:   Show the user where the guessed character appears in computer's word using blanks

#   step 7 - The game ends when the user constructs the full word or runs out of guesses. 
#   TODO - code - If the player runs out of guesses, reveal the word to the user when the game ends. 

#   step 8 - When a game ends, ask the user if she wantd\s to play again. The game begins again if she reply positively.