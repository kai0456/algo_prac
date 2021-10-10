# Brute Force
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        for i in range(len(nums1)):
            j = nums2.index(nums1[i])
            for k in range(j+1, len(nums2)):
                if nums2[k] > nums2[j]:
                    res[i] = nums2[k]
                    break
        return res


# Monotonic Stack

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [-1] * len(nums1)
        stack = []

        d = {}
        for i, n in enumerate(nums1):
            d[n] = i

        stack.append(0)
        for i in range(1,len(nums2)):
            if stack[-1] >= nums2[i]:
                stack.append(i)
            else:
                while stack and stack[-1] < nums2[i]:
                    nums2_i = stack.pop()
                    if nums2[nums2_i] in d:
                        nums1_i = d[nums2[nums2_i]]
                        res[nums1_i] = nums2[i]
                stack.append(i)

        return res
