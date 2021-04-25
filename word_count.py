#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dummy Program Just for Testing GitHub

happy = input("Enter a statement to word count: ")    # Read intput from user an store it in happy

words = happy.split()     # Split input words and save them in words

counts = {}               #  initialize counts
for word in words:        #  over all items in words
    counts[word] = counts.get(word, 0) + 1      # increase number of occurrance

print("The word frequency of your statement is: " + str(counts))     # print result




