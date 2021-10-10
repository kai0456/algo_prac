class Solution:
    def partition(self, s: str) -> List[List[str]]:

        def isPalin(s):
            if len(s) == 0:
                return False
            else:
                return s == s[::-1]

        res = []
        vec = []

        def backtrack(sp):
            if len(s) == 0:
                return

            if sp >= len(s):
                res.append(vec.copy())
                return

            for i in range(sp, len(s)):
                if isPalin(s[sp:(i+1)]):
                    vec.append(s[sp:(i+1)])
                    backtrack(i+1)
                    vec.pop()

                else:
                    continue


        backtrack(0)

        return res