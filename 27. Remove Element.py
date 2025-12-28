class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # two pointers solution

        k = 0
        for x in nums: # check every element in array
            if x != val:
                nums[k] = x
                k += 1
        
        return k

    # look at all values in array.
    # If it isnt the bad value, write down that value
    # By definition, it can't contain bad value

