"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['colorama', 're', 'random', 'string']

Note: install colorama before running the code with: pip install colorama
"""
from random import choice
from HW03_Ishan_Aryendu_dictionary import Dictionary
from colorama import Fore
from HW03_Ishan_Aryendu_ui import UI
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
        """
        Generate a list of 5 lettered words
        :param all_words: 
        :return: 
        """
        tmp_word = choice(all_words)
        # debugging
        print(Fore.WHITE + '\nThe selected word is', tmp_word)
        return tmp_word

    def log_gameplay(self, log_file_loc: str, given_word: str, input_word: str, games_played: int, wins: int,
                     guess_dist: dict) -> object:
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
        exit()

    def get_match_char_list(self, file_path) -> str:
        _file = open(file_path, 'r')
        counter = 5
        res_string = ''
        for line in _file.readlines():
            res_string += line[0]
            counter -= 1
            if not counter:
                break
            # print(line[0])
        return res_string

    def solve(self, flag: bool, match: str = '?', mismatch: str = '?', pattern: str = '?') -> list:
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
        # print("Loaded " + str(len(words)) + " words from dictionary.")
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

        # llist = SLinkedList()
        lst = []
        for word in solutions:
            if pattern.match(word):
                if flag:
                    max -= 1
                    if max == 0:
                        # return llist
                        return lst
                # print(word)
                # llist.AtBegining(word)
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
        # MAX_TRIES = 6
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
        # given_word = ""
        given_word = wordle.gen_word(all_words)
        # ref = Ref()
        # ref.set_given_word(given_word)
        while prompt != "" and NO_GAMES>0:
            if prev_tries == len(all_words):
                self.play_wordle()
            self.ui.welcome_message(WORD_LENGTH, MAX_TRIES, games_played)
            # print("Ref Object stores: " + ref.get_given_word())
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
                wordle.log_gameplay(LOG_FILE_PATH, given_word, prev_tries, games_played, wins, guess_dist)
                # check for termination of the program
                if retries == MAX_TRIES and not flag:
                    self.ui.game_over()
                    break
                if NO_GAMES <= 0:
                    break


if __name__ == '__main__':
    w = Wordle()
    w.play_wordle()
