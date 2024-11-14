n, c = map(int, input().split())
s = input()
ans = count_a = count_b = roughness = right = 0
for left in range(n):
    while right < n and roughness <= c:
        if s[right] == 'a': count_a += 1
        elif s[right] == 'b':
            count_b += 1
            roughness += count_a
        if roughness > c: ans = max(ans, right - left)
        else: ans = max(ans, right - left + 1)
        right += 1
    else:
        if s[left] == 'a':
            roughness -= count_b
            count_a -= 1
        if s[left] == 'b': count_b -= 1
    left += 1
print(ans)