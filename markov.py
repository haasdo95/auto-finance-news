import jieba
import random

class Markov(object):
    def __init__(self, file):
        self.cache = {}
        self.file_to_read = file
        self.word_list = self.pre_proc() # separate text file into words
        print len(self.word_list)
        self.build() # fill cache with word tuples

    def pre_proc(self):
        newsFile = open(self.file_to_read)
        news = newsFile.read()
        return jieba.lcut(news)

    def build(self):
        list_len = len(self.word_list)
        for i in range(list_len - 2):
            key = (self.word_list[i], self.word_list[i+1])
            if key in self.cache:
                self.cache[key].append(self.word_list[i+2])
            else:
                self.cache[key] = [self.word_list[i+2]]

    def generateRandomNews(self, size):
        randomStart = random.randint(0, len(self.word_list) - 3)
        start1, start2 = self.word_list[randomStart], self.word_list[randomStart+1]
        runner1, runner2 = start1, start2
        generated_text = []
        for i in range(size):
            generated_text.append(runner1)
            key = (runner1, runner2)
            runner1 = runner2
            runner2 = random.choice(self.cache[key])
        generated_text.append(runner2)
        return "".join(generated_text)

markov = Markov("news_lib.txt")
print markov.generateRandomNews(100)
