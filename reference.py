class Ref():
    pattern: str
    given_word: str
    def __init__(self):
        self.pattern = ""
        self.given_word = ""


    def set_pattern(self, pattern):
        self.pattern = pattern

    def set_given_word(self, given_word):
        self.given_word = given_word

    def get_pattern(self):
        return self.pattern

    def get_given_word(self):
        return self.given_word
