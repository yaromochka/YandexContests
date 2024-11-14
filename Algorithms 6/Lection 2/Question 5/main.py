n = int(input())
arr = [int(i) for i in input().split()]
arr.sort()
length = len(arr)
ans = []
while length >= 1:
    if length % 2 != 0: idx = length // 2
    else:
        idx = length // 2-1
    ans.append(arr[idx])
    arr.pop(idx)
    length = len(arr)
print(*ans)