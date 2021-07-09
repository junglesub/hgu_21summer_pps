ans = []
for _ in range(int(input())):
  word = input()
  a = word.count('a')
  b = word.count('b')
  c = word.count('c')
  ans.append(len(set([a, b, c])) < 3)

for i, a in enumerate(ans):
  #1 YES
  print(f"#{i + 1} {'YES' if a else 'NO'}")