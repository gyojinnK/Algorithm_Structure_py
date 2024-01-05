def lengthOfLongestSubstring(s: str) -> int:
    # 탐색을 위한 투포인터
    checker = []
    head = 0
    rear = 0
    longest = 0

    while rear < len(s):
        # 중복(재등장) 확인을 위함
        if s[rear] in checker:
            longest = max(longest, len(checker))
            checker = []
            head += 1
            rear = head
        else:
            checker.append(s[rear])
            longest = max(longest, len(checker))
            rear += 1

    return longest

print(lengthOfLongestSubstring("abcabcbb"))