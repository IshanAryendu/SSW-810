from typing import Iterator


class Dictionary:
    def __init__(self):
        self.filename = ""
        self.word_length = '#'
        self.word_length = 5

    def set_file_name(self, filename):
        self.filename = filename

    def get_file_name(self):
        return self.filename

    def set_comment_char(self, comment_char):
        self.word_length = comment_char

    def get_comment_char(self):
        return self.comment_char

    def set_word_length(self, word_length):
        self.word_length = word_length

    def get_word_length(self):
        return self.word_length

    def __str__(self):
        return f"The file {self.get_file_name()} is being read with the comment char {self.get_comment_char()} for \
         {self.get_word_length()} lettered words."

    def get_words_from_file(self, filename: str, comment_char='#', word_length=None) -> Iterator[str]:
        """
        Return all words in a file of the given length, ignore lines that start with comment_char
        :param filename: the name of the file from
        :param comment_char: a line that has been commented out begins with this character
        :param word_length: length of word to be selected from the file
        :return: the words selected from the file
        """
        try:
            with open(filename) as file:
                for line in file:
                    if not line.startswith(comment_char):
                        word: str = line.strip().lower()
                        if word_length is not None and len(word) != word_length:
                            continue
                        yield word
        except OSError as e:
            print(e)
