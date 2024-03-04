from hangman import HangmanGame


def main() -> None:
    game = HangmanGame()

    while True:
        game.show_word()
        game.draw_hanged_man()

        try:
            game.get_guess_from_user()
        except ValueError:
            print("ERROR. Enter either a letter f.e. 'a' or a word f.e. 'apple'. ")

        if game.all_letters_guessed():
            print(game.show_inccorect_letters())
            print(game.show_inccorect_words())
            game.draw_hanged_man()
            game.print_game_won()
            break

        if game.game_won:
            print(game.show_inccorect_letters())
            print(game.show_inccorect_words())
            game.draw_hanged_man()
            game.print_game_won()
            break

        if game.score_is_6():
            print(game.show_inccorect_letters())
            print(game.show_inccorect_words())
            game.draw_hanged_man()
            game.print_game_over()
            break


if __name__ == "__main__":
    main()
