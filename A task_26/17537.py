with open(r'./files/26_17537.txt') as file:
    n, m, k = map(int, file.readline().split())
    seats = [m] * (k + 1)
    for i in file:
        row, seat = map(int, i.split())
        seats[seat] = min(seats[seat], row -  1)

ans = []
for seat in range(1, k + 1 - 1):
    row_1, row_2 = seats[seat:seat + 2]
    ans.append([min(row_1, row_2), seat + 1])
print(*max(ans))