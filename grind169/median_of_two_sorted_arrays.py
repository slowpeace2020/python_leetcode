from typing import List


class Solution:
    def findMedianSortedArrays(self,nums1:List[int],nums2:List[int])->float:
        merged = nums1+nums2
        merged.sort()

        total = len(merged)


