with open(r'files/24-371.txt') as file:
    data = file.readline()

data = data.replace('.', '.*')
data = data.split('*')[:-1]

ans = 0
for line in data:
    k_m = line.count('M')
    if k_m == 112:
        ans = max(ans, len(line))
    elif k_m > 112:
        while k_m > 112:
            if line[0] == 'M': k_m -= 1
            line = line[1:]
        ans = max(ans, len(line))
print(ans)