with open(r'./files/26_7014.txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

max_earning_per_day = 0
sum_earning = 0

while prices:
    max_price = max(prices)
    pos = len(prices) - prices[::-1].index(max_price) - 1
    earning_per_day = max_price * (pos + 1)
    sum_earning += earning_per_day
    max_earning_per_day = max(max_earning_per_day, earning_per_day)
    prices = prices[pos + 1:]

print(sum_earning, max_earning_per_day)