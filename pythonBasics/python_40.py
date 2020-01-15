class song(object):
    def __init__(self, a, b, c):
        self.a = c
        self.b = a
        self.c = b

    def sing_me_a_song(self):
        for line in self.a:
            print line
        for line in self.b:
            print line
        for line in self.c:
            print line

happy_bday = song(["happy bday to you",
                    "I don't want to get sued",
                    "so i'll stop righting there"],["abcbcb"], ["third line"])

bulls_on_parade = song(["They rally around tha family",
                        "With pockets full of shells"],["assdd"], ["third newlines"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()
