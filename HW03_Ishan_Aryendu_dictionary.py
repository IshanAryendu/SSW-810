from typing import Iterator


def get_words_from_file(filename: str, comment_char='#', word_length=None) -> Iterator[str]:
    """
    Return all words in a file of the given length, ignore lines that start with comment_char
    :param filename: the name of the file from
    :param comment_char: a line that has been commented out begins with this character
    :param word_length: length of word to be selected from the file
    :return: the words selected from the file
    """
    with open(filename) as file:
        for line in file:
            if not line.startswith(comment_char):
                word: str = line.strip().lower()
                if word_length is not None and len(word) != word_length:
                    continue
                yield word
