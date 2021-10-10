class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(sp):

            res.append(path.copy())

            for i in range(sp, len(nums)):
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        backtrack(0)
        return res
