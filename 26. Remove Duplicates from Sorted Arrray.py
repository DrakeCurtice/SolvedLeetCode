class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        k = 1 # first element is unique

        for i in range(1, len(nums)):
            if nums[i] != nums[k-1]: # compare to the last unique
                nums[k] = nums[i]
                k += 1


        return k
            
