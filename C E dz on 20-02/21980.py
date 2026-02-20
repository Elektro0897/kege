def is_prime(num):
    if num < 2: return False
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            return False
    return True


def f(num):
    d = set()
    for i in range(2, int(num ** .5) + 1):
        if num % i == 0:
            if i % 10 == 7 and is_prime(i): d |= {i}
            if num // i % 10 == 7 and is_prime(num // i): d |= {num // i}
    if d:
        return sum(d) // len(d)
    return 0

k = 0
for n in range(750000, 0, -1):
    m = f(n)
    if m and m % 111 == 0:
        print(n, m)
        k += 1
        if k == 5:
            break