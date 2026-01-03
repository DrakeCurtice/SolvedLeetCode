class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if needle == "":
            return 0

        # If needle longer than haystack, then can't be found
        if len(needle) > len(haystack):
            return -1

        # Loop only where needle can still fit
        for haystack_index in range(len(haystack) - len(needle) + 1):

            haystack_char = haystack[haystack_index]

            # If character = first character in needle start tracking
            if haystack_char == needle[0]:

                # Index of first occurence which we will return if it works
                occurence_index = haystack_index

                # Check if the following characters work
                needle_matches = True

                for needle_index in range(len(needle)):
                    if haystack[occurence_index + needle_index] != needle[needle_index]:
                        needle_matches = False
                        break
                    
                if needle_matches:
                    return occurence_index

        # If nothing works, return -1
        return -1
