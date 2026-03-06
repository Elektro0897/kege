def dig(x, y):
    if str(x)[0] == str(y)[0]: return True
    return False
def f(x):
    return ((not dig(x, 28)) and dig(x, 47)) <= (x > a - 20)
ans = []
for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break
#23