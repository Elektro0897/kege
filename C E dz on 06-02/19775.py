def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            return False
    return True

def f(num):
    d = set()
    for i in range(2, int(num**.5)):
        if num % i == 0:
            if is_prime(i): d |= {i}
            if is_prime(num // i): d |= {num // i}

    s = sum(d)
    if s and s % 145 == 0:
        return s
    return 0

k = 0
for n in range(32500001, 10**20):
    if s := f(n):
        print(n, s)
        k += 1
        if k == 7:
            break