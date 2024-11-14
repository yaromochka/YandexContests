n = int(input())
arr = [int(i) for i in input().split()]
sum_remaining = sum(arr)
k = (sum_remaining + n) // (n + 1)
ans = k * (n + 1) - sum_remaining
print(ans)