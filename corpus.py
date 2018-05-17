# importing necessary libraries
import pickle
import time
import string
import re
from collections import Counter

# singleton class


class Corpus(object):
    def __init__(self, characters):
        self.characters = characters

    def unigrams(self, characters):
        return dict(Counter(list(characters)))

    def bigrams(self, c):
        return {k: c.count(k) for k in {c[i]+c[i+1] for i in range(len(c)-1)}}

letters = list(string.ascii_letters)

# processingtime
start_time = time.perf_counter()
cpu_start_time = time.process_time()
print("start at elapsed time ", str(start_time).rjust(20),
      ", cpu time ", str(cpu_start_time).rjust(10))

# file processing and cleaning
f = open('/home/turing/t90rkf1/dnl/dhw/data/app88.txt').readlines()
f = list(map(lambda x: re.sub('AP[0-9]{6}-[0-9]{4}', '', x), f))
f = list(map(str.lower, f))
f = list(map(lambda x: ''.join([y.replace(y, ' ')
             if y not in letters else y for y in x]), f))
words = list(filter(None, [word for line in f for word in line.split(" ")]))

words = list(map(lambda x: re.sub('^[a-z]*', '<' + x + '>', x), words))
characters = ' '.join(words)

# creating required data structures for the corpus
w_object = Corpus(characters)
list_unigrams = sorted((w_object.unigrams(characters)).items(),
                       key=lambda x: x[0])
list_bigrams = sorted((w_object.bigrams(characters)).items(),
                      key=lambda x: x[0])

my_data = [list_unigrams, list_bigrams, dict(Counter(list(words))),
           len(words), len(set(words))]

# pickiling the data
my_file = open("pickled_data.dat", 'wb')
pickle.dump(my_data, my_file)

end_time = time.perf_counter()
cpu_end_time = time.process_time()
print("finish reading at elapsed time ", str(end_time).rjust(20),
      ", cpu time ", str(cpu_end_time).rjust(10))

print("total elapsed time ", str(end_time - start_time).rjust(20),
      ", cpu time ", str(cpu_end_time - cpu_start_time).rjust(20))

# printing the corpus metric for error checking
print("\nNo of words:  ", len(words))
print("Number of types (distinct words):  ", len(set(words)))

print('\nUnigram counts:')
for a, b in list_unigrams[1:]:
    print(str(a).ljust(8), str(b).rjust(8))

print('\nBigram counts:')
for a, b in list_bigrams:
    print(str(a).ljust(8), str(b).rjust(8))
