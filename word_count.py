#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Dummy Program Just for Testing GitHub

happy = input("Enter a statement to word count: ")

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print("The word frequency of your statement is: " + str(counts))



