"""
__author__ = "Ishan Aryendu"
__credits__ = ["NeuralNine (YouTube)", "geeksforgeeks.org", stackoverflow]
__license__ = "GPL"
__version__ = "0.1"
__maintainer__ = "Ishan Aryendu"
__email__ = "iaryendu@stevens.edu"
__status__ = "Development"
__packages__ = ['unittest', 'HW03_Ishan_Aryendu_wordle', 'HW03_Ishan_Aryendu_ui']
"""

import unittest
import HW03_Ishan_Aryendu_wordle as wordle
import HW03_Ishan_Aryendu_ui as ui
import HW03_Ishan_Aryendu_dictionary as dictionary
import count_occurrence_stats as stat


class TestFileReader(unittest.TestCase):
    def test_with_invalid_file_path(self):
        WORD_LENGTH = 5
        FILE_PATH = 'word_list'
        d = dictionary.Dictionary()
        self.assertEqual(list(d.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH)), [])

    def test_with_valid_file_path(self):
        WORD_LENGTH = 5
        FILE_PATH = 'resource/word_list'
        d = dictionary.Dictionary()
        self.assertNotEqual(list(d.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH)), [])


class TestUI(unittest.TestCase):
    def test_with_match_words(self):
        """Test valid valid input length of string"""
        u = ui.UI()
        self.assertTrue(u.match_words("Tests", "Tests", 1, 1))

    def test_with_unmatch_words(self):
        """Test valid invalid input length of string"""
        u = ui.UI()
        self.assertFalse(u.match_words("Test", "Tests", 1, 1))

    def test_with_word_not_in_list(self):
        """Test if there is a string is in the input list"""
        u = ui.UI()
        self.assertEqual(u.not_in_list(), '')

    def test_with_previously_untried(self):
        """Test a string that hasn't been tried before"""
        u = ui.UI()
        self.assertFalse(u.previously_tried("tests", ["hello", "sonar"]))

    def test_with_previously_tried(self):
        """Test a string that has been tried before"""
        u = ui.UI()
        self.assertTrue(u.previously_tried("hello", ["hello", "sonar"]))

    def test_case_game_over(self):
        u = ui.UI()
        var_0 = u.game_over()
        self.assertEqual(var_0, None)

    def test_with_creating_char_dict(self):
        """Test if a value is being converted into a valid dictionary"""
        str_0 = '*8Y6Lk)H\rwhrk2;'
        u = ui.UI()
        self.assertEqual(u.create_char_dict(str_0), {'*': 1, '8': 1, 'Y': 1, '6': 1, 'L': 1, 'k': 2, ')': 1, 'H': 1, '\r': 1, 'w': 1, 'h': 1, 'r': 1, '2': 1, ';': 1})


class TestWordle(unittest.TestCase):
    def test_with_valid_input(self):
        """Test valid input"""
        u = ui.UI()
        self.assertTrue(u.valid_input("Hello", 5))

    def test_with_invalid_input_no(self):
        """Test valid invalid input number"""
        u = ui.UI()
        with self.assertRaises(TypeError):
            u.valid_input(123.45, 5)

    def test_with_invalid_input_list(self):
        """Test valid invalid input list"""
        u = ui.UI()
        with self.assertRaises(TypeError):
            u.valid_input([1, 2, 3, 4, 5], 5)

    def test_with_invalid_input_len(self):
        """Test valid invalid input length of string"""
        u = ui.UI()
        with self.assertRaises(ValueError):
            u.valid_input("Yellow", 5)

    def test_case_init(self):
        """Test if the main function runs without failures"""
        u = ui.UI()
        try:
            u.play()
        except BaseException:
            pass

    def test_log_gameplay(self):
        w = wordle.Wordle()
        try:
            w.log_gameplay("log/logs.txt", "tests", "input_word", 1, 1, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})
        except Exception:
            pass


class TestCountOccurStat(unittest.TestCase):
    def test_case_0(self):
        stats_0 = stat.Stats()
        if stats_0.FILE_PATH is not None:
            raise AssertionError
        if stats_0.words != []:
            raise AssertionError
        if stats_0.no_of_words != 0:
            raise AssertionError
        if stats_0.test_list != []:
            raise AssertionError

    def test_case_1(self):
        stats_0 = stat.Stats()
        if stats_0.FILE_PATH is not None:
            raise AssertionError
        if stats_0.words != []:
            raise AssertionError
        if stats_0.no_of_words != 0:
            raise AssertionError
        if stats_0.test_list != []:
            raise AssertionError
        var_0 = stats_0.__str__()
        if var_0 != 'None: Counting game statistics...':
            raise AssertionError

    def test_case_2(self):
        try:
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            stats_1 = stat.Stats()
            if stats_1.FILE_PATH is not None:
                raise AssertionError
            if stats_1.words != []:
                raise AssertionError
            if stats_1.no_of_words != 0:
                raise AssertionError
            if stats_1.test_list != []:
                raise AssertionError
            str_0 = '5iH#dpM*oX"xN<7VU<es'
            var_0 = stats_1.set_file_path(str_0)
            if stats_1.FILE_PATH != '5iH#dpM*oX"xN<7VU<es':
                raise AssertionError
            dict_0 = {stats_1: stats_0}
            object_0 = stats_0.covert_to_tuple(dict_0)
        except BaseException:
            pass

    def test_case_3(self):
        try:
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            var_0 = stats_0.get_file_path()
            stats_1 = stat.Stats()
            if stats_1.FILE_PATH is not None:
                raise AssertionError
            if stats_1.words != []:
                raise AssertionError
            if stats_1.no_of_words != 0:
                raise AssertionError
            if stats_1.test_list != []:
                raise AssertionError
            list_0 = [var_0, var_0, stats_1]
            int_0 = 1144
            dict_0 = stats_0.make_list_count_dict(list_0, int_0)
        except BaseException:
            pass

    def test_case_4(self):
        try:
            dict_0 = None
            list_0 = [dict_0, dict_0, dict_0, dict_0]
            int_0 = 1649
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            tuple_0 = stats_0.convert(list_0)
            dict_1 = stats_0.make_list_count_dict(list_0, int_0)
        except BaseException:
            pass

    def test_case_5(self):
        try:
            list_0 = []
            list_1 = [list_0, list_0, list_0, list_0]
            list_2 = [list_0, list_0, list_0, list_1]
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            object_0 = stats_0.calculate_stats(list_2)
        except BaseException:
            pass

    def test_case_6(self):
        try:
            str_0 = 'q0#9J`JGEg.n_q'
            list_0 = [str_0]
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            object_0 = stats_0.calculate_stats(list_0)
        except BaseException:
            pass

    def test_case_7(self):
        try:
            str_0 = "?V'i]{-hbG"
            list_0 = [str_0, str_0, str_0, str_0]
            list_1 = [list_0, list_0, str_0, str_0]
            int_0 = -1002
            stats_0 = stat.Stats()
            if stats_0.FILE_PATH is not None:
                raise AssertionError
            if stats_0.words != []:
                raise AssertionError
            if stats_0.no_of_words != 0:
                raise AssertionError
            if stats_0.test_list != []:
                raise AssertionError
            dict_0 = stats_0.make_list_count_dict(list_1, int_0)
        except BaseException:
            pass
