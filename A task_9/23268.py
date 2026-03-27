with open(r'./files/23268.txt') as file:
    data = [list(map(int, i.split()))for i in file]
k = 0
for line in data:
    k += 1
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == [1, 1, 1, 2, 2]:
        pov = [i for i in line if line.count(i) != 1]
        ne_pov = [i for i in line if line.count(i) == 1]
        if sum(pov) / len(pov) < max(ne_pov):
            print(k)
            break