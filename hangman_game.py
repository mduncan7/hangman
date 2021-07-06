import random

WORDLIST_PATH = "assets/words.txt"  # TODO: don't make this hardcoded


class Hangman(object):
    def __init__(self):
        self._word = self.pick_word()
        self._word_len = len(self._word)
        self.game_ended = False

    def start(self):
        print("Welcome to Hangman 2022!")
        while not self.game_ended:
            print("Playing...")
            self.game_ended = True
        print("Bye.")

    def pick_word(self) -> str:
        with open(WORDLIST_PATH, "r") as f:
            raw_words = f.readlines()

        all_words = list()
        for word in raw_words:
            all_words.append(word.strip())

        return random.choice(all_words)
