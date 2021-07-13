import functools

def compare(a, b):
  if len(a) != len(b): return len(a) - len(b)
  else:
    asum = sum(map(int, filter(lambda x: x.isnumeric(), a)))
    bsum = sum(map(int, filter(lambda x: x.isnumeric(), b)))
    if asum != bsum: return asum - bsum
    else: return -1 if a < b else 1

n = int(input())
words = []
for i in range(n):
  words.append(input())
print("\n".join(sorted(words, key=functools.cmp_to_key(compare))))