class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        s_nums = sorted(nums)
        ans = []

        for i, n in enumerate(s_nums):
            if i > 0 and s_nums[i] == s_nums[i-1]:
                continue
                
            for j in range(i+1, len(s_nums)):
                if j > i+1 and s_nums[j] == s_nums[j-1]:
                    continue

                left = j + 1
                right = len(s_nums) - 1

                while left < right:
                    if s_nums[i] + s_nums[j] + s_nums[left] + s_nums[right] > target:
                        right -= 1
                    elif s_nums[i] + s_nums[j] + s_nums[left] + s_nums[right] < target:
                        left += 1
                    else:
                        ans.append([s_nums[i], s_nums[j], s_nums[left], s_nums[right]])
                        while left < right and s_nums[left] == s_nums[left+1]:
                            left += 1
                        while left < right and s_nums[right] == s_nums[right-1]:
                            right -= 1

                        left += 1
                        right -= 1
        return ans