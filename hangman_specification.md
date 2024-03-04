## Hangman (D)

How it looks like [here](https://i.vimeocdn.com/video/1727623664-abc3c668b087e48ec826f30ef75a285dada9f1fc4c3a45eba37c254f3a0406cd-d?mw=700&mh=393). 

### Step 1: Set Up the Hangman Project

Your hangman game will select a word, handle user input, and display all output using a text-based user interface. You need code to handle each of these tasks. However, you’ll do everything using built-in and standard-library tools. You don’t need to install anything else.

### Step 2: Select a Word to Guess

The first step in playing hangman is to select the target word. When a human player selects a word for hangman, they pick one word from their own vocabulary. For the computer to select a word, it needs to have a vocabulary from which to select. Of course, its vocabulary doesn’t need to be as large as a human’s.

### Step 3: Get and Validate the Player’s Input

Now, you need a way to get the player’s guesses at the command line. After all, a game isn’t much of a game if there isn’t some way for the player to influence the outcome.

In your hangman game, you have to get the player’s input and make sure that it’s valid. Remember when you created your list of words? All the words were in lowercase, so you should turn the player’s guesses into lowercase letters as well.

Additionally, the player shouldn’t be able to guess the same letter twice. It’d also be good to avoid numbers, special characters, and complete words as well.

### Step 4: Display the Guessed Letters and Word

Once you’ve selected the target word in a real-life game of hangman, you need to write an underscore, or blank, for each letter in the word. These blanks tell the players how many letters are in the target word. As players make guesses, you fill in the blanks with the correct letters. You should also keep track of incorrect letters, which you write to the side.

### Step 5: Draw the Hanged Man

Of course, there’s no hangman game without the actual hanged man, is there? You could simply print out the number of guesses the player has taken. But if you want to make the game look like hangman, then showing the hanged man is a good idea.
Implement a function `draw_hanged_man` that, depending on the integer passed, will show different ASCII pictures 

```
>>> draw_hanged_man(0)
  -----
  |   |
      |
      |
      |
      |
      |
      |
      |
      |
-------

>>> draw_hanged_man(6)
  -----0
  |   |1
  O   |2 
 ---  |3
/ | \ |4
  |   |5
 ---  |6
/   \ |7
|   | |8
      |9
-------10
0123456

### Step 6: Figure Out When the Game Is Over

Games normally end due to a condition set up by the player’s input. Perhaps the player has finally reached the goal, or they failed some task and lost the game.

Your hangman game ends when one of two events happens:

- The player makes six incorrect guesses.
- The player guesses the word correctly.

Both of these outcomes stem from the player’s input. So, it makes sense to check for them in the game loop, which is where you gather, validate, and process all player input. Encapsulating these checks into a function is a good idea as well.

### Step 7: Run the Game Loop

Up to this point, you’ve assembled the functions and code that cover most of the important parts of your hangman game. Those parts include the following:

1. Selecting a random word to guess
2. Gathering and processing the player’s input
3. Showing the word with unguessed letters hidden
4. Showing the hanged man drawing
5. Tracking the letters guessed and guesses taken
6. Checking if the game is over
