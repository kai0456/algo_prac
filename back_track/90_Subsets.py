class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        res = []
        path = []

        nums.sort()

        def backtrack(sp):

            res.append(path.copy())

            for i in range(sp, len(nums)):

                if i > sp and nums[i] == nums[i-1]:
                    continue
                else:
                    path.append(nums[i])
                    
                    backtrack(i+1)
                    path.pop()

        backtrack(0)
        return res