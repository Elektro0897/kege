with open(r'./files/17628.txt') as file:
    data = [list(map(int, i.split())) for i in file]
k = 0
for line in data:
    if max(line) + min(line) <= sum(line) - max(line) - min(line):
        k += 1
print(k)