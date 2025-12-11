class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Given an array nums, integer target, return indices [] of the two numbers such that they add up to target number
        # Assume each input has one solution and cant use same element twice like 2+2 = 4target no.
        # Return those two indices containing the numbers

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if (nums[i] + nums[j] == target):
                    return(i, j)

        # Brute force check each value in array with all other values. Each time it checks to see if they can
        # add up together to be equal to target
        # Return only the indeces.
                
        


        