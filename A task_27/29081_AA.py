from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, info = i.replace(',','.').split()
        dots.append([float(x), float(y)])
        if info == 'VII':
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if d[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

a = []
for s in stars_1:
    a.append(dist(center_1, s))

for s in stars_2:
    a.append(dist(center_2, s))

print(min(a) * 10000, max(a) * 10000)