def customMax(l):
  result = (-1, -1)
  for i in range(len(l)):
    if result[1] < int(l[i]):
      result = (i, int(l[i]))
  return result

def solution(number, k):
    # Base case
    if len(number) - 1 == k:
      return max([int(x) for x in number])
    answer = ''
    while len(number):
      if k == 0:
        answer += number
        break

      sub = number[:k + 1]
      # max_n = max(list(sub)) # not optimized.
      # max_i = sub.find(max_n)
      max_i, max_n = customMax(list(sub))

      # Post Effect
      number = number[max_i+1:]
      k -= max_i
      answer += str(max_n)
    return answer

# TC
t1 = solution("1924", 2)
print(t1)
t1 = solution("1231234", 3)
print(t1)
t1 = solution("4177252841", 4)
print(t1)
t1 = solution("12312345231234", 12)
print(t1, len("12312341231234"))