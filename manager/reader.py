class Reader:
    def __init__(self, list):
        self.__list = list
        self.__idx = 0

    def end(self):
        return len(self.__list) <= (self.__idx)

    def next(self):
        self.__idx += 1

    def prev(self):
        self.__idx -= 1

    def get(self):
        return self.__list[self.__idx]
