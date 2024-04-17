from typing import List


class Solution:
    # merge sort
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()

        total = len(merged)

        if total % 2 == 1:
            return float(merged[total // 2])
        else:
            middle1 = merged[total // 2 - 1]
            middle2 = merged[total // 2]
            return (float(middle1) + float(middle2)) / 2.0

    # two pointers
    def findMedianSortedArraysI(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        i = 0
        j = 0
        m1 = 0
        m2 = 0

        for count in range(0, (n + m) // 2 + 1):  # 不包括最后一个
            m2 = m1
            if i < n and j < m:
                if nums1[i] > nums2[j]:
                    m1 = nums2[j]
                    j += 1
                else:
                    m1 = nums1[i]
                    i += 1
            elif i < n:
                m1 = nums1[i]
                i += 1
            else:
                m1 = nums2[j]
                j += 1

        if (n + m) % 2 == 1:
            return float(m1)
        else:
            return (float(m1) + float(m2)) / 2.0

    # binary search
    def findMedianSortedArraysIII(self, nums1: List[int], nums2: List[int]) -> float:
        n1 = len(nums1)
        n2 = len(nums2)
        # 假定nums1的长度比nums2小，统一处理
        if n1 > n2:
            return self.findMedianSortedArraysII(nums2, nums1)

        n = n1 + n2
        # 确定左半边的长度,size
        left = (n1 + n2 + 1) // 2
        low = 0
        high = n1

        while low <= high:
            # 计算median在nums1的位置
            mid1 = (low + high) // 2
            # 计算median在nums2的位置
            mid2 = left - mid1

            # 初始化为负无穷大,l1, l2 是左侧分区的最大值，r1, r2 是右侧分区的最小值
            l1 = float('-inf')
            l2 = float('-inf')
            r1 = float('inf')
            r2 = float('inf')
            # 更新这几个变量
            # 这些边界值 (l1, l2, r1, r2) 用于检查当前的分割线是否正确。
            # 正确的分割意味着任何左侧分区的元素不应大于右侧分区的任何元素
            if mid1 < n1:
                r1 = nums1[mid1]
            if mid2 < n2:
                r2 = nums2[mid2]
            if mid1 - 1 >= 0:
                l1 = nums1[mid1 - 1]
            if mid2 - 1 >= 0:
                l2 = nums2[mid2 - 1]

            # 检查分割是否正确的条件是 l1 <= r2 和 l2 <= r1。如果这些条件都满足，表示我们找到了正确的分割线
            if l1 <= r2 and l2 <= r1:
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            # nums1 的中间值太大，需要向左调整 high
            elif l1 > r2:
                high = mid1 - 1
            # nums1 的中间值太小，需要向右调整 low
            else:
                low = mid1 + 1
        return 0

    def findMedianSortedArraysIV(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        left = (m + n + 1) // 2
        right = (m + n + 2) // 2
        return (self.findKth(nums1, 0, nums2, left) + self.findKth(nums1, 0, nums2, right)) / 2.0

    def findKth(self, nums1, i, nums2, j, k):
        if i >= len(nums1):
            return nums2[j + k - 1]
        if j >= len(nums2):
            return nums1[i + k - 1]
        if k == 1:
            return min(nums1[i], nums2[j])

        midVal1 = nums1[i + k // 2 - 1] if i + k // 2 - 1 < len(nums1) else float('inf')
        midVal2 = nums2[i + k // 2 - 1] if i + k // 2 - 1 < len(nums2) else float('inf')

        if midVal1 < midVal2:
            return self.findKth(nums1, i + k // 2, nums2, j, k - k // 2)
        else:
            return self.findKth(nums1, i, nums2, j + k // 2, k - k // 2)


if __name__ == "__main__":
    solution = Solution()
    solution.findMedianSortedArrays([1, 3], [2, 4])
