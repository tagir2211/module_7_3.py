class WordsFinder:
    '''
    Напишите класс WordsFinder, объекты которого создаются следующим образом:
    WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
    Объект этого класса должен принимать при создании неограниченного количество названий файлов
    и записывать их в атрибут file_names в виде списка или кортежа.
    '''

    def __init__(self, *args):
        self.file_names = []
        for i in args:
            self.file_names.append(i)

    def del_punctuation(self, line):
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ', '...']
        str_without_punct = ''
        for j in range(len(punctuation)):
            line = line.replace(punctuation[j], '')
        str_without_punct += line

        return str_without_punct

    def get_all_words(self):
        self.all_words = {}
        self.values = []
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                text = file.read()
                self.values.append(self.del_punctuation(text.lower()).split())
        self.all_words = dict(zip(self.file_names, self.values))
        return self.all_words

    def find(self, word):
        result = {}
        index_word = 0
        for name in self.file_names:
            for words in self.all_words[name]:
                if words == word.lower():
                    index_word = self.all_words[name].index(words) + 1
                    result = {name: index_word}
        if index_word == 0:
            return f'{word} не найдено'
        else:
            return result

    def count(self, word_c):
        result = {}
        index_count = 0
        for name in self.file_names:
            for words in self.all_words[name]:
                if words == word_c.lower():
                    index_count += 1
        result = {name: index_count}
        return result


f = WordsFinder('test_file.txt')
print(f.get_all_words())
print(f.find("for"))
print(f.count('TeXt'))
