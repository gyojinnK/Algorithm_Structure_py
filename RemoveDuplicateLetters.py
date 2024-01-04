import collections


def removeDuplicateLetters(s):
    counter, stack = collections.Counter(s), []
    print(counter)

    for char in s:
        counter[char] -= 1
        if char in stack:
            continue
        # 뒤에 붙일 문자가 남아있다면 스택에서 제거
        # 뽑은 문자가 스택 상단의 문자 보다 작고 이후 상단의 문자가 이후 재등장한다면
        while stack and char < stack[-1] and counter[stack[-1]] > 0:
            stack.pop()
        stack.append(char)

    return ''.join(stack)

print(removeDuplicateLetters("cbacdcbc"))

# a b b c c