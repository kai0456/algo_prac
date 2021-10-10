class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        vec = []

        def backtrack(sp, summ):

            if len(candidates) == 0:
                return res

            if summ > target:
                return
            elif summ == target:
                res.append(vec.copy())
                return

            for i in range(sp, len(candidates)):
                if i > sp and candidates[i] == candidates[i-1] :
                    continue
                vec.append(candidates[i])
                summ += candidates[i]
                backtrack(i+1, summ)
                summ -= candidates[i]
                vec.pop()

        summ = 0
        candidates.sort()
        backtrack(0, summ)

        return res

