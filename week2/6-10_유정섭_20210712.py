from itertools import combinations_with_replacement
word = input()
print(len(set(map(lambda x: word[x[0]:x[1] + 1],list(combinations_with_replacement(range(len(word)), 2))))))