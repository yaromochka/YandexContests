s = input()
stack = []
matching_parentheses = {')': '(', ']': '[', '}': '{'}
ans = True
for elem in s:
    if elem in '[({': stack.append(elem)
    else:
        if not stack or stack[-1] != matching_parentheses[elem]:
            ans = False
            break
        stack.pop()
print('yes' if ans and not stack else 'no')
print(0 % 4)