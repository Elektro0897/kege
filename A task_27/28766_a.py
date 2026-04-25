from math import *
def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append(list(map(float, [x, y])))

cluster_1 = [d for d in dots if d[1] > 9]
cluster_2 = [d for d in dots if d[1] < 9]

clusters = [cluster_1, cluster_2]

min_center = center(min(clusters, key=len))

print(min(dist(min_center, s) for s in stars) * 10000)
print(max(dist(min_center, s) for s in stars) * 10000)