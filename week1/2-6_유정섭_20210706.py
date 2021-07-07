n = int(input())
cnt = 0
for i in range(n):
  appeared = []
  word = input()
  for i, c in enumerate(word):
    s = True
    if i == 0:
      appeared.append(c)
      continue
    if word[i - 1] != c:
      # 다른 단어인데
        if c in appeared:
          # 이미 등장한 단어면 그대로 끝나며 실패.
          cnt -= 1
          break
        appeared.append(c) # 아니면 추가.
  cnt += 1
print(cnt)