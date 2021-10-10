class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        c_nums = [nums]*2
        
        res = [-1] * len(nums)
        stack = []
        stack.append(0)
        
        for i in range(1, len(c_nums)):
            if c_nums[stack[-1]] >= c_nums[i]:
                stack.append(i)
            else:
                while stack and c_nums[stack[-1]] < c_nums[i]:
                    c_nums_i = stack.pop()
                    if c_nums_i < len(nums):
                        res[c_nums_i] = c_nums[i]

                stack.append(i)

        return res        