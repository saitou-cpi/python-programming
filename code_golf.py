#!/usr/bin/env python
import re, sys, collections

stops = open('../stop_words.txt').read().split(',')
words = re.findall(r'[a-z]{2,}', open(sys.argv[1]).read().lower())
print("words:", words)
counts = collections.Counter(w for w in words if w not in stops)
print("counts", counts)
for (w, c) in counts.most_common(25):
    print(w, '-', c)
