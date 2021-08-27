import random

WORDLIST_PATH = "assets/words.txt"  # TODO: don't make this hardcoded


def run_game():
    print("Welcome to Hangman 2022!")
    game_ended = False

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
