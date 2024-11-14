n, k = map(int, input().split())
arr = sorted([int(i) for i in input().split()])
r = ans = 0
for l in range(n):
    while r < n and (arr[r] - arr[l]) <= k:
        ans = max(ans, r - l + 1)
        r += 1
    else: l += 1
print(ans)