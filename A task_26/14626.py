with open(r'./files/26_14626.txt') as file:
    n = int(file.readline())
    k, m = map(int, file.readline().split())
    caves = dict()
    for id in sorted(map(int, file.readline().split())):
        caves[id] = m
    weights = sorted(int(i) for i in file)

ans = []
ans2 = 0
for id in caves:
    cave = caves[id]
    len_weights = len(weights)
    for maximum, minimum in list(zip(weights[::-1], weights))[:len(weights) // 2]:
        if cave >= maximum:
            cave -= maximum
            weights.remove(maximum)
        else:
            break
        if cave >= maximum:
            cave -= maximum
            weights.remove(minimum)
    else:
        if len_weights % 2 != 0:
            len_weights = len(weights)
            if weights[len_weights // 2] <= cave:
                cave -= weights[len_weights // 2]
                weights.remove(weights[len_weights // 2])
    ans.append([cave, id])
    if cave != m:
        ans2 += cave

print(min(ans, key=lambda x: (x[0], x[-1]))[1])
print(ans2)