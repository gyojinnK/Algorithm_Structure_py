'''
이미 감소하지 않는 순서로 정렬되어 있는 1 인덱스 정수 배열이 주어지면
특정 목표 숫자에 합산되는 두 개의 숫자를 찾습니다.
이 두 숫자를 숫자[index1]과 숫자[index2]로 둡니다.
여기서 1 <= index1 < index2 <= 숫자.길이입니다.
두 숫자 index1과 index2의 인덱스를 길이 2의 정수 배열 [index1, index2]로 1씩 더한 값으로 반환합니다.
테스트는 정확히 하나의 솔루션이 있도록 생성됩니다.
동일한 요소를 두 번 사용할 수 없습니다.
솔루션은 일정한 추가 공간만 사용해야 합니다.
'''
from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        start = 0
        end = len(numbers) - 1
        while start < end:
            ts = numbers[start] + numbers[end]
            if ts < target:
                start += 1
            elif ts > target:
                end -= 1
            else:
                res.append([start+1, end+1])
                break

        return res[0]


print(Solution().twoSum([5,25,75], 100))
# Solution().twoSum([2, 7, 11, 15], 9)
# Solution().twoSum([-1, 0], -1)
# Solution().twoSum([2,3,4], 6)
