class HangmanGame:

    def draw_hanged_man(self):
        row = 11
        column = 7

        # for h in range(row):
        #     for w in range(column):
        #         print("-", end="")
        #     print("")

        for r in range(row):
            for c in range(column):
                # Check for first and last rows
                if c != 0 and c != 1 and r == 0 or r == row - 1:
                    print("-", end="")
                # Check for last column and rope
                elif c == column - 1 or r == 1 and c == 2:
                    print("|", end="")
                else:
                    print(" ", end="")
            print("")


def main() -> None:

    game = HangmanGame()
    game.draw_hanged_man()


if __name__ == "__main__":
    main()
