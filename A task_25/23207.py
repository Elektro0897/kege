def prost(num):
    if num < 2: return False
    for i in range(2, int(num**.5)):
        if num % i == 0:
            return False
    return True

def f(num):
    d = []
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            if prost(i) and str(i).count('5') == 1: d += [i]
            if prost(num // i) and str(num // i).count('5') == 1: d += [num // i]
    if len(d) == 2 and d[0] * d[1] == num:
        return max(d)
    return 0

k = 0
for n in range(1324727 + 1, 10**20):
    if m := f(n):
        print(n, m)
        k += 1
        if k == 5:
            break

# 1324795 264959
# 1324801 1151
# 1324903 2543
# 1325015 265003
# 1325029 5279
