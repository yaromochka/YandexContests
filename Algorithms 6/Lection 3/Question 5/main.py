s = input().replace(' ', '')
notation = []
ans = ''
for i in range(len(s)):
    elem = s[i]
    num = ''
    while i < len(s) and s[i].isdigit():
        num += s[i]
        i += 1
    else:
        ans += num
    if elem in '-*+/':
        if elem == '+' or elem == '-':
            while notation and (notation[-1] in '*/+-'): ans += notation.pop()
        if elem == '*' or elem == '/':
            while notation and (notation[-1] in '*/'): ans += notation.pop()
        notation.append(elem)
    else:
        if elem == '(': notation.append(elem)
        if elem == ')':
            while notation and notation[-1] != '(': ans += notation.pop()
            notation.pop()
ans = ans + ''.join(notation[::-1])
print(ans)
stack = []
for elem in ans:
    if elem in '0123456789': stack.append(elem)
    else:
        if len(stack) >= 2:
            second, first = stack.pop(), stack.pop()
            if elem == '+': stack.append(int(first) + int(second))
            if elem == '-': stack.append(int(first) - int(second))
            if elem == '*': stack.append(int(first) * int(second))
        else:
            stack = []
            break
print(*stack if len(stack) == 1 else "WRONG", sep='')