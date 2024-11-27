class Info:
    # use this if need parameter in class
    def __init__(self, name):
        self.name = name

    def infofunc(self):
        print(self.name)

inf = Info('Hamja')
inf.infofunc()
