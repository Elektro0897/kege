with open(r'./files/26_29234.txt') as file:
    k = int(file.readline())
    n = int(file.readline())
    times = [list(map(int, i.split())) for i in file]

times = sorted(times)
putters = [0] * k
profit = [0] * k
cnt = 0
for time in times:
    for i in range(k):
        if time[0] > putters[i]:
            putters[i] = time[1]
            cnt += 1
            t = time[1] - time[0]
            profit[i] += t * (t + 1) // 2
            break
print(cnt, max(profit))