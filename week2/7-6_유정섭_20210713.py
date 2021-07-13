import functools

def compare(a, b):
  if a[0] != b[0]: return a[0] - b[0]
  else:
    return a[1] - b[1]

n = int(input())
coords = []
for i in range(n):
  coords.append(list(map(int, input().split())))
for c in sorted(coords, key=functools.cmp_to_key(compare)):
  print(" ".join(map(str, c)))