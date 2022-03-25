from wordleSolver import Solve
import string


class Help():
    def get_match_char_list(self, file_path):
        _file = open(file_path, 'r')
        counter = 5
        res_string = ''
        for line in _file.readlines():
            res_string += line[0]
            counter -= 1
            if not counter:
                break
            # print(line[0])
        return res_string

    def help_me(self):
        flag = False
        match_file_path = 'log/letterFrequency.csv'
        match = self.get_match_char_list(match_file_path)
        print("Starting helper module...")
        match = input("Enter the matching letters (or press enter to skip): ")
        mismatch = input("Enter the non-matching letters (or press enter to skip): ")
        pattern = input("Enter the pattern of letters in the word (or press enter to skip): ")
        if not mismatch:
            mismatch = '?'
        if not pattern:
            pattern = '?'
        if not match:
            flag = True
            match = self.get_match_char_list(match_file_path)
        allowed = set(string.ascii_lowercase + '?')
        # if not set(sys.argv[1] + sys.argv[2]) <= allowed:
        if not set(match + mismatch) <= allowed:
            print(
                "The first and second arguments should either be lowercase letters, or a single question mark (?) as a "
                "placeholder")
            match = self.get_match_char_list(match_file_path)
        return flag, match, mismatch, pattern


if __name__ == '__main__':
    h = Help()
    s = Solve()
    flag, match, mismatch, pattern = h.help_me()
    # print(flag, " ", match, " ", mismatch, " ", pattern)
    llist = s.solve(flag, match, mismatch, pattern)
    llist.listprint()