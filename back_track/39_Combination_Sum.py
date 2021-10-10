
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        vec = []

        if len(candidates) == 0:
            return res

        def backtrack(candidates, sp, summ):
            if summ == target:
                res.append(vec.copy())
                return

            if summ > target:
                return

            for i in range(sp, len(candidates)):
                vec.append(candidates[i])
                summ += candidates[i]
                backtrack(candidates, i, summ)
                summ -= candidates[i]
                vec.pop()

        summ = 0
        backtrack(candidates, 0, summ)

        return res
