from random_words import RandomWords


class HangmanGame:
    # Get random word
    def __init__(self):
        self.level = None

    def get_random_word(self) -> str:
        min_letters = 10
        rw = RandomWords()
        word = rw.random_word(min_letter_count=min_letters)
        return word

    def show_game_instructions(self):
        print("Welcome to deadman game")
        print("")
        print("The goal of the game is to guess a word by choosing letters. ")
        print("You have 6 guesses in total to guess ")
        print("Write 'start' to start the game")
        print("")
        print("Write 'exit' to exit from program or active game")
        print("")

    def draw_hanged_man(self, score=0) -> None:
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
                elif score >= 1 and r == 2 and c == 2:
                    print("O", end="")

                # Print shoulders if score is 2
                elif score >= 2 and r == 3 and (c == 1 or c == 2 or c == 3):
                    print("-", end="")

                # Print left arm if score is 3
                elif score >= 3 and r == 4 and c == 0:
                    print("/", end="")

                # Print right arm if score is 3
                elif score >= 3 and r == 4 and c == 4:
                    print("\\", end="")

                # Print body if score is 4
                elif score >= 4 and c == 2 and (r == 4 or r == 5):
                    print("|", end="")

                # Print torso if score is 5
                elif score >= 5 and r == 6 and (c == 1 or c == 2 or c == 3):
                    print("-", end="")

                # Print left leg
                elif score >= 6 and c == 0 and r == 7:
                    print("/", end="")
                elif score >= 6 and c == 0 and r == 8:
                    print("|", end="")

                # Print right leg
                elif score >= 6 and c == 4 and r == 7:
                    print("\\", end="")
                elif score >= 6 and c == 4 and r == 8:
                    print("|", end="")

                # Print whitespace
                else:
                    print(" ", end="")

            print("")


def main() -> None:

    game = HangmanGame()

    word = game.get_random_word()
    print(word)

    game.draw_hanged_man(6)


if __name__ == "__main__":
    main()
