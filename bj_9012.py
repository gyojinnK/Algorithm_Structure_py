# 데스트 데이터 수
T = int(input())

stack = []
res = []
cor = {'(':')'}
for i in range(T):
    vps = input()

    for p in vps:
        if stack and stack[-1] == '(' and p == ')':
            stack.pop()
        else:
            stack.append(p)

    if not stack:
        res.append('YES')
    else:
        res.append('NO')

    stack = []

print('\n'.join([el for el in res]))

