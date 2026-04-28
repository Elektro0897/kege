from math import *
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
        x, y, data = i.replace(',','.').split()
        dots.append(list(map(float, [x, y])))
        if data[-3:] == 'VII':
            stars.append(dots[-1])

cluster_1 = [d for d in dots if d[1] < 8]
cluster_2 = [d for d in dots if d[1] > 8]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

stars_1 = [d for d in stars if d[1] < 8]
stars_2 = [d for d in stars if d[1] > 8]

ans = []
for s in stars_1:
    ans.append(dist(center_1, s))
for s in stars_2:
    ans.append(dist(center_2, s))

print(min(ans) * 10000, max(ans) * 10000)
####################################################

cluster_1 = [[d for d in dots if d[1] > 8],
             [d for d in stars if d[1] > 8]]
cluster_2 = [[d for d in dots if d[1] < 8],
             [d for d in stars if d[1] < 8]]
clusters = [cluster_1, cluster_2]

a1 = min(dist(center(cl[0]), s) for cl in clusters for s in cl[1]) * 10000
a2 = max(dist(center(cl[0]), s) for cl in clusters for s in cl[1]) * 10000
print(a1, a2)
