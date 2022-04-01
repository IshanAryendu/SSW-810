"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['colorama', 're']

Note: install colorama before running the code with: pip install colorama
"""
from random import choice
from HW03_Ishan_Aryendu_dictionary import Dictionary
from colorama import Fore
from count_occurrence_stats import Stats
from HW03_Ishan_Aryendu_ui import UI


class Wordle:
    def __init__(self):
        self.tmp_word = ""
        self.log_file_loc = 'log/gameplay.log'
        self.given_word = ""
        self.input_word = ""
        self.games_played = 0
        self.wins = 0
        self.guess_dist = {}
        self.mismatch = {}
        self.match = {}
        self.res_pattern = ""
        self.ui = UI()

    def __str__(self):
        return f'The files are being logged at {self.log_file_loc}'

    def gen_word(self, all_words: list):
        tmp_word = choice(all_words)
        # debugging
        print(Fore.WHITE + '\nThe selected word is', tmp_word)
        return tmp_word

    def log_gameplay(self, log_file_loc: str, given_word: str, input_word: str, games_played: int, wins: int,
                     guess_dist: dict):
        # log the gameplay
        # selected word, user input, user report
        try:
            f = open(log_file_loc, "a")
            f.write(f"Selected word: {given_word}")
            f.write("\n")
            f.write(f"User's input: {input_word}")
            f.write("\n")
            f.write(f"Total number of games played: {games_played}")
            f.write("\n")
            f.write(f"Win percentage: {(wins / games_played) * 100}")
            f.write("\n")
            f.write(f"Guess distribution: {guess_dist}")
            f.write("\n")
        except Exception as e:
            print(e)
        finally:
            f.close()

    def play_wordle(self, flag=None, given_word=None, match=None, mismatch=None, prev_tries=None, prompt=None,
                    retries=None):
        # set the default parameters
        wordle = Wordle()
        WORD_LENGTH = 5
        MAX_TRIES = 6
        FILE_PATH = 'resource/word_list'
        LOG_FILE_PATH = 'log/gameplay.log'
        d = Dictionary()
        all_words = list(d.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH))
        max_limit = len(all_words)
        flag, given_word, self.match, self.mismatch, prev_tries, prompt, retries = self.ui.re_init(all_words, flag, given_word, match,
                                                                                    mismatch, prev_tries, prompt,
                                                                                    retries)
        prompt = "_____"
        games_played = 0
        wins = 0
        guess_dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        # given_word = ""
        given_word = wordle.gen_word(all_words)
        while prompt != "":
            if prev_tries == len(all_words):
                self.play_wordle()
            self.ui.welcome_message(WORD_LENGTH, MAX_TRIES, games_played)
            # increment the number of games played
            games_played += 1
            try:
                temp = wins
                wins += self.ui.play(MAX_TRIES, WORD_LENGTH, self.match, self.mismatch, games_played, all_words, prev_tries,
                                given_word, retries, guess_dist, wins)
                # self.res_pattern = self.ui.res_pattern
            except TypeError:
                wins = temp
            self.ui.stats(games_played, wins, guess_dist)
            given_word = wordle.gen_word(all_words)
            # debugging
            print(Fore.WHITE + '\nThe selected word is', given_word)
            wordle.log_gameplay(LOG_FILE_PATH, given_word, prev_tries, games_played, wins, guess_dist)
            s = Stats()
            s.calculate_stats(prev_tries)
            # check for termination of the program
            if retries == MAX_TRIES and not flag:
                self.ui.game_over()
                break


if __name__ == '__main__':
    w = Wordle()
    w.play_wordle()
