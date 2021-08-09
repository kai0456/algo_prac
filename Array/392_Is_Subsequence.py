# two pointers
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        j = 0
        for i in range(len(s)):
            while j < len(t) and t[j] != s[i]:
                j += 1
            j += 1
            if i < len(s) and j > len(t):
                return False
        
        return True


#dp 
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        dp = [[0]*(len(t)+1) for i in range(len(s)+1)]

        for i in range(1, len(s)+1):
            for j in range(1, len(t)+1):
                if s[i-1] == t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])

        if dp[-1][-1] == len(s):
            return True
        else:
            return False