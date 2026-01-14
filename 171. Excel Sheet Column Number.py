class Solution:
    def titleToNumber(self, columnTitle: str) -> int:

        length = len(columnTitle)
        ans = 0
        
        for letter in columnTitle:
            value = ord(letter) - ord('A') + 1
            ans = ans * 26 + value

        return ans
            


