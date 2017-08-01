class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        Find the medium of two sorted arrays.
        
        Time complexity: O(N), where N is the length of the combined array.
        Space complexity: O(N)
        
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        length = len(nums1) + len(nums2)

        combined = []

        i1 = 0
        i2 = 0

        for i in range(0, length):
            if i1 >= len(arr1):
                combined.append(arr2[i2])
                i2 += 1
                continue
            elif i2 >= len(arr2):
                combined.append(arr1[i1])
                i1 += 1
                continue

            if arr1[i1] < arr2[i2]:
                combined.append(arr1[i1])
                i1 += 1
            else:
                combined.append(arr2[i2])
                i2 += 1

        if length % 2 == 0:
            # Length is even
           median = (combined[(length // 2) - 1] + combined[length // 2]) / 2
        else:
            # Length is odd
            median = combined[(length // 2) + 1]

        print(combined)
        return median


s = Solution()

arr1 = [1, 2, 3, 4]
arr2 = []

print(sorted(arr1 + arr2))
print(s.findMedianSortedArrays(arr1, arr2))