class Solution:
    def search(self, nums: List[int], target: int) -> int:

        # We are given a sorted, ascending array called nums, and an integer target
        # Goal is to search for target in nums and if it exists, return the index.
        # Binary search cuts the array size in half each move
        # If middle > target, search left
        # if middle < target, search right

        # Left and right are both indexes
        left = 0
        right = len(nums) -1
      
        while left <= right:
            middle = ((left + right) // 2)
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            elif nums[middle] < target:
                left = middle + 1
        
        return -1
        

