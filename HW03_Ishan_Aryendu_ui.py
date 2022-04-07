"""
- A user interface module would contain functions to interact with the user, and ensure a proper word is provided.
"""
from io import StringIO
from colorama import Fore
from wordleSolver import Solve
import re
import sys


class UI:
    def __init__(self):
        self.WORD_LENGTH = 5
        self.MAX_TRIES = 6
        self.retries = 0
        self.match = {}
        self.mismatch = {}
        self.games_played = 0
        self.all_words = []
        self.prev_tries = {}
        self.given_word = ""
        self.guess_dist = {}
        self.wins = 0
        self.res_pattern = ""

    def set_word_length(self, word_length):
        self.WORD_LENGTH = word_length

    def set_max_tries(self, max_tries):
        self.MAX_TRIES = max_tries

    def set_retries(self, retries):
        self.retries = retries

    def set_mismatch(self, mismatch):
        self.mismatch = mismatch

    def set_games_played(self, games_played):
        self.games_played = games_played

    def set_all_words(self, all_words):
        self.all_words = all_words

    def set_prev_tries(self, prev_tries):
        self.prev_tries = prev_tries

    def set_given_word(self, given_word):
        self.given_word = given_word

    def set_guess_dist(self, guess_dist):
        self.guess_dist = guess_dist

    def set_wins(self, wins):
        self.wins = wins

    def get_word_length(self):
        return self.WORD_LENGTH

    def get_max_tries(self):
        return self.MAX_TRIES

    def get_retries(self):
        return self.retries

    def get_mismatch(self):
        return self.mismatch

    def get_games_played(self):
        return self.games_played

    def get_all_words(self):
        return self.all_words

    def get_prev_tries(self):
        return self.prev_tries

    def get_given_word(self):
        return self.given_word

    def get_guess_dist(self):
        return self.guess_dist

    def get_wins(self):
        return self.wins

    def __str__(self):
        return f'You have played {self.games_played} with {self.wins} wins!'

    def welcome_message(self, word_length, max_tries, games_played):
        """
        :param word_length: length of the chosen word
        :param max_tries: maximum number of user tries
        """
        print(
            Fore.GREEN + f'\nGuess a {word_length} letter word. You have {max_tries} chances. \nEnter an empty string to '
                         f'terminate. \nGame {games_played + 1} BEGIN...')

    def game_over(self):
        print(Fore.RED + 'GAME OVER!')

    def valid_input(self, prompt: str, word_length: int):
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

    def user_input(self, WORD_LENGTH: object, MAX_TRIES: object, retries: object, match: object, mismatch: object,
                   games_played: object, all_words: object, prev_tries: object,
                   given_word: object,
                   guess_dist: object,
                   wins: object) -> object:
        """
        take the user input
        :param WORD_LENGTH:
        :param MAX_TRIES:
        :param retries:
        :param mismatch:
        :param games_played:
        :param all_words:
        :param prev_tries:
        :param given_word:
        :param guess_dist:
        :param wins:
        :return: prompt if it is valid
        """
        prompt = input(self.letter_status(match, mismatch) + Fore.WHITE + "\nEnter your guess: ").lower()
        try:
            if prompt == "":
                # print("UI func called")
                return "quit"
            elif self.valid_input(prompt, WORD_LENGTH):
                return prompt
        except ValueError:
            print("Please provide a proper Value! ")
            self.play(MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries, given_word, retries,
                      guess_dist, wins)
        except TypeError:
            print("Please provide a proper Type! ")
            self.play()
        else:
            print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
            return None

    def exit_func(self):
        self.game_over()
        sys.exit("Quitting...")

    def create_char_dict(self, word):
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

    def re_init(self, all_words, flag, given_word, match, mismatch, prev_tries, prompt, retries):
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

    def play(self, MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries, given_word, retries,
             guess_dist, wins):
        """
        :param MAX_TRIES:
        :param WORD_LENGTH:
        :param match:
        :param mismatch:
        :param games_played:
        :param all_words:
        :param prev_tries:
        :param given_word:
        :param retries:
        :param guess_dist:
        :param wins:
        :return: count as 1 if everything goes without any errors
        """
        while retries != MAX_TRIES:
            prompt = self.user_input(WORD_LENGTH, MAX_TRIES, retries, match, mismatch, games_played, all_words,
                                     prev_tries,
                                     given_word, guess_dist, wins)
            # print('"'+prompt+'"')
            if prompt == "quit":
                self.exit_func()
                break
            elif prompt not in all_words:
                self.not_in_list()
                continue
            # if prompt is None or HW03_Ishan_Aryendu_ui.previously_tried(prompt, prev_tries):
            #     continue
            if self.previously_tried(prompt, prev_tries):
                continue
            # HW03_Ishan_Aryendu_ui.letter_status(match, mismatch)
            prev_tries.add(prompt)
            File_object = open(r"log/pattern.txt", "w")
            # given_char_dict = {}
            # input_char_dict = {}
            given_char_dict = self.create_char_dict(given_word)
            # print(given_char_dict)
            input_char_dict = self.create_char_dict(prompt)
            # print(input_char_dict)
            # green_dict = {}
            # yellow_set = set()
            # red_set = set()
            self.res_pattern = ""
            for letter_of_given_word, letter_of_input_word in zip(given_word, prompt):
                self.set_char_color(letter_of_given_word, letter_of_input_word, given_word, match,
                                    mismatch, given_char_dict, input_char_dict)
            # increment the counter
            retries += 1
            # print(self.res_pattern)
            File_object.write(self.res_pattern)

            # match the words
            flag = self.match_words(prompt, given_word, MAX_TRIES, retries)
            if flag:
                # update guess distribution
                guess_dist[retries] += 1
                flag, given_word, match, mismatch, prev_tries, prompt, retries = self.re_init(all_words, flag,
                                                                                              given_word,
                                                                                              match,
                                                                                              mismatch, prev_tries,
                                                                                              prompt,
                                                                                              retries)
                # wins += 1
                return 1

    def auto_play(self, prompt, MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries,
                  given_word, retries,
                  guess_dist, wins, ui):
        if prompt == "quit":
            self.exit_func()
            return
        elif prompt not in all_words:
            self.not_in_list()
            self.auto_play(prompt, MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries,
                           given_word, retries,
                           guess_dist, wins)
        if self.previously_tried(prompt, prev_tries):
            self.auto_play(prompt, MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries,
                           given_word, retries,
                           guess_dist, wins, ui)
        prev_tries.add(prompt)
        File_object = open(r"log/pattern.txt", "w")
        given_char_dict = self.create_char_dict(given_word)
        input_char_dict = self.create_char_dict(prompt)
        self.res_pattern = ""
        for letter_of_given_word, letter_of_input_word in zip(given_word, prompt):
            self.set_char_color(letter_of_given_word, letter_of_input_word, given_word, match,
                                mismatch, given_char_dict, input_char_dict)
        # increment the counter
        retries += 1
        print("\nPattern in UI: " + self.res_pattern)
        # ref.set_pattern(self.res_pattern)
        # print("\nPattern in UI ref: " + ref.get_pattern())
        ui.res_pattern = self.res_pattern
        File_object.write(self.res_pattern)

        # match the words
        flag = self.match_words(prompt, given_word, MAX_TRIES, retries)
        if flag:
            # update guess distribution
            guess_dist[retries] += 1
            flag, given_word, match, mismatch, prev_tries, prompt, retries = self.re_init(all_words, flag,
                                                                                          given_word,
                                                                                          match,
                                                                                          mismatch, prev_tries,
                                                                                          prompt,
                                                                                          retries)
            # wins += 1
            return 1
        else:
            return "continue"

    # def valid_input(prompt: str, word_length: int):
    #     """
    #     validate the user input
    #     """
    #     if len(prompt.strip()) != word_length:
    #         print(Fore.RED + f"Try again with a {word_length} letter word.")
    #         return False
    #     elif not (bool(re.match('^[a-zA-Z]*$', prompt)) is True):
    #         print(Fore.RED + "Enter a word without numbers or special characters.")
    #         return False
    #     else:
    #         return True

    def previously_tried(self, prompt, prev_tries):
        """
        check if a string has been tried before
        """
        if prompt.lower() in prev_tries:
            print(Fore.YELLOW + f"You have already tried {prompt}")
            return True
        else:
            return False

    # def set_green(given_word, input_word, match, green_dict, pos):
    #     for letter_of_given_word, letter_of_input_word in zip(given_word, input_word):
    #         if letter_of_given_word == letter_of_input_word:
    #             match.add(letter_of_input_word)
    #             green_dict[pos] = letter_of_input_word
    #     return green_dict

    def set_char_color(self, letter_of_given_word, letter_of_input_word, given_word, match, mismatch, given_char_dict,
                       input_char_dict):
        """
        set the character color depending on their position
        """
        # letter_color, letter = (Fore.GREEN, letter_of_given_word) if letter_of_given_word == letter_of_input_word \
        #     else (Fore.YELLOW, letter_of_input_word) if letter_of_input_word in given_word \
        #     else (Fore.WHITE, 'x')

        # letter_color, letter = (Fore.GREEN, letter_of_given_word + ', ') if letter_of_given_word == letter_of_input_word \
        #     else (Fore.YELLOW, '`, ') if letter_of_input_word in given_word \
        #     else (Fore.RED, '", ')
        if letter_of_given_word == letter_of_input_word:
            letter_color, letter = (Fore.GREEN, letter_of_given_word + ', ')
            match.add(letter_of_input_word)
            self.res_pattern += letter_of_given_word
            # Decrement Dictionary value by 1
            given_char_dict[letter_of_given_word] = given_char_dict.get(letter_of_given_word, 0) - 1
            input_char_dict[letter_of_input_word] = input_char_dict.get(letter_of_input_word, 0) - 1
        elif letter_of_input_word in given_word and given_char_dict[letter_of_input_word] > 0 and \
                input_char_dict[letter_of_input_word] <= given_char_dict[letter_of_input_word]:
            letter_color, letter = (Fore.YELLOW, '`, ')
            match.add(letter_of_input_word)
            self.res_pattern += '_'
            # Decrement Dictionary value by 1
            given_char_dict[letter_of_given_word] = given_char_dict.get(letter_of_given_word, 0) - 1
            input_char_dict[letter_of_input_word] = input_char_dict.get(letter_of_input_word, 0) - 1
        else:
            letter_color, letter = (Fore.RED, '", ')
            mismatch.add(letter_of_input_word)
            self.res_pattern += '_'
        # print(char_dict)
        # if letter_of_input_word in given_word:
        #     match.add(letter_of_input_word)
        # else:
        #     assert isinstance(letter_of_input_word, object)
        #     mismatch.add(letter_of_input_word)
        print(letter_color + letter, end='')

    def letter_status(self, match, mismatch):
        """
        write the satus of the letter to the buffer
        """
        buffer: StringIO = StringIO()
        for char_code in range(ord('a'), ord('z') + 1):
            char = chr(char_code)
            color = Fore.GREEN if char in match else Fore.RED if char in mismatch else Fore.WHITE
            buffer.write(color)
            buffer.write(char)
            # if color == Fore.RED:
            #     buffer.write("\'")
            # elif color != Fore.GREEN:
            #     buffer.write("\"")
            buffer.write(Fore.WHITE + ', ')
        return buffer.getvalue()

    def match_words(self, prompt, given_word, MAX_TRIES, retries):  # match the words
        """
        match if the two words are the same
        """
        if prompt == given_word:
            print('\nSpot on!!!')
            flag = True
        else:
            print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
            flag = False
        return flag

    def not_in_list(self):
        """
        print that the word is not in the list
        """
        print(Fore.RED + 'Not in word list! Try Again...')
        return ""

    def stats(self, games_played, wins, guess_dist):
        """
        display the game statistics (number of games played, win percentage, and the guess distribution)
        """
        print(f"Total number of games played: {games_played}")
        try:
            print(f"Win percentage: {(wins / games_played) * 100}")
        except TypeError:
            print(f"Win percentage: {(0 / games_played) * 100}")
        finally:
            print(f"Guess distribution: ", end='')
            print(guess_dist)
