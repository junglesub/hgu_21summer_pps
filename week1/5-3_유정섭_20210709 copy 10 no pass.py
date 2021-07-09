def solution(number, k):
    answer = ''
    while len(number):
      print(">", k)
      # If later digit doesn't matter
      if len(number) <= k:
        break

      # always add 9
      if number[0] == '9':
        print("9 OR")
        answer += '9'
        number = number[1:]
        continue

      # no more k left
      if k == 0:
        answer += number
        break

      sub = number[:k + 1]
      # max_i, max_n = max(enumerate(sub), key=lambda p: p[1]) # not optimized.
      max_n = max(list(sub))
      max_i = sub.find(max_n)

      # Post Effect
      if len(number) == max_i :
        break
      number = number[max_i+1:]
      k -= max_i
      answer += max_n
    return answer

# TC
t1 = solution("1924", 2)
print(t1)
t1 = solution("1231234", 3)
print(t1)
t1 = solution("4177252841", 4)
print(t1)
t1 = solution("1000", 3)
print(t1)
t1 = solution(("8"*30000000) + "3", 30000000)
print(t1)