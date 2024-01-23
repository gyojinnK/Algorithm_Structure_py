'''
당신은 거리의 집을 털려는 전문 강도입니다.
각 집에는 일정 금액의 돈이 숨겨져 있으며,
각 집에서 물건을 강탈하는 것을 막는 유일한 제약은 인접한 집에 보안 시스템이 연결되어 있고
같은 밤에 인접한 두 집에 침입한 경우 자동으로 경찰에 연락한다는 것입니다.
각 집의 돈 금액을 나타내는 정수 배열 숫자가 주어지면,
오늘 밤 경찰에 신고하지 않고 도둑질할 수 있는 최대 돈 금액을 반환하십시오.
'''
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [nums[0]]
        idx = 1
        while 1:
            target = nums[idx]
            acc = dp[-1]


print(Solution().rob([2,7,9,3,1]))