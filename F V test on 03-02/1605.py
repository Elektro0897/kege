ans = []
for n in range(1, 1000):
    r = bin(n + 2)[2:]
    r += str(sum(map(int, r)) % 2)
    r += str(sum(map(int, r)) % 2)
    r = int(r, 2)
    if r < 61:
        ans.append(n)
print(max(ans))
# ответ: 13