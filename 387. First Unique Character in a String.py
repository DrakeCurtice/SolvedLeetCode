class Solution:
    def firstUniqChar(self, s: str) -> int:
        # Loop through all characters and store key value pairs
        # storing the character and how many times it exists in array

        # Then loop again and check every character in array and if
        # its quantity is exactly 1 then return that index

        # Else, return -1
        unique = {}

        for i in s:
            if i in unique:
                unique[i] = unique[i] + 1
            else:
                unique[i] = 1

        for idx, ch in enumerate(s):
            if unique[ch] == 1:
                return idx
    
        return -1
