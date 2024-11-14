n = int(input())
arr = [int(i) for i in input().split()]
prefix_sum = [0] * n
for i in range(n):
    prefix_sum[i] = (prefix_sum[i - 1] + arr[i])
ans = 0
for j in range(1, n):
    left_sum = prefix_sum[j - 1]
    right_sum = prefix_sum[n - 1] - prefix_sum[j]
    ans += (arr[j] * right_sum * left_sum)
print(ans % (10 ** 9 + 7))