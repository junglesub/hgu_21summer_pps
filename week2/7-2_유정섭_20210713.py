min, max = map(int, input().split())
wordlist = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
word = {}

for i in range(min, max+1):
  sp_out = ' '.join(map(lambda x: wordlist[x], map(int, str(i))))
  word[sp_out] = i
for i, x in enumerate(sorted(word.keys())):
  print(word[x], end="\n" if (i + 1) % 10 == 0 else " ")
