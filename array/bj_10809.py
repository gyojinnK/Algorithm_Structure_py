import string

def get_idx_naive(word):
    # O(N^2)
    result = [-1]*len(string.ascii_lowercase)
    for i in range(len(word)):
        char = word[i]
        for j in range(len(string.ascii_lowercase)):
            lo = string.ascii_lowercase[j]
            if result[j] == -1 and char == lo:
                result[j] = i
    # 요소와 요소 사이에 ' '를 넣고 join을 이용해서 for문으로 반복적으로 str타입으로 변환하여 num을 하나의 변수로 합친다
    print(' '.join([str(num) for num in result]))

def get_idx(word):
    # point 1. ord
    # point 2. 아스키 코드 활용
    # point 3. O(n)
    result = [-1] * len(string.ascii_lowercase)
    for i in range(len(word)):
        # ord: 문자(알파벳 대소문자) -> 숫자로 변환
        # a -> 97, b -> 98 ...
        idx = ord(word[i]) - 97  # ord를 이용해서 현재 가리키고 있는 알파벳의 위치를 만들어줌
        if result[idx] == -1:
            result[idx] = i
    print(' '.join([str(num) for num in result]))

get_idx_naive('baekjoon')
get_idx('baekjoon')

# 내 첫 풀이 (오답)
# import string
#
# def result(S):
#     exam = string.ascii_lowercase
#     res = ""
#     for al in exam:
#         if al in S:
#             for el in S:
#                 if al == el:
#                     res += str(S.index(el))
#                     res += " "
#                 else:
#                     continue
#         else:
#             res += str(-1)
#             res += " "
#
#     return(print(res))
#
# if __name__ == '__main__':
#     result('baekjoon')