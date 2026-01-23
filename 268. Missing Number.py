class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Array nums contains n distinct numbers in range 0 to n
        # Return the ONLY number in the range that is missing from array
        
        # Create dict with key value pairs, storing COUNT and number
        # This dict will hold numbers [0, n]
        # Return the NUMBER of the one with 0 COUNT

        missing = {}
        n = len(nums)

        for i in range(n + 1):
            missing[i] = 0

        for idx in range(len(nums)):
            missing[nums[idx]] += 1

        for i in range(n + 1):
            if missing[i] == 0:
                return i


