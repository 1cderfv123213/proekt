while True:
    try:
        t = input()
    except EOFError:
        break
    if not t:
        break
    stack = []
    u = 0
    for j in t:
        if j == "{":
            stack.append(0)
        elif j == "[":
            stack.append(1)
        elif j == "(":
            stack.append(2)
        else:
            if not stack:
                u = 1
                break
            else:
                if j == "}":
                    if stack[-1] == 0:
                        stack.pop()
                    else:
                        u = 1
                        break
                if j == "]":
                    if stack[-1] == 1:
                        stack.pop()
                    else:
                        u = 1
                        break
                if j == ")":
                    if stack[-1] == 2:
                        stack.pop()
                    else:
                        u = 1
                        break
    if not stack and not u:
        print(0, end="")
    else:
        print(1, end="")
