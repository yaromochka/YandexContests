s = input().split()
stack = []
for elem in s:
    if elem in '0123456789': stack.append(elem)
    else:
        if elem == '+':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first) + int(second))
        if elem == '-':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first) - int(second))
        if elem == '*':
            second, first = stack.pop(), stack.pop()
            stack.append(int(first) * int(second))
print(*stack)