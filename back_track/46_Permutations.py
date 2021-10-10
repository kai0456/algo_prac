class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        vec = []
        used = [0 for _ in range(len(nums))]

        def backtrack(used):
            if len(vec) == len(nums):
                res.append(vec.copy())
                return

            for i in range(len(nums)):
                
                if used[i] == 0:
                    used[i] = 1
                    vec.append(nums[i])
                    backtrack(used)
                    vec.pop()
                    used[i] = 0

        backtrack(used)
        return res