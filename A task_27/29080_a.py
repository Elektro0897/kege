from math import *
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'L' and data[1] == '3':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 8]
cluster_2 = [d for d in dots if d[1] < 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

a1 = []
for s in stars:
    if len(cluster_1) < len(cluster_2):
        a1.append(dist(center_1, s))
a2 = []
for s in stars:
    if len(cluster_1) < len(cluster_2):
        a2.append(dist(center_2, s))
print(max(a1) * 10000, max(a2) * 10000)