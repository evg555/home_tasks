class Word:
    text = ''

    def __init__(self, text):
        self.text = text

class Sentence:
    content = []

    def __init__(self, content):
        self.content = content

    def show(self):
        words = []
        for i in self.content:
            words.append(i.text)
        return ' '.join(words)

    def show_parts(self):
        parts = []
        for i in self.content:
            if i.part() not in parts:
                parts.append(i.part())
        return ' '.join(parts)

class Noun(Word):
    __grammar = 'сущ'

    def __init__(self, text):
        self.text = text

    def part(self):
        return self.__grammar

class Verb(Word):
    __grammar = 'гл'

    def __init__(self, text):
        self.text = text

    def part(self):
        return self.__grammar