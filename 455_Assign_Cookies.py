
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:

        g.sort()
        s.sort()

        res = 0
        j = 0
        for i in range(len(g)):
            while j < len(s):
                if g[i] <= s[j]:
                    res += 1
                    j += 1
                    break
                else:
                    j += 1
            if j == len(s):
                break

        return res





