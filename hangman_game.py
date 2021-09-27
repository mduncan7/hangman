import random

WORDLIST_PATH = "assets/words.txt"  # TODO: don't make this hardcoded


def run_game():
    print("Welcome to Hangman 2022!")

    max_wrong_guesses = 3
    game_ended = False
    _the_word = pick_word()
    _correct_display = [None for _ in _the_word]
    _incorrect_guesses = list()

    while not game_ended:
        print("Playing...")
        print(_the_word)  # Temporary print for feedback

        display_ui(_correct_display, _incorrect_guesses)
        _guess = input("Guess a letter!")
        _correct_display, _incorrect_guesses = check_guess(_guess, _the_word, _correct_display, _incorrect_guesses)
        if len(_incorrect_guesses) == max_wrong_guesses:
            print("You lose, good day sir.")
            game_ended = True
        elif has_won(_correct_display, _the_word):
            print("You win!")
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
    """

    :param guess:
    :param word:
    :param correct_display:
    :param incorrect_guess:
    :return:
    """
    if guess in correct_display or guess in incorrect_guess:
        print('You already guessed that letter.')
    elif not guess.isalpha() or not len(guess) == 1:
        print('Make sure your guess is a single letter.')
    elif guess in word:
        _populate_correct_display(word, guess, correct_display)
        print('Correct')
    else:
        incorrect_guess.append(guess)
        print("Incorrect guess.")
    return correct_display, incorrect_guess


def _populate_correct_display(word, guess, correct_display):
    """

    :param word:
    :param guess:
    :param correct_display:
    :return:
    """
    guess_index = 0
    while guess_index < len(word):
        guess_index = word.find(guess, guess_index)
        if guess_index == -1:
            # str.find() returns -1 if value is not found.
            break
        correct_display[guess_index] = guess
        guess_index += 1


def has_won(correct_display: list, the_word: str) -> bool:
    """
    Check if the combined letters of `correct_display` are equal to `the_word`.

    :param correct_display:
    :param the_word:
    :return:
    """
    return the_word == "".join(map(str, correct_display))
