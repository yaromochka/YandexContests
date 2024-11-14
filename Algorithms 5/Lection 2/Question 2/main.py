n, k = map(int, input().split())
prices = list(map(int, input().split()))
max_profit = 0
for i in range(1, n):
    min_price = prices[max(0, i - k):i]
    min_price = min(min_price) if min_price else prices[i]
    profit = prices[i] - min_price
    max_profit = max(max_profit, profit)
print(max_profit)