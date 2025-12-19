class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Start from end
        # Skip trailing spaces
        # Count letters until we hit a space

        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        # Count last word length
        last_word_len = 0
        while i >= 0 and s[i] != " ":
            last_word_len += 1
            i -= 1

        return last_word_len

