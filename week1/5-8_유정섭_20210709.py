def divisor(n):
  result = set()
  for i in range(1, int(n/2 + 1) + 1):
    if n % i == 0:
      result.add(i)
      result.add(n/i)
  return result

def solution(left, right):
    answer = 0
    for n in range(left, right + 1) :
      answer += (n if len(divisor(n)) % 2 == 0 else -n)
    return answer

# TC
print(solution(13, 17))
print(solution(24, 27))