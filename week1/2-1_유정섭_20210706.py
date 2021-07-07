import re

def test(word):
  # 확인1: 모음이나 자음이 있는지 확인한다.
  if len(re.compile("[aeiou]").findall(word)) == 0:
    return False

  vow_cnt = 0
  cons_cnt = 0
  for i in range(len(word)):
    c = word[i]
    # 3. 같은 글자인지 확인
    if i>0 and word[i-1:i + 1] not in ['ee', 'oo'] and word[i-1] == word[i]:
      return False # 같은 글자 확인 False
    # 2. 모음 3개, 자음 3개인지 확인
    if c in "aeiou":
      vow_cnt += 1
      cons_cnt = 0
    else:
      cons_cnt += 1
      vow_cnt = 0
    if max((vow_cnt, cons_cnt)) >= 3: return False # 자음과 모음 둘중 1개가 이상이라면
  return True

result = {}

while True:
  word = input()
  if word == "end": break
  result[word] = test(word)

for word, b in result.items():
  if b:
    print(f"<{word}> is acceptable.")
  else:
    print(f"<{word}> is not acceptable.")
