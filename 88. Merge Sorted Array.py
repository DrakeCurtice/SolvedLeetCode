class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        counter = 0
        for i in range(len(nums1)):
            if m == 0:
                nums1[i] = nums2[counter]
                counter += 1
            while nums1[i] == 0 and counter < n and m > 0:
                nums1[i] = nums2[counter]
                counter += 1
        nums1.sort()
            
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
