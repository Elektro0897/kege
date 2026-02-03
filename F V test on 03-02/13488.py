def f(num):
    d = set()
    for i in range(2, int(num**.5) + 1):
        if num % i == 0:
            if i % 2 != 0: d |= {i}
            if num // i % 2 != 0: d |= {num // i}

    if len(d) == 3:
        return sorted(d)
    return []

for n in range(18782, 18823):
    if m := f(n):
        print(*m)