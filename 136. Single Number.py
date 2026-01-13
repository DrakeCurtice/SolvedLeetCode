class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Every element appears twice except for one element
        counts = {}
        for val in nums:
            if val in counts:
                counts[val] += 1
            else:
                counts[val] = 1

        for val in counts:
            if counts[val] == 1:
                return val


