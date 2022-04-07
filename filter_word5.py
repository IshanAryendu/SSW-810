"""
__author__ = "Ishan Aryendu"
__credits__ = ["Tech With Tim (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "1.0"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"

"""
import HW03_Ishan_Aryendu_dictionary as d


class FilterWords:

    def __init__(self):
        self.SRC_FILE_PATH = 'resource/word_list'
        self.all_words = []
        self.DEST_FILE_PATH = 'resource/word5.txt'
        self.dictionary = d.Dictionary()

    def __str__(self):
        return f'The file is being read from {self.get_src_file_path()} and written onto {self.get_dest_file_path()}.'

    def set_src_file_path(self, src_file_path: str):
        self.SRC_FILE_PATH = src_file_path

    def set_all_words(self, all_words: list):
        self.all_words = all_words

    def set_dest_file_path(self, dest_file_path):
        self.DEST_FILE_PATH = dest_file_path

    def get_src_file_path(self, src_file_path: str):
        return self.SRC_FILE_PATH

    def get_all_words(self, all_words: list):
        return self.all_words

    def get_dest_file_path(self, dest_file_path):
        return self.DEST_FILE_PATH

    def add_words_to_file(self):
        all_words = list(self.dictionary.get_words_from_file(self.SRC_FILE_PATH, comment_char='#', word_length=5))
        textfile = open(self.DEST_FILE_PATH, "w")
        for element in all_words:
            textfile.write(element + "\n")
        textfile.close()


if __name__ == '__main__':
    fw = FilterWords()
    fw.add_words_to_file()
