def prost(num):
    if num < 2: return False
    for i in range(2, int(num**.5)):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            if prost(i): d |= {i}
            if prost(num // i): d |= {num // i}
    if len(d) > 1:
        m = min(d) + max(d)
        if m > 60000 and str(m) == str(m)[::-1]:
            return m
    return 0

k = 0
for n in range(5400001, 10**20):
    if m := f(n):
        print(n, m)
        k += 1
        if k == 5:
            break

# 5400042 900009
# 5400420 90009
# 5400866 158851
# 5406116 1351531
# 5406420 90109