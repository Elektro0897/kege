def dig(x, y):
    if str(x)[-1] == str(y)[-1]: return True
    return False
def f(x):
    return ((not dig(x, 28)) and dig(x, 47)) <= (x > a - 20)
ans = []
for a in range(1, 1000)[::-1]:
    if all(f(x) for x in range(1, 1000)):
        print(a)
        break