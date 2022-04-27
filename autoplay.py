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
import log_module as lm
import pandas
from HW03_Ishan_Aryendu_dictionary import Dictionary
from colorama import Fore
from count_occurrence_stats import Stats
from HW03_Ishan_Aryendu_ui import UI
import sys
from wordleSolver import Solve
from help import Help
import re
import string


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
        self.res_pattern = "_____"
        self.ui = UI()
        self.prev_tried_words = []

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

    def error_msg(self):
        print("Second argument should be exactly 5 characters long, consisting of letters and underscores only")
        sys.exit()

    def get_match_char_list(self, file_path):
        _file = open(file_path, 'r')
        counter = 5
        res_string = ''
        for line in _file.readlines():
            res_string += line[0]
            counter -= 1
            if not counter:
                break
        return res_string

    def solve(self, flag: bool, match: str = '?', mismatch: str = '?', pattern: str = '?'):
        match_file_path = 'log/letterFrequency.csv'
        if not mismatch:
            mismatch = '?'
        if not pattern:
            pattern = '?'
        if not match:
            flag = True
            match = self.get_match_char_list(match_file_path)
        dictionary = open("resource/word5.txt", "r")
        words = dictionary.readlines()
        dictionary.close()
        max = 51

        # this will be the array with the possible answers
        solutions = []

        # remove new lines from words in array, put them into solutions array
        for word in words:
            solutions.append(word.strip())

        # remove words without the necessary chars
        if match != '?':
            solutions = [x for x in solutions if all(y in x for y in match)]

        # remove words with characters that we know aren't in the solution
        # if mismatch != '?':
        #     solutions = [x for x in solutions if all(y not in x for y in mismatch)]

        regex = pattern

        if regex == '?':
            regex = "_____"
        allowed = set(string.ascii_lowercase + '_')
        if not set(regex) <= allowed:
            self.error_msg()
        if len(regex) != 5:
            self.error_msg()

        regex = regex.replace("_", ".")

        # match based on regex
        regex_pattern = "^" + regex + "$"
        pattern = re.compile(regex_pattern)

        lst = []
        for word in solutions:
            if pattern.match(word):
                if flag:
                    max -= 1
                    if max == 0:
                        # return llist
                        return lst
                lst.append(word)

        # return llist
        return lst

    def play_wordle(self, flag=None, given_word=None, match=None, mismatch=None, prev_tries=None, prompt=None,
                    retries=None):
        # set the default parameters
        wordle = Wordle()
        h = Help()
        s = Solve()
        NO_GAMES = 1
        WORD_LENGTH = 5
        MAX_TRIES = 100
        FILE_PATH = 'resource/word5.txt'
        LOG_FILE_PATH = 'log/gameplay.log'
        d = Dictionary()
        all_words = list(d.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH))
        max_limit = len(all_words)
        flag, given_word, self.match, self.mismatch, prev_tries, prompt, retries = self.ui.re_init(all_words, flag,
                                                                                                   given_word, match,
                                                                                                   mismatch,
                                                                                                   prev_tries, prompt,
                                                                                                   retries)
        prompt = "_____"
        games_played = 0
        wins = 0
        guess_dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        given_word = wordle.gen_word(all_words)
        while prompt != "" and NO_GAMES>0:
            if prev_tries == len(all_words):
                self.play_wordle()
            self.ui.welcome_message(WORD_LENGTH, MAX_TRIES, games_played)
            prev_tried_words = []
            # increment the number of games played
            games_played += 1
            countr = 0
            while retries != MAX_TRIES:
                try:
                    temp = wins
                    countr+=1
                    print("TRY: "+str(countr))
                    print("Pattern: " + self.ui.res_pattern)

                    f, pattern = h.help_my_autoplay(self.match, pattern=self.ui.res_pattern)
                    # # print(flag, " ", match, " ", mismatch, " ", pattern)
                    l = self.solve(f, self.match, self.mismatch, pattern=self.ui.res_pattern)
                    print(l)
                    print(prev_tried_words)
                    prompt = choice(l)
                    while prompt in prev_tried_words:
                        prompt = choice(l)
                    print(prompt)
                    prev_tried_words.append(prompt)
                    self.prev_tried_words.append(prompt)
                    inter_result = self.ui.auto_play(prompt, MAX_TRIES, WORD_LENGTH, self.match, self.mismatch,
                                                     games_played, all_words, prev_tries, given_word, retries,
                                                     guess_dist,
                                                     wins, self.ui)
                    if inter_result == "continue":
                        continue
                    elif inter_result is None:
                        break
                    else:
                        wins += inter_result
                    self.res_pattern = self.ui.res_pattern
                    print("Wodele pattern: " + self.res_pattern)
                except TypeError:
                    wins = temp
                self.ui.stats(games_played, wins, guess_dist)
                NO_GAMES -= 1
                given_word = wordle.gen_word(all_words)
                prev_tried_words = []
                print("given word:", given_word)
                print("prev_tries:", prev_tries)
                print("games_played", games_played)
                print("wins", wins)
                print("guess_dist", guess_dist)
                wordle.log_gameplay(LOG_FILE_PATH, given_word, prev_tries, games_played, wins, guess_dist)
                # s = Stats()
                # try:
                #     s.calculate_stats(prev_tries)
                # except pandas.errors.EmptyDataError:
                #     print("EXCEPTION OCCURRED")
                # check for termination of the program
                return wins, countr, prev_tries, given_word
                if len(prev_tries) == MAX_TRIES and not flag:
                # if retries == MAX_TRIES and not flag:
                    self.ui.game_over()
                    break
                if NO_GAMES <= 0:
                    break


if __name__ == '__main__':
    w = Wordle()
    lm.create_user_in_word()
    lm.create_win_stats()
    lm.create_log_table()
    for i in range(10):
        wins, retries, prev_tried_words, given_word = w.play_wordle()
        # print(wins, " : ", retries, " : ", tuple(prev_tried_words))
        temp_lst = []
        # insert prev_tried_words into the user_inp_words
        for ind, word in enumerate(prev_tried_words):
            if ind >=6:
                break
            temp_lst.append(word)
        lm.insert_user_in_word(lm.get_word_id(), prev_tried_words=temp_lst)
        # insert into win_stats
        lm.insert_user_win_stats(lm.get_win_id(), retires=retries)
        # insert into log
        lm.insert_log(given_word=given_word)
    inp = input("Do you want to specify a range of timestamp for search? [y/n]")
    if inp.lower() == 'y' or inp.lower() == 'yes':
        print("Enter the start timestamp and end timestamp in %Y-%m-%d (%H:%M:%S) format" \
              "eg. 2022-04-27 (18:44:44)")
        start_ts = input("start timestamp: ")
        end_ts = input("end timestamp: ")
        lm.select_in_range(start_ts, end_ts)
    else:
        lm.display_log()

