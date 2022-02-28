"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['colorama', 're']

Note: install colorama before running the code with: pip install colorama
"""
from random import choice
from HW03_Ishan_Aryendu_dictionary import *
from colorama import Fore

import re
import sys

from HW03_Ishan_Aryendu_ui import *


def main(flag=None, given_word=None, match=None, mismatch=None, prev_tries=None, prompt=None, retries=None):
    # set the default parameters
    # given_word = 'sonar'
    # given_word = 'sooon'
    WORD_LENGTH = 5
    MAX_TRIES = 6
    FILE_PATH = 'resource/word5.txt'
    LOG_FILE_PATH = 'log/gameplay.log'
    all_words = list(get_words_from_file(FILE_PATH, word_length=WORD_LENGTH))
    max_limit = len(all_words)
    flag, given_word, match, mismatch, prev_tries, prompt, retries = re_init(all_words, flag, given_word, match,
                                                                             mismatch, prev_tries, prompt, retries)
    prompt = "_____"
    games_played = 0
    wins = 0
    guess_dist = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
    # given_word = ""
    given_word = gen_word(all_words)
    while prompt != "":
        if prev_tries == len(all_words):
            main()
        welcome_message(WORD_LENGTH, MAX_TRIES, games_played)
        # increment the number of games played
        games_played += 1
        try:
            temp = wins
            wins += play(MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries, given_word,
                         retries, guess_dist, wins)
        except TypeError:
            wins = temp
        # while retries != MAX_TRIES:
        #     prompt = user_input(WORD_LENGTH, MAX_TRIES, retries, match, mismatch)
        #     if prompt == "":
        #         games_played -= 1
        #         break
        #     elif prompt not in all_words:
        #         not_in_list()
        #         continue
        #     # if prompt is None or HW03_Ishan_Aryendu_ui.previously_tried(prompt, prev_tries):
        #     #     continue
        #     if previously_tried(prompt, prev_tries):
        #         continue
        #     # HW03_Ishan_Aryendu_ui.letter_status(match, mismatch)
        #     prev_tries.add(prompt)
        #     # given_char_dict = {}
        #     # input_char_dict = {}
        #     given_char_dict = create_char_dict(given_word)
        #     # print(given_char_dict)
        #     input_char_dict = create_char_dict(prompt)
        #     # print(input_char_dict)
        #     # green_dict = {}
        #     # yellow_set = set()
        #     # red_set = set()
        #     for letter_of_given_word, letter_of_input_word in zip(given_word, prompt):
        #         set_char_color(letter_of_given_word, letter_of_input_word, given_word, match,
        #                                              mismatch, given_char_dict, input_char_dict)
        #     # increment the counter
        #     retries += 1
        #
        #     # match the words
        #     flag = match_words(prompt, given_word, MAX_TRIES, retries)
        #     if flag:
        #         # update guess distribution
        #         guess_dist[retries] += 1
        #         flag, given_word, match, mismatch, prev_tries, prompt, retries = re_init(all_words, flag, given_word,
        #                                                                                  match,
        #                                                                                  mismatch, prev_tries, prompt,
        #                                                                                  retries)
        #         wins += 1
        #         break
        stats(games_played, wins, guess_dist)
        given_word = gen_word(all_words)
        # debugging
        print(Fore.WHITE + '\nThe selected word is', given_word)
        log_gameplay(LOG_FILE_PATH, given_word, prev_tries, games_played, wins, guess_dist)
        # check for termination of the program
        if retries == MAX_TRIES and not flag:
            game_over()
            break


def gen_word(all_words):
    tmp_word = choice(all_words)
    # debugging
    print(Fore.WHITE + '\nThe selected word is', tmp_word)
    return tmp_word


def valid_input(prompt: str, word_length: int):
    """
    validate the user input
    """
    if type(prompt) != str:
        raise TypeError("Invalid type")
    if len(prompt) != word_length:
        raise ValueError("Invalid word length")
    if len(prompt.strip()) != word_length:
        print(Fore.RED + f"Try again with a {word_length} letter word.")
        return False
    elif not (bool(re.match('^[a-zA-Z]*$', prompt)) is True):
        print(Fore.RED + "Enter a word without numbers or special characters.")
        return False
    else:
        return True


def create_char_dict(word):
    """
    create a character dictionary
    """
    char_dict = {}
    for char in word:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def re_init(all_words, flag, given_word, match, mismatch, prev_tries, prompt, retries):
    """
    re-initialize the variables
    """
    # given_word = "sooon"
    # given_word = choice(all_words)
    # # debugging
    # print(Fore.WHITE + '\nThe selected word is', given_word)
    # initialize the required variables
    retries = 0
    prompt = "_____"
    flag = False
    match = set()
    mismatch = set()
    prev_tries = set()
    return flag, given_word, match, mismatch, prev_tries, prompt, retries


def play(MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries, given_word, retries,
         guess_dist, wins):
    while retries != MAX_TRIES:
        prompt = user_input(WORD_LENGTH, MAX_TRIES, retries, match, mismatch, games_played, all_words, prev_tries,
                            given_word, guess_dist, wins)
        # print('"'+prompt+'"')
        if prompt == "quit":
            exit_func()
            break
        elif prompt not in all_words:
            not_in_list()
            continue
        # if prompt is None or HW03_Ishan_Aryendu_ui.previously_tried(prompt, prev_tries):
        #     continue
        if previously_tried(prompt, prev_tries):
            continue
        # HW03_Ishan_Aryendu_ui.letter_status(match, mismatch)
        prev_tries.add(prompt)
        # given_char_dict = {}
        # input_char_dict = {}
        given_char_dict = create_char_dict(given_word)
        # print(given_char_dict)
        input_char_dict = create_char_dict(prompt)
        # print(input_char_dict)
        # green_dict = {}
        # yellow_set = set()
        # red_set = set()
        for letter_of_given_word, letter_of_input_word in zip(given_word, prompt):
            set_char_color(letter_of_given_word, letter_of_input_word, given_word, match,
                           mismatch, given_char_dict, input_char_dict)
        # increment the counter
        retries += 1

        # match the words
        flag = match_words(prompt, given_word, MAX_TRIES, retries)
        if flag:
            # update guess distribution
            guess_dist[retries] += 1
            flag, given_word, match, mismatch, prev_tries, prompt, retries = re_init(all_words, flag, given_word,
                                                                                     match,
                                                                                     mismatch, prev_tries, prompt,
                                                                                     retries)
            # wins += 1
            return 1


def log_gameplay(log_file_loc, given_word, input_word, games_played, wins, guess_dist):
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


def exit_func():
    game_over()
    sys.exit("Quitting...")

if __name__ == '__main__':
    main()
