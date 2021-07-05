def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        s_lv = -1
        doable = True
        for c in st:
            if c not in skill:
                continue
            if skill.index(c) - 1 > s_lv:
                doable = False
                break
            else:
                s_lv = skill.index(c)
        if doable:
            answer += 1
    return answer


# Test Case
s = solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])
if s == 2:
    print("Passing", s)
else:
    print("Failed", s)
