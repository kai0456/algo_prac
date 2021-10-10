class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = ["", # 0
                    "", # 1
                    "abc", # 2
                    "def", # 3
                    "ghi", # 4
                    "jkl", # 5
                    "mno", # 6
                    "pqrs", # 7
                    "tuv", # 8
                    "wxyz" # 9
                ]

        res = []
        vec = []

        d = {i:letters[i] for i in range(len(letters))}

        def backtrack(digits, id):
            if len(digits) == 0:
                return res

            if len(vec) == len(digits):
                vec_str = ''.join(vec)
                res.append(vec_str)
                return

            for i in range(id, len(digits)):
                digit = int(digits[i])
                # print(digit)
                # print(d)
                for j in range(len(d[digit])):
                    vec.append(d[digit][j])
                    backtrack(digits, i+1)
                    vec.pop()

        backtrack(digits, 0)

        return res


