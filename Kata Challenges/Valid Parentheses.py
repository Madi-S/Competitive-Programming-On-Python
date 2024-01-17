def valid_parentheses(s):
    if s.startswith(')'):
        return False

    s = list(filter(lambda p: p in '()', s))

    if len(s) % 2 != 0:
        return False

    buf = []
    for p in s:
        if p == '(':
            buf.append(s)
        else:
            try:
                buf.pop()
            except Exception as e:
                return False
    if buf:
        return False
    return True


print(valid_parentheses('()()'))
