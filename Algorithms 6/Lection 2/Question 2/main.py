n, k = map(int, input().split())
arr = [int(i) for i in input().split()]
prefix_sum = {0: 1}
current_sum = ans = 0
for num in arr:
    current_sum += num

    if (current_sum - k) in prefix_sum:
        ans += prefix_sum[current_sum - k]

    if current_sum not in prefix_sum:
        prefix_sum[current_sum] = 0
    prefix_sum[current_sum] += 1
print(ans)