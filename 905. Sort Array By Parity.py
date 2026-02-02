class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # build new array with even integers in first then odd integers

        sorted_nums = []

        for even in nums:
            if even % 2 == 0:
                sorted_nums.append(even)
            else:
                continue

        for odd in nums:
            if odd % 2 != 0:
                sorted_nums.append(odd)
            else:
                continue

        return sorted_nums

        
