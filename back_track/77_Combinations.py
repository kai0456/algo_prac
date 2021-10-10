class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = range(1, n+1)
        res = []
        path = []

        def backtrack(n, k, sp):
            # sp =  starting point
            if len(path) == k:
                res.append(path.copy())
                return

            for i in range(sp, n, 1):
                path.append(nums[i])
                backtrack(n, k, i+1)
                path.pop()

        backtrack(n, k, 0)
        return res

