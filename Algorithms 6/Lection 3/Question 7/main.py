from collections import deque


n = int(input())
w = input()
s = input()
dick = {
    '(': (')', w.index('(')),
    ')': ('(', w.index(')')),
    '[': (']', w.index('[')),
    ']': ('[', w.index(']'))
}
min_open_bracket = '(' if dick['('][1] < dick['['][1] else '['
stack_closed = deque()
stack = deque()
s = s if len(s) > 0 else min_open_bracket
i = 0
while i < n:
    if i < len(s):
        bracket = s[i]
        if bracket in '([':
            stack.append(bracket)
            stack_closed.appendleft(dick[bracket][0])
        elif bracket in ')]':
            stack.append(stack_closed.popleft())
    else:
        while len(stack) < n - len(stack_closed) - 1:
            if stack[-1] in '([':
                closed_last = dick[stack[-1]][0]
                if dick[closed_last][1] < dick[min_open_bracket][1]: stack.append(stack_closed.popleft())
                else:
                    stack.append(min_open_bracket)
                    stack_closed.appendleft(dick[min_open_bracket][0])
            elif stack[-1] in ')]':
                if stack_closed:
                    closed_last = stack_closed[0]
                    if dick[closed_last][1] < dick[min_open_bracket][1]:
                        stack.append(stack_closed.popleft())
                    else:
                        stack.append(min_open_bracket)
                        stack_closed.appendleft(dick[min_open_bracket][0])
                else:
                    stack.append(min_open_bracket)
                    stack_closed.appendleft(dick[min_open_bracket][0])
            i += 1

        else:
            while stack_closed:
                stack.append(stack_closed.popleft())
                i += 1
    i += 1
[print(el, end='') for el in stack]


# 14
# ]([)
# ([[]()[]

# ([[]()[]](())
# ([[]()[]](()))