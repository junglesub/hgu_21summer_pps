# 참고 자료 - https://velog.io/@soo5717/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%81%B0-%EC%88%98-%EB%A7%8C%EB%93%A4%EA%B8%B0-%ED%8C%8C%EC%9D%B4%EC%8D%AC

def solution(number, k):
    answer = ''
    stack = []

    for digit in number:
      while stack and stack[-1] < digit and k > 0:
        k-=1
        stack.pop()
      stack.append(digit)
    return ''.join(stack[:len(stack) - k])

# TC
t1 = solution("1924", 2)
print(t1)
t1 = solution("1231234", 3)
print(t1)
t1 = solution("4177252841", 4)
print(t1)
t1 = solution("1000", 3)
print(t1)
# t1 = solution(("8"*30000000) + "3", 30000000)
# print(t1)