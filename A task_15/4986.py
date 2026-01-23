def f(x):
    return (x % a == 0) or ((x % 23 == 0) <= (x not in range(50, 71)))

for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
        #69