class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:

        res = []
        path = []
        if len(s) > 3*4:
            return []

        def backtrack(sp):
            if sp >= len(s):
                if len(path) == 4:
                    path_str = '.'.join(path)
                    res.append(path_str)
                    return
                else:
                    return

            for i in range(sp, min(sp+3, len(s))):
                if int(s[sp:i+1]) >= 0 and int(s[sp:i+1]) <= 255:
                    if len(s[sp:i+1]) >1 and s[sp:i+1][0] == '0':
                        continue
                    else:

                        path.append(s[sp:i+1])
                        backtrack(i+1)
                        path.pop()
                else:
                    continue

        backtrack(0)

        return res

