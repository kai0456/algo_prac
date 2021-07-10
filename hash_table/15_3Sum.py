class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s_nums = sorted(nums)
        ans = []


        for i, n in enumerate(s_nums):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue

            left = i + 1
            right = len(s_nums) - 1

            diff = 0 - n

            while left < right:

                if s_nums[left] + s_nums[right] + n > 0:
                    right -= 1
                elif s_nums[left] + s_nums[right] + n < 0:
                    left += 1
                else:
                    while left < right and s_nums[left] == s_nums[left+1]:
                        left += 1
                    while left < right and s_nums[right] == s_nums[right-1]:
                        right -= 1
                    ans.append([n, s_nums[left], s_nums[right]])
                    left += 1
                    right -= 1
        return ans

