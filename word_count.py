# Dummy Program just for Testing GitHub

print "Enter a statement to word count: "
happy = input()

words = happy.split()

counts = {}
for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)
