from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_A_1 = [d for d in dots if d[1] < -6]
cluster_A_2 = [d for d in dots if -6 < d[1] < 10 / 12 * d[0] - 10]
cluster_A_3 = [d for d in dots if 10 / 12 * d[0] - 10 < d[1]]

clusters = [cluster_A_1, cluster_A_2, cluster_A_3]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)


with open(r'.\files\27_B_21599.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

cluster_B_1 = [d for d in dots if d[1] < -2 * d[0] - 26]
cluster_B_2 = [d for d in dots if -2 * d[0] - 26 < d[1] and d[0] < -10]
cluster_B_3 = [d for d in dots if -10 < d[0] and 2 * d[0] + 14 < d[1]]
cluster_B_4 = [d for d in dots if d[0] < d[1] < 2 * d[0] + 14]
cluster_B_5 = [d for d in dots if -5 < d[1] < d[0]]
cluster_B_6 = [d for d in dots if d[1] < -5]

clusters = [cluster_B_1, cluster_B_2, cluster_B_3, cluster_B_4, cluster_B_5, cluster_B_6]

centers = [center(cluster) for cluster in clusters]
print(sum(c[0] for c in centers) / len(centers) * 10_000)
print(sum(c[1] for c in centers) / len(centers) * 10_000)