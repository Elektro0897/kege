with open(r'./files/17522.txt') as file:
    data = [list(map(int, i.split())) for i in file]
k = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    lines = []
    if sorted(amount) == [1, 1, 2]:
        lines += [i for i in line]
        if max(lines) < sum(lines) - max(lines):
            k += 1
print(k)