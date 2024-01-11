'''
2부터 9까지의 숫자가 포함된 문자열이 주어지면 숫자가 나타낼 수 있는 가능한 모든 문자 조합을 반환합니다.
어떤 순서로든 답을 반환하세요.
전화 버튼과 마찬가지로 숫자를 문자로 매핑하는 방법은 다음과 같습니다.
1은 어떤 문자에도 매핑되지 않습니다.
'''
from typing import List

code = {
    '2':['a','b','c'],
    '3':['d','e','f'],
    '4':['g','h','i'],
    '5':['j','k','l'],
    '6':['m','n','o'],
    '7':['p','q','r','s'],
    '8':['t','u','v'],
    '9':['w','x','y','z']
}

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        pass







s = Solution()
s.letterCombinations("234")