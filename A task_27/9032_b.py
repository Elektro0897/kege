from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_B_9032.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if info[:2] == 'L3':
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] < 15]
cluster_2 = [d for d in dots if 15 < d[1] < 22]
cluster_3 = [d for d in dots if d[1] > 22]

stars_1 = [d for d in stars if d[1] < 15]
stars_2 = [d for d in stars if 15 < d[1] < 22]
stars_3 = [d for d in stars if d[1] > 22]

center_1 = center(cluster_1)
center_2 = center(cluster_2)
center_3 = center(cluster_3)

b = []
for s1 in stars_1:
    for s2 in stars_2:
            b.append(dist(s1, s2))
for s1 in stars_2:
    for s2 in stars_3:
            b.append(dist(s1, s2))
for s1 in stars_3:
    for s2 in stars_1:
            b.append(dist(s1, s2))
print(dist(center_3, center_1) * 10000, max(b) * 10000)