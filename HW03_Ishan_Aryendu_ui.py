"""
- A user interface module would contain functions to interact with the user, and ensure a proper word is provided.
"""
from io import StringIO
from colorama import Fore
import HW03_Ishan_Aryendu_wordle


def welcome_message(word_length, max_tries, games_played):
    """
    :param word_length: length of the chosen word
    :param max_tries: maximum number of user tries
    """
    print(Fore.GREEN + f'\nGuess a {word_length} letter word. You have {max_tries} chances. \nEnter an empty string to '
                       f'terminate. \nGame {games_played+1} BEGIN...')


def game_over():
    print(Fore.RED + 'GAME OVER!')


def user_input(WORD_LENGTH, MAX_TRIES, retries, match, mismatch, games_played, all_words, prev_tries, given_word, guess_dist, wins):
    """
    take the user input
    :param match:
    :param played:
    :param words:
    :param tries:
    :param word:
    :param dist:
    :param wins:
    """
    prompt = input(letter_status(match, mismatch) + Fore.WHITE + "\nEnter your guess: ").lower()
    try:
        if prompt == "":
            # print("UI func called")
            return "quit"
        elif HW03_Ishan_Aryendu_wordle.valid_input(prompt, WORD_LENGTH):
            return prompt
    except ValueError:
        print("Please provide a proper Value! ")
        HW03_Ishan_Aryendu_wordle.play(MAX_TRIES, WORD_LENGTH, match, mismatch, games_played, all_words, prev_tries, given_word, retries,
             guess_dist, wins)
    except TypeError:
        print("Please provide a proper Type! ")
        HW03_Ishan_Aryendu_wordle.play()
    else:
        print('\n' + Fore.WHITE + f'Chances left: {MAX_TRIES - retries}')
        return None


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


def previously_tried(prompt, prev_tries):
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


def set_char_color(letter_of_given_word, letter_of_input_word, given_word, match, mismatch, given_char_dict,
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
        # Decrement Dictionary value by 1
        given_char_dict[letter_of_given_word] = given_char_dict.get(letter_of_given_word, 0) - 1
        input_char_dict[letter_of_input_word] = input_char_dict.get(letter_of_input_word, 0) - 1
    elif letter_of_input_word in given_word and given_char_dict[letter_of_input_word] > 0 and \
            input_char_dict[letter_of_input_word] <= given_char_dict[letter_of_input_word]:
        letter_color, letter = (Fore.YELLOW, '`, ')
        match.add(letter_of_input_word)
        # Decrement Dictionary value by 1
        given_char_dict[letter_of_given_word] = given_char_dict.get(letter_of_given_word, 0) - 1
        input_char_dict[letter_of_input_word] = input_char_dict.get(letter_of_input_word, 0) - 1
    else:
        letter_color, letter = (Fore.RED, '", ')
        mismatch.add(letter_of_input_word)
    # print(char_dict)
    # if letter_of_input_word in given_word:
    #     match.add(letter_of_input_word)
    # else:
    #     assert isinstance(letter_of_input_word, object)
    #     mismatch.add(letter_of_input_word)
    print(letter_color + letter, end='')


def letter_status(match, mismatch):
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


def match_words(prompt, given_word, MAX_TRIES, retries):  # match the words
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


def not_in_list():
    """
    print that the word is not in the list
    """
    print(Fore.RED + 'Not in word list! Try Again...')
    return ""


def stats(games_played, wins, guess_dist):
    """
    display the game statistics (number of games played, win percentage, and the guess distribution)
    """
    print(f"Total number of games played: {games_played}")
    try:
        print(f"Win percentage: {(wins/games_played) * 100}")
    except TypeError:
        print(f"Win percentage: {(0/games_played) * 100}")
    finally:
        print(f"Guess distribution: ", end='')
        print(guess_dist)

