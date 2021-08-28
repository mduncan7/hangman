import random

WORDLIST_PATH = "assets/words.txt"  # TODO: don't make this hardcoded


def run_game():
    print("Welcome to Hangman 2022!")

    max_wrong_guesses = 2
    game_ended = False
    _the_word = pick_word()
    _correct_display = [None for _ in _the_word]
    _incorrect_guesses = list()

    while not game_ended:
        print("Playing...")
        game_ended = True

    print("Bye.")


def pick_word() -> str:
    with open(WORDLIST_PATH, "r") as f:
        raw_words = f.readlines()

    all_words = list()
    for word in raw_words:
        all_words.append(word.strip())

    return random.choice(all_words)


def display_ui(correct_display: list, incorrect_guesses: list) -> None:
    print("This is the UI.")
    print(f"This is the displayed list: {correct_display}")
    print(f"This is the incorrect guess list: {incorrect_guesses}")


def check_guess(guess: str, word: str, correct_display: list, incorrect_guess: list):
    incorrect_guess.append(guess)
    print("I have checked the guess")
    return correct_display, incorrect_guess


def has_won(correct_display: list) -> bool:
    # True if correct display is the same as the word
    # This could be either that there are no longer any `None` values
    # or the list could be converted to a string and checked against the word.
    return True
