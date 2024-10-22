class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for file in self.file_names:
            with open(file, 'r', encoding='utf-8') as f:
                words = f.read().lower().split()
                words = [words.strip('.,!?;:= - ') for words in words]
                all_words[file] = words
        return all_words

    def find(self, word):
        dict_ = self.get_all_words()
        result = {}
        for file, words in dict_.items():
            if word.lower() in [w.lower() for w in words]:
                result[file] = words.index(next(w for w in words if w.lower() == word.lower())) + 1
        return result

    def count(self, word):
        dict_ = self.get_all_words()
        result = {}
        for file, words in dict_.items():
            result[file] = sum(1 for w in words if w.lower() == word.lower())
        return result


# finder2 = WordsFinder('test_file.txt')
# print(finder2.get_all_words()) # Все слова
# print(finder2.find('TEXT')) # 3 слово по счёту
# print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder1.get_all_words())
print(finder1.find('captain'))
print(finder1.count('captain'))

# finder1 = WordsFinder('Rudyard Kipling - If.txt',)
#
# print(finder1.get_all_words())
# print(finder1.find('if'))
# print(finder1.count('if'))

# finder1 = WordsFinder('Mother Goose - Monday’s Child.txt',)
# print(finder1.get_all_words())
# print(finder1.find('Child'))
# print(finder1.count('Child'))
