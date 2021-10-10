class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        vec = []
        used = [0 for _ in range(len(nums))]

        def backtrack(used):
            repeat_nums_at_same_level = []

            if len(vec) == len(nums):
                res.append(vec.copy())
                return

            for i in range(len(nums)):
                
                if nums[i] in repeat_nums_at_same_level:
                    continue

                if used[i] == 0:
                    repeat_nums_at_same_level.append(nums[i])
                    used[i] = 1
                    vec.append(nums[i])
                    backtrack(used)
                    vec.pop()
                    used[i] = 0

        backtrack(used)
        return res
