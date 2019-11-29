from classes import Word, Sentence

words = [Word("собака", "сущ"),
         Word("ела", "глагол"),
         Word("колбасу", "сущ"),
         Word("вечером", "наречие")]

sentence = Sentence(words)

print(sentence.show())
print(sentence.show_parts())

