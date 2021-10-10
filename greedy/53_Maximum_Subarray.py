
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-math.inf] * (len(nums)+1)
        dp[0] = nums[0]


        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        res = max(dp)

        return res