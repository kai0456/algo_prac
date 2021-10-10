class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res = []
        path = []

        nums = range(1, 10)

        def backtrack(n, k, sp):
            if sum(path) > n: # cut branch to speed up
                return
            if len(path) == k and sum(path) == n:
                res.append(path.copy())
                return

            for i in range(sp, len(nums) , 1):
                path.append(nums[i])
                backtrack(n, k, i+1)
                path.pop()

        backtrack(n, k, 0)

        return res

        # - (k-len(path))