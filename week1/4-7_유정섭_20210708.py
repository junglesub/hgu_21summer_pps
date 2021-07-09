def solution(x):
    answer = x % sum([int(c) for c in str(x)]) == 0
    return answer

# TC
print(solution(11))