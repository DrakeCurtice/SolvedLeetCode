class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Loop through and look at each number
        # Store the quantity of each number and the number itself in key value pairs
        # Return the number whose quantity is > n // 2


        # Each number itself will be i here
        # 3, 2, 3
        majority = {}
        for i in nums:
            # if we see the same number again, increment
            if i in majority:
                majority[i] = majority[i] + 1
            else:
                majority[i] = 1

        threshold = len(nums) // 2
        for h in majority:

            if majority[h] > threshold:
                return h
            # Do not add an else case
