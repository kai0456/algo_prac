# Greedy
# if moving sum is negative, it drags the res by reducing the number. So restart the moving_sum.
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        res = - math.inf
        moving_sum = 0

        for i in range(len(nums)):
            moving_sum += nums[i]
            res = max(res, moving_sum)

            if moving_sum <= 0:
                moving_sum = 0

        return res



# dp
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [-math.inf]*len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i-1] + nums[i])

        return dp[-1]
