#!/usr/bin/env python
import sys, string

data = []
words = []
word_freqs = []

def read_file(path_to_file):
    global data
    with open(path_to_file) as f:
        data = data + list(f.read())
        print("data_read_file:", data)

def filter_chars_and_normallize():
    global data
    for i in range(len(data)):
        if not data[i].isalnum:
            data[i] = ' '
            print("data_filter", data[i])
        else:
            data[i] = data[i].lower()
            print("data_filter", data[i])

def scan():
    global data
    global words
    data_str = ''.join(data)
    print("data_str:", data_str)
    words = words + data_str.split()
    print("words", words)

def remove_stop_words():
    global words
    with open('../stop_words.txt') as f:
        stop_words = f.read().split(',')
    stop_words.extend(list(string.ascii_lowercase))
    indexes = []
    for i in range(len(words)):
        if words[i] in stop_words:
            indexes.append(i)
    for i in reversed(indexes):
        words.pop(i)

def frequencies():
    global words
    global word_freqs
    for w in words:
        keys = [wd[0] for wd in word_freqs]
        if w in keys:
            word_freqs[keys.index(w)][1] += 1
        else:
            word_freqs.append([w, 1])

def sort():
    global word_freqs
    word_freqs.sort(key=lambda x: x[1], reverse=True)

read_file(sys.argv[1])
filter_chars_and_normallize()
scan()
remove_stop_words()
frequencies()
sort()

for tf in word_freqs[0:25]:
    print(tf[0], '-', tf[1])
