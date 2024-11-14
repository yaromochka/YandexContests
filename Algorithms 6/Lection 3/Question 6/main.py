def evaluate(expression):
    def apply_operator(op, b, a):
        if op == '+':
            return a + b
        elif op == '-':
            return a - b
        elif op == '*':
            return a * b
        elif op == '/':
            if b == 0:
                return 'WRONG'
            return a // b
    def precedence(op):
        if op in ('+', '-'): return 1
        if op in ('*', '/'): return 2
        return 0
    values = []
    operators = []
    i = 0
    n = len(expression)
    while i < n:
        ch = expression[i]
        if ch == ' ':
            i += 1
            continue
        if ch.isdigit():
            num = 0
            while i < n and expression[i].isdigit():
                num = num * 10 + int(expression[i])
                i += 1
            values.append(num)
        elif ch == '(':
            operators.append(ch)
            i += 1
        elif ch == ')':
            while operators and operators[-1] != '(':
                if len(values) < 2: return "WRONG"
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.append(apply_operator(op, b, a))
            if operators and operators[-1] == '(': operators.pop()
            else: return "WRONG"
            i += 1
        elif ch in '+-*/':
            while (operators and operators[-1] != '(' and
                   precedence(operators[-1]) >= precedence(ch)):
                if len(values) < 2:
                    return "WRONG"
                op = operators.pop()
                b = values.pop()
                a = values.pop()
                values.append(apply_operator(op, b, a))
            operators.append(ch)
            i += 1
        else: return "WRONG"
    while operators:
        if len(values) < 2: return "WRONG"
        op = operators.pop()
        b = values.pop()
        a = values.pop()
        values.append(apply_operator(op, b, a))
    if len(values) == 1: return values[0]
    else: return "WRONG"
expression = input().strip()
result = evaluate(expression)
print(result)