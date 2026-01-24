class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # Given array nums
        # Return TRUE if ANY value appears AT LEAST twice in array
        # otherwise false
        seen = set()
        
        for i in nums:
            if i in seen:
                return True
            seen.add(i)

        return False

