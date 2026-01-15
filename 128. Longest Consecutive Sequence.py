class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        max_val = 0
        st = set(nums)
        sequence = {}

        for num in st:
            if num-1 not in st:
                tmp = 1
                while num+1 in st:
                    tmp += 1
                    num += 1
                
                max_val = max(max_val, tmp)

        return max_val
        

        
