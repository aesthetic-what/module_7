class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, encoding='utf8') as file:
                self.list_words = file.read().lower().split()
                all_words = {self.file_names[0]: self.list_words}
            return all_words

    def find(self, word):
        find_word = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf8'):
                word = word.lower()
                if word in self.list_words:
                    find_word[file_name] = self.list_words.index(word) + 1
        return find_word

    def count(self, word):
        count_dict = {}
        for file_name in self.file_names:
            with open(file_name, encoding='utf8'):
                word = word.lower()
                for name, words in self.get_all_words().items():
                    count_dict[file_name] = words.count(word)
                return count_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
