from random_words import RandomWords
import re


class HangmanGame:
    # Get random word
    def __init__(self) -> None:
        self.score = 0
        self.correct_letters = []
        self.inccorect_letters = []
        self.inccorect_words = []
        self.word = self.__get_random_word()
        # print(self.word)
        self._game_won = False

    @property
    def game_won(self):
        return self._game_won

    @game_won.setter
    def game_won(self, game_won):
        self._game_won = game_won

    def __get_random_word(self) -> str:
        min_letters = 4
        rw = RandomWords()
        word = rw.random_word(min_letter_count=min_letters)
        return word

    def score_is_7(self) -> bool:
        return self.score == 7

    def print_game_over(self) -> None:
        print(f"GAME OVER! Word to guess was '{self.word}'. ")

    def print_game_won(self) -> None:
        print(f"CONGRATS! You have succesfully guessed the word '{self.word}'. ")

    def all_letters_guessed(self):
        for letter in self.word:
            if letter not in self.correct_letters:
                return False
        return True

    def show_word(self) -> None:
        # Loop every letter in a word
        print(f"Guess a word: ", end="")
        for i in range(len(self.word)):
            # Check if letter was already guessed and print it if so
            if self.word[i] in self.correct_letters:
                print(f"{self.word[i]}", end="")
            # If letter was not guessed add it to incorrect list
            else:
                print("_", end="")
        print("")
        print(f"{self.show_inccorect_letters()}")
        print(f"{self.show_inccorect_words()}", end="")
        print("")

    def show_inccorect_letters(self) -> None:
        result = "Inccorect letters: " + ", ".join(
            (letter for letter in self.inccorect_letters)
        )
        return result

    def show_inccorect_words(self) -> None:
        result = "Inccorect words: " + ", ".join(
            (word for word in self.inccorect_words)
        )
        return result

    def guess_a_word(self, word: str) -> None:
        # Check for
        if word != self.word:
            # Check if word was not already guessed
            if word not in self.inccorect_words:
                print(f"'{word}' is an inccorect guess for a word. ")
                self.inccorect_words.append(word)
                self.score += 1
            else:
                print(f"Aready guessed. '{word}' is an inccorect guess for a word. ")
        else:
            self.game_won = True
            print(f"{word} is a correct guess for a word. ")

    def guess_a_letter(self, letter: str) -> None:
        # Check if letter is in a word
        if letter in self.word:
            # Check if letter was not guessed and append if so append to correct list
            if letter not in self.correct_letters:
                print(f"'{letter}' is in a word. ")
                self.correct_letters.append(letter)
            else:
                print(f"Already guessed. '{letter}' is in a word. ")
        else:
            # Check if letter was not already guessed
            if letter not in self.inccorect_letters:
                print(f"'{letter}' is NOT in a word. ")
                self.inccorect_letters.append(letter)
                self.score += 1
            else:
                print(f"Already guessed. '{letter}' is NOT in a word. ")

    def get_guess_from_user(self) -> None:
        word = input("Guess a letter or a word: ")

        # Check if user input is trying to guess a letter
        if len(word) == 1:
            # Check if user input alpabetical letter
            if re.search(r"^[A-za-z]$", word):
                word = word.lower()
                self.guess_a_letter(word)
            else:
                raise ValueError

        # Check if user is trying to guess a word
        else:
            # Check if user input a string word that is at least 2 letters
            if re.search(r"^[A-za-z]+$", word):
                word = word.lower()
                self.guess_a_word(word)
            else:
                raise ValueError

    def draw_hanged_man(self) -> None:
        row = 11
        column = 7

        for r in range(row):
            for c in range(column):
                # Print game window - upper and lower bound
                # Check for first and last rows
                if c != 0 and c != 1 and r == 0 or r == row - 1:
                    print("-", end="")

                # Print game window - right bound and a rope
                # Check for last column and rope
                elif c == column - 1 or r == 1 and c == 2:
                    print("|", end="")

                # Print head if score is 1
                elif self.score >= 1 and r == 2 and c == 2:
                    print("O", end="")

                # Print shoulders if score is 2
                elif self.score >= 2 and r == 3 and (c == 1 or c == 2 or c == 3):
                    print("-", end="")

                # Print left arm if score is 3
                elif self.score >= 3 and r == 4 and c == 0:
                    print("/", end="")

                # Print right arm if score is 3
                elif self.score >= 3 and r == 4 and c == 4:
                    print("\\", end="")

                # Print body if score is 4
                elif self.score >= 4 and c == 2 and (r == 4 or r == 5):
                    print("|", end="")

                # Print torso if score is 5
                elif self.score >= 5 and r == 6 and (c == 1 or c == 2 or c == 3):
                    print("-", end="")

                # Print left leg
                elif self.score >= 6 and c == 0 and r == 7:
                    print("/", end="")
                elif self.score >= 6 and c == 0 and r == 8:
                    print("|", end="")

                # Print right leg
                elif self.score >= 7 and c == 4 and r == 7:
                    print("\\", end="")
                elif self.score >= 7 and c == 4 and r == 8:
                    print("|", end="")

                # Print whitespace
                else:
                    print(" ", end="")

            print("")


def main(): ...


if __name__ == "__main__":
    main()
