n = int(input())
arr = [int(num) for num in input().split()]
ans = [0] * (len(arr))
for i in range(len(arr)):
    ans[i] = ans[i - 1] + arr[i]
print(*ans)