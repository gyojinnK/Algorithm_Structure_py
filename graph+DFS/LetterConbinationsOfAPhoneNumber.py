'''
2부터 9까지의 숫자가 포함된 문자열이 주어지면 숫자가 나타낼 수 있는 가능한 모든 문자 조합을 반환합니다.
어떤 순서로든 답을 반환하세요.
전화 버튼과 마찬가지로 숫자를 문자로 매핑하는 방법은 다음과 같습니다.
1은 어떤 문자에도 매핑되지 않습니다.
'''
# 참고: itertools
# https://soundprovider.tistory.com/entry/python-itertools
from itertools import product
from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # len = 9
        digitsToken = [
            [], ['abc'], ['def'], ['ghi'], ['jkl'], ['mno'], ['pqrs'], ['tuv'], ['wxyz']
        ]
        arr = []
        res = []
        for t in digits:
            arr += digitsToken[int(t)-1]

        combi = product(*arr)
        for el in combi:
            temp = ''
            for t in el:
                temp += t
            res.append(temp)

        return res


s = Solution()
s.letterCombinations("23")