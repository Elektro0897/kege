with open(r'./files/26_17687.txt') as file:
    n = int(file.readline())
    prices = [int(i) for i in file]

prices = sorted(prices, reverse=True)

k = 9
luck_price_customer = sum(prices) - sum(prices[:n // k])
real_price_customer = sum(prices) - sum(prices[k - 1::k])

print(luck_price_customer, real_price_customer)