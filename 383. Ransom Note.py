import ast
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # loop through ransomNote, note down each unique character into an array
        # loop through magazine, note down each unique character into an array
        # compare the arrays to check if they contain the same unique character set

        unique_ransom = {}
        for i in ransomNote:
            if i in unique_ransom:
               unique_ransom[i] += 1
            else: 
               unique_ransom[i] = 1
        

        unique_magazine = {}
        for j in magazine:
            if j in unique_magazine:
                unique_magazine[j] += 1
            else: 
                unique_magazine[j] = 1

        # check if ransom is a subset of magazine and has enough counts of those characters
        for ch in unique_ransom:
            if ch not in unique_magazine:
                return False
            if unique_magazine[ch] < unique_ransom[ch]:
                return False

        return True
