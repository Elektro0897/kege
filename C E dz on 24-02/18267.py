# частный случай
def f(s, e):
    if s == e: return 1
    if s > e: return 0
    if s == 6:
        return f(s + 2, e) + f(s + 5, e)
    return f(s + 2, e) + f(s + 5, e) + f(s ** 2, e)

print(f(4, 36))

######################################################
# общий случай
def f(s, e, l):
    if s == e and l != 'c': return 1
    if s > e: return 0
    return f(s + 2, e, 'a') + f(s + 5, e, 'b') + f(s ** 2, e, 'c')

print(f(4, 36, ''))