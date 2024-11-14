n = int(input())
stack = []
prefix_sum = []
for i in range(n):
    elem = input()
    if elem[0] == '+':
        number = int(elem[1::])
        stack.append(number)
        if prefix_sum: prefix_sum.append(prefix_sum[-1] + number)
        else: prefix_sum.append(number)
    elif elem[0] == '-':
        prefix_sum.pop()
        print(stack.pop())
    elif elem[0] == '?':
        limit = int(elem[1::])
        if limit == len(prefix_sum): print(prefix_sum[-1])
        else: print(prefix_sum[-1] - prefix_sum[-1 - limit])