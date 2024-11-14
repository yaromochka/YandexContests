n = int(input())
prices = [int(i) for i in input().split()]
stack = []
result = [-1] * n
for i in range(n):
    while stack and prices[stack[-1]] > prices[i]: result[stack.pop()] = i
    stack.append(i)
print(*result)