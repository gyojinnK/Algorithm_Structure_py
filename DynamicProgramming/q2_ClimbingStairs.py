'''
당신은 계단을 오르고 있습니다.
정상에 도달하려면 n 단계가 필요합니다.
매번 1~2계단씩 오를 수 있습니다.
얼마나 많은 방법으로 정상에 오를 수 있나요?
'''

class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * n
        dp[0] = 1
        dp[1] = 2
        print(dp)

        for i in range(2, n):
            dp[i] = dp[i-2] + dp[i-1]

        return dp[n-1]

print(Solution().climbStairs(1))