# Brute Force
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)-1):
            count = 0
            for j in range(i+1, len(temperatures)):
                if temperatures[j] <= temperatures[i]:
                    continue
                else:
                    count = j - i
                    break

            res.append(count)

        res.append(0)

        return res
