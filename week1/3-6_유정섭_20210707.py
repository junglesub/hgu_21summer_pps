tc = int(input())
answer = []
for t in range(tc):
  input()
  odd = {}
  for x in input().split():
    try:
      if odd[x] == True:
        del odd[x]
    except KeyError:
      odd[x] = True
      pass
  result = 0
  for x in odd.keys():
    result = result ^ int(x)
  answer.append(result)

# 출력
for i, ans in enumerate(answer):
  print(f"Case #{i+1}")
  print(answer[i])