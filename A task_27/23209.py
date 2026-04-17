from math import dist

def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]

with open(r'./files/27_A_23209.txt') as file:
    dots = [list(map(float, i.replace(',','.').split())) for i in file]

cluster_A_1 = [d for d in dots if d[0] < 5]
cluster_A_2 = [d for d in dots if d[0] > 5]

center_A_1 = center(cluster_A_1)
center_A_2 = center(cluster_A_2)

print(abs(max(center_A_1[0], center_A_2[0])) * 10000)
print(abs(max(center_A_1[1], center_A_2[1])) * 10000)

with open(r'./files/27_B_23209.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [d for d in dots if 0 < d[1] < 10]
cluster_B_2 = [d for d in dots if 10 < d[1] < 21]
cluster_B_3 = [d for d in dots if 21 < d[1] < 28]
clusters_B = [cluster_B_1, cluster_B_2, cluster_B_3]

max_cluster = center(max(clusters_B, key=len))
min_cluster = center(min(clusters_B, key=len))

print((max_cluster[0] - min_cluster[0]) * 10_000)
print((max_cluster[1] - min_cluster[1]) * 10_000)

center_B_1 = center(cluster_B_1)
center_B_2 = center(cluster_B_2)
center_B_3 = center(cluster_B_3)

print((center_B_1[0] - center_B_3[0]) * 10000)
print((center_B_1[1] - center_B_3[1]) * 10000)