A, B, C, D = map(int, [input() for _ in range(4)])
arr = []
if A > 0 and C > 0:
    arr.append([B + 1, D + 1])
if B > 0 and D > 0:
    arr.append([A + 1, C + 1])
if A > 0 and B > 0:
    arr.append([max(A, B) + 1, 1])
if C > 0 and D > 0:
    arr.append([1, max(C, D) + 1])
ans = min(arr, key=sum)
print(*ans)
