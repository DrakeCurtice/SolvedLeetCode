class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # Find longest common prefix for an array containing strings
        # First check if first character matches, if no then output "", if yes then that letter is part of the common prefix
        # Figure out some way to capture the next few characters that are matching
        # Maybe check if first char match, if so then store that char, and check next char, if match then store that also and so on.
        prefix = ""
        first = strs[0]

        for i in range(len(first)): # Compares the characters in the first word to all other words
            common_char = first[i]

            for j in strs:
                if i >= len(j) or j[i] != common_char:
                    return prefix

            prefix += common_char

        return prefix

            