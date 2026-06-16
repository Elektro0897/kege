from math import dist

with open(r'./files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if 'VIII' in info or 'IX' in info:
            stars.append([float(x), float(y)])

stars_1 = [d for d in stars if d[1] < 15]
stars_2 = [d for d in stars if 15 < d[1] < 22]
stars_3 = [d for d in stars if d[1] > 22]

b1 = []
for s1 in stars_1:
    for s2 in stars_2:
            b1.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_3:
            b1.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_1:
            b1.append(dist(s1, s2))

b2 = []
for s1 in stars_1:
    for s2 in stars_1:
        if s1 != s2:
            b2.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_2:
        if s1 != s2:
            b2.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_3:
        if s1 != s2:
            b2.append(dist(s1, s2))
print(min(b1) * 10000, sum(b2) / len(b2) * 10000)