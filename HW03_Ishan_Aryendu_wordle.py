"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org"]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['colorama', 're']

Pseudocode:
1. Set the word length and no of retries
2. Set target word to 'sonar'
3. repeat step 4 to 7 until success or error
4. Match the length of the selected word and the user input
    4.1. if length doesn't match, error message and retry
    4.2. if word has digits or special characters, error message and retry
    4.3. if word has been tried before, error message and retry
    4.4. else continue to step 5
5. compare each letter of the user input and the target word
    5.1. if the letters match, color it green for display
    5.2. else if the letter is in the target word, color it yellow for display
    5.3. else mark it 'x'
    5.4. if letter in the given word, add it to the 'match' set
    5.5. else add it to mismatch set
    5.6. print the letter with its color
6. if words match, print success message
7. keep track of retries
8. if chances exceed no of retries, print error message
"""
# colorama: Provides a simple cross-platform API to print colored terminal text from Python applications.
# install colorama before starting the project
from colorama import Fore
import re


if __name__ == '__main__':
    # set the default parameters
    GIVEN_WORD = 'sonar'
    WORD_LENGTH = 5
    MAX_TRIES = 6
    # debugging
    # print('The selected word is', GIVEN_WORD)
    # initialize the required variables
    retries = 0
    prompt = None
    flag = False
    # create sets to store matched letters, unmatched letters and previous words
    match = set()
    mismatch = set()
    prev_tries = set()
    print(Fore.GREEN + f'Guess a {WORD_LENGTH} letter word. You have {MAX_TRIES} chances. \nBEGIN...' + Fore.WHITE)
    while prompt != GIVEN_WORD and retries != MAX_TRIES:
        prompt = input(Fore.WHITE + "Enter your guess: ").lower()
        # compare length
        if len(prompt.strip()) != WORD_LENGTH:
            print(Fore.RED + f"Try again with a {WORD_LENGTH} letter word.")
            print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
            continue
        # check for valid input
        elif not (bool(re.match('^[a-zA-Z]*$', prompt)) is True):
            print(Fore.RED + "Enter a word without numbers or special characters.")
            print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
            continue
        # check if the word has been used before
        elif prompt in prev_tries:
            print(Fore.YELLOW + f"You have already tried {prompt}")
            continue
        else:
            # set the color from tuple of letters using the GIVEN_WORD and the word from the user's input
            for letter_of_chosen_word, letter_of_input_word in zip(GIVEN_WORD, prompt):
                letter_color, letter = (
                    Fore.GREEN, letter_of_chosen_word) if letter_of_chosen_word == letter_of_input_word \
                    else (Fore.YELLOW, letter_of_input_word) if letter_of_input_word in GIVEN_WORD \
                    else (Fore.WHITE, 'x')
                if letter_of_input_word in GIVEN_WORD:
                    match.add(letter_of_input_word)
                else:
                    assert isinstance(letter_of_input_word, object)
                    mismatch.add(letter_of_input_word)
                print(letter_color + letter, end='')
            # add the word to the set of previous words
            prev_tries.add(prompt)
        # increment the counter
        retries += 1
        # match the words
        if prompt == GIVEN_WORD:
            print('\nSpot on!!!')
            flag = True
        else:
            print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
    # check for termination of the program
    if retries == MAX_TRIES and not flag:
        print(Fore.RED + 'GAME OVER!')
