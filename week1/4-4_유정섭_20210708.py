save = {}

def useSave(k, n):
  try: return save[(k, n)]
  except KeyError:
    save[(k, n)] = getPeople(k, n)
    return save[(k, n)]

def getPeople(k, n):
  if n == 1:
    return 1
  if n == 2:
    return k + 2
  if k == 0:
    return n
  return sum([useSave(k - 1, i) for i in range(1, n + 1)])

res = []
tc = int(input())
for i in range(tc):
  k, n = [int(input()) for _ in range(2)]
  res.append(getPeople(k, n))

for r in res: print(r)