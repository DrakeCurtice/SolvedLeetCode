class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # Greedy problem. Check furthest reach from each index
        # From each furthest reach, check if its furthest reach
        # can get to the last index
        # Remember that you don't have to jump the furthest jumps
        # You can jump shorter

        farthest = 0
        for i in range(len(nums)):

            if i > farthest:
                return False
            
            farthest = max(farthest, i + nums[i])

            if farthest >= len(nums) -1:
                return True

        return True

