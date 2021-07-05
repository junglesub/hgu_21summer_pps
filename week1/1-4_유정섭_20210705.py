result = []
for i in range(int(input())):
    sc = [int(x) for x in input().split()[1:]]
    result.append(
        len(list(filter(lambda x: x > sum(sc) / len(sc), sc))) / float(len(sc)))

for avg in result:
    print(f"{format(avg * 100, '.3f')}%")
