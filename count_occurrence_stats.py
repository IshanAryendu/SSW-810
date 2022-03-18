# Add a new module and relevant methods to count occurrence statistics of each letter at a particular index from the
# filtered dictionary. To obtain letter likelihood, you would need to count the number of times a particular letter
# appears in a given index and divide the count by the number of dictionary words. Hint: Use a dictionary data
# structure with each letter as the key and an initial count list of [0, 0, 0, 0, 0] where the count would be
# incremented with each word's letters at the corresponding index. Results should be stored in the
# "letterFrequency.csv" file such that each row is "letter, first_pos_%, second_pos_%, third_pos_%, fourth_pos_%,
# fifth_pos_%" without % sign.
import csv
import pandas as pd
import numpy as np


class Stats:
    def __init__(self):
        self.FILE_PATH = None
        FILE_PATH = ""
        self.words = []
        self.no_of_words = 0
        self.test_list = []

    def __str__(self):
        return f"{self.FILE_PATH}: Counting game statistics..."

    def set_file_path(self, file_path):
        self.FILE_PATH = file_path

    def get_file_path(self):
        return self.FILE_PATH

    def parse_file_as_dict_of_tuples(self, FILE_PATH: str):
        dictionary = {}
        with open(FILE_PATH, "r") as f:
            reader = csv.reader(f)
            next(reader)  # skip header
            for line in reader:
                dictionary[tuple(map(str, line[0].replace(',', '')))] = tuple(line[1:-1])

    def make_list_count_dict(self, words: list, no_of_words: int) -> dict:
        all_freq = {}
        default_list = [0, 0, 0, 0, 0]
        for word in words:
            pos = 0
            for i in word:
                if i in all_freq:
                    all_freq[i][pos] += 1 / no_of_words
                else:
                    all_freq[i] = default_list.copy()
                    all_freq[i][pos] = 1 / no_of_words
                pos += 1
        # printing result
        # print("Count of all characters is :\n "
        #       + str(all_freq))
        # print(type(all_freq))
        return all_freq

    def write_stats(self, test_list: list, my_dict: dict) -> object:
        with open("log/statistics.csv", 'w') as f:
            for word in test_list:
                pos = 0
                prob = 1
                for i in range(5):
                    prob = prob * (my_dict[word[pos]][pos])
                    pos += 1
                f.write("%s, %s\n" % (word, prob))
        f.close()

    def write_perc(self, my_dict: dict, FREQ_FILE_PATH = "log/letterFrequency.csv") -> object:
        FREQ_FILE_PATH = "log/letterFrequency.csv"
        with open(FREQ_FILE_PATH, 'w') as f:
            for key in my_dict.keys():
                f.write("%s, " % key)
                # f.write("%s,%s\n" % (key, my_dict[key]))
                for entry in my_dict[key]:
                    f.write("%s, " % (entry * 100))
                f.write("\n")
        f.close()

    def convert(self, lst: list) -> tuple:
        """
        convert list into a tuple
        :param list: a list of integers
        :return: tuple of integers
        """
        return tuple(lst)

    def covert_to_tuple(self, my_dict: dict) -> object:
        FREQ_FILE_PATH = "log/letterFrequency.csv"
        with open(FREQ_FILE_PATH, 'w') as f:
            for key in my_dict.keys():
                f.write("%s, %s,\n" % (key, self.convert(my_dict[key])))
                # f.write()
        f.close()

    def calculate_stats(self, inp_list: list) -> object:
        """
        inp_list : the input list to calculate statistics
        """
        no_of_words = len(inp_list)
        letter_summary = ['word', 'probability']
        no_of_words = len(inp_list)
        my_dict = self.make_list_count_dict(inp_list, no_of_words)
        self.write_stats(inp_list, my_dict)
        self.write_perc(my_dict)
        self.covert_to_tuple(my_dict)
        file = pd.read_csv("log/statistics.csv")
        file.to_csv("log/statistics.csv", header=letter_summary, index=False)
        csv_file = pd.read_csv("log/statistics.csv")
        sorted_csv = csv_file.sort_values(by=['probability'], ascending=False)
        sorted_csv.index = np.arange(1, len(sorted_csv) + 1)
        sorted_csv.index.name = "rank"
        sorted_csv.to_csv("resource/wordRank.csv", encoding='utf-8')
        sortedlist = sorted_csv.values.tolist()
        # print(sortedlist)
