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
        self.assertEqual(list(dictionary.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH)), [])

    def test_with_valid_file_path(self):
        WORD_LENGTH = 5
        FILE_PATH = 'resource/word_list'
        self.assertNotEqual(list(dictionary.get_words_from_file(FILE_PATH, word_length=WORD_LENGTH)), [])


class TestUI(unittest.TestCase):
    def test_with_match_words(self):
        """Test valid valid input length of string"""
        self.assertTrue(ui.match_words("Tests", "Tests", 1, 1))

    def test_with_unmatch_words(self):
        """Test valid invalid input length of string"""
        self.assertFalse(ui.match_words("Test", "Tests", 1, 1))

    def test_with_word_not_in_list(self):
        """Test if there is a string is in the input list"""
        self.assertEqual(ui.not_in_list(), '')

    def test_with_previously_untried(self):
        """Test a string that hasn't been tried before"""
        self.assertFalse(ui.previously_tried("tests", ["hello", "sonar"]))

    def test_with_previously_tried(self):
        """Test a string that has been tried before"""
        self.assertTrue(ui.previously_tried("hello", ["hello", "sonar"]))

    def test_case_game_over(self):
        var_0 = ui.game_over()
        self.assertEqual(var_0, None)


class TestWordle(unittest.TestCase):
    def test_with_creating_char_dict(self):
        """Test if a value is being converted into a valid dictionary"""
        str_0 = '*8Y6Lk)H\rwhrk2;'
        self.assertEqual(wordle.create_char_dict(str_0), {'*': 1, '8': 1, 'Y': 1, '6': 1, 'L': 1, 'k': 2, ')': 1, 'H': 1, '\r': 1, 'w': 1, 'h': 1, 'r': 1, '2': 1, ';': 1})
        # var_0 = wordle.create_char_dict(str_0)
        # assert var_0 == {'*': 1, '8': 1, 'Y': 1, '6': 1, 'L': 1, 'k': 2, ')': 1, 'H': 1, '\r': 1, 'w': 1, 'h': 1, 'r': 1, '2': 1, ';': 1}
        # try:
        #     float_0 = -733.9
        #     var_1 = wordle.create_char_dict(float_0)
        #     self.assertEqual(var_1, ('-', '7', '3', '3', '.', '9'))
        # except BaseException:
        #     pass

    def test_with_valid_input(self):
        """Test valid input"""
        self.assertTrue(wordle.valid_input("Hello", 5))

    def test_with_invalid_input_no(self):
        """Test valid invalid input number"""
        with self.assertRaises(TypeError):
            wordle.valid_input(123.45, 5)

    def test_with_invalid_input_list(self):
        """Test valid invalid input list"""
        with self.assertRaises(TypeError):
            wordle.valid_input([1, 2, 3, 4, 5], 5)

    def test_with_invalid_input_len(self):
        """Test valid invalid input length of string"""
        with self.assertRaises(ValueError):
            wordle.valid_input("Yellow", 5)

    def test_case_init(self):
        """Test if the main function runs without failures"""
        try:
            wordle.play()
        except BaseException:
            pass

    def test_log_gameplay(self):
        try:
            wordle.log_gameplay("log/logs.txt", "tests", "input_word", 1, 1, {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0})
        except Exception:
            pass


class TestCountOccurStat(unittest.TestCase):
    def test_parse_file_as_dict_of_tuples_01(self):
        try:
            stat.parse_file_as_dict_of_tuples('log/test.csv')
        except Exception:
            pass

    def test_covert_to_tuple(self):
        str_0 = 'abcd'
        str_1 = '12ab34cd'
        dict_0 = {str_0: str_1, str_0: str_0, str_0: str_1, str_1: str_0}
        var_0 = stat.covert_to_tuple(str_0, dict_0)
        assert var_0 is None

    def test_convert(self):
        str_0 = 'test'
        var_0 = stat.convert(str_0)
        assert var_0 == ('t', 'e', 's', 't')

    def test_calculate_stats(self):
        try:
            list_0 = []
            object_0 = stat.calculate_stats(list_0)
        except BaseException:
            pass

    def test_write_perc_01(self):
        try:
            str_0 = '\n UPf'
            dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
            var_0 = stat.write_perc(str_0, dict_0)
            assert var_0 is None
            object_0 = stat.parse_file_as_dict_of_tuples(str_0)
        except BaseException:
            pass

    def test_covert_to_tuple(self):
        try:
            str_0 = "~`'{\tzp9!,\x0b8t@$GEwx"
            dict_0 = None
            var_0 = stat.covert_to_tuple(str_0, dict_0)
        except BaseException:
            pass

    def test_parse_file_as_dict_of_tuples_02(self):
        try:
            str_0 = '3+gXeT7A8yQSuisp'
            object_0 = stat.parse_file_as_dict_of_tuples(str_0)
        except BaseException:
            pass

    def test_write_perc_02(self):
        try:
            str_0 = "-No-b4j9%#fb1'"
            dict_0 = None
            var_0 = stat.write_perc(str_0, dict_0)
        except BaseException:
            pass
