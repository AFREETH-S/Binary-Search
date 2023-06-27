class Solution:

    def merge(self, nums1: List[int], nums2: List[int], sorted_arr: List[int]):
        i, j = 0, 0
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                sorted_arr.append(nums1[i])
                i += 1
            else:
                sorted_arr.append(nums2[j])
                j += 1

        sorted_arr.extend(nums1[i:])
        sorted_arr.extend(nums2[j:])


    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        sorted_arr = []
        self.merge(nums1, nums2, sorted_arr)

        
        isOddArr = len(sorted_arr) %  2 != 0
        middle_item_idx = floor(len(sorted_arr) / 2)
        if isOddArr:
            return sorted_arr[middle_item_idx]
        else:
            i, j = int(middle_item_idx) - 1, int(middle_item_idx) 
            return (sorted_arr[i] + sorted_arr[j]) / 2

        return 0
