
# from typing import List


class Solution(object):
    def merge(self, nums1: list, m: int, nums2: list, n: int):
        self.nums1 = nums1
        self.m = m
        self.nums2 = nums2
        self.n = n

        nums1 = nums1[:m] + nums2[:n]
        return sorted(nums1)
    


a = [1,2,3,0,0,0]
b = 3
c = [2,5,6]
d = 3

# e = a[:b] + c[:d]
# print(e.sort())
# print(merge(a,b,c,d))

solve = Solution
print(solve.merge(a,b,c,d,d))