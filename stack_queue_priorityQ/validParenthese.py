# 하나 적재
# 다음 적재 후 짝이 맞는지 체크
# 짝이 맞으면 제거


def isValid(s):
    open = ['(','{','[']
    cor = {
        '(' : ')',
        '{' : '}',
        '[' : ']'
    }

    stack = []
    for t in s:
        # 유효한 인접 괄호 제거
        if stack and cor[stack[len(stack)-1]] == t:
            stack.pop()
        # 위 조건을 만족하지 못한 경우 제가
        # 1. 유효괄호가 아닌 경우 ex) [}
        # 2. 닫는 괄호부터 적재된 경우
        # 3. ...
        elif t not in open:
            return False
        else:
            stack.append(t)

    if not stack:
        return True
    else:
        return False

print(isValid("([)]"))