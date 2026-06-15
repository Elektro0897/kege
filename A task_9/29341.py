with open(r'./files/29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]
k = 0
for line in data:
    if max(line) < sum(line) - max(line):
        if not (line[0] + line[1] == line[2] + line[3]):
            if not (line[0] + line[2] == line[1] + line[3]):
                if not (line[0] + line[3] == line[2] + line[1]):
                    k += 1
print(k)