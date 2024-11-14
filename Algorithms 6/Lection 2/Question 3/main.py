n, k = map(int, input().split())
arr = sorted([int(i) for i in input().split()])
days = r = 0
prefix_sum = [0] * n
for i in range(n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
for l in range(n):
    while r < n:
        r += 1
    days += 1
print(prefix_sum)
print(days)

# 9 2
# 1 2 3 4 5 6 7 8 9