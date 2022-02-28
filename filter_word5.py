from HW03_Ishan_Aryendu_dictionary import get_words_from_file


def add_words_to_file():
    SRC_FILE_PATH = 'resource/word_list'
    all_words = list(get_words_from_file(SRC_FILE_PATH, comment_char='#', word_length=5))
    DEST_FILE_PATH = 'resource/word5.txt'
    textfile = open(DEST_FILE_PATH, "w")
    for element in all_words:
        textfile.write(element + "\n")
    textfile.close()


if __name__ == '__main__':
    add_words_to_file()
