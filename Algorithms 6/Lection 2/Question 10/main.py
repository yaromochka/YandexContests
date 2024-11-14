n = int(input())
evidences = list(map(int, input().split()))
m, k = map(int, input().split())
started = list(map(int, input().split()))
left = moves = 0
ans = [0] * n
for right in range(1, n):
    if evidences[right] == evidences[right - 1]:
        if moves < k:
            ans[right] = left
            moves += 1
        else:
            while moves >= k:
                if evidences[left] == evidences[left + 1]:
                    moves -= 1
                left += 1
            ans[right] = left
            moves += 1
    elif evidences[right] < evidences[right - 1]:
        left = right
        moves = 0
    ans[right] = left
to_print = []
for idx in started:
    to_print.append(ans[idx - 1] + 1)
print(*to_print)