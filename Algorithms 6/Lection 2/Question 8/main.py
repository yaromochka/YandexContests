n = int(input())
arr = [int(i) for i in input().split()]
prefix_sum = [0] * n
current_sum = minimal = 0
for i in range(n):
    prefix_sum[i] = prefix_sum[i - 1] + arr[i]
    if i != 0:
        current_sum += arr[i] * i
minimal = float('inf')
for i in range(1, n):
    current_sum = current_sum + prefix_sum[i - 1] - arr[i] - (prefix_sum[n - 1] - prefix_sum[i])
    minimal = min(current_sum, minimal)
print(minimal)