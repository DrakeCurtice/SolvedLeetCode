class Solution:
    def longestPalindrome(self, s: str) -> str:

        best = s[0]
        for center in range(len(s)):
            # Odd length case
            left = center
            right = center

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            if right - (left + 1) > len(best):
                best = s[left + 1:right]

            # Even length case
            left = center
            right = center + 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            if right - (left + 1) > len(best):
                best = s[left + 1: right]


        return best
