from classes import Sentence, Noun, Verb, Word

words = []
words.append(Noun("собака"))
words.append(Verb("ела"))
words.append(Noun("колбасу"))
words.append(Noun("кот"))

sentence = Sentence(words)

print(sentence.show())
print(sentence.show_parts())