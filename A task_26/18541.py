with open(r'./files/26_18541.txt') as file:
    n, m = map(int, file.readline().split())
    data = [int(i) for i in file]

weights = sorted(data[:n], reverse=True)
athletes = sorted(data[n:], reverse=True)

lifted_weights = []
for athlete in athletes:
    for weight in weights:
        if athlete >= weight:
            lifted_weights.append(weight)
            break

print(sum(lifted_weights) / len(lifted_weights))
print(max(lifted_weights, key=lambda x: lifted_weights.count(x)))