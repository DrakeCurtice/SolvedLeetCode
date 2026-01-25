import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # convert to lowercase
        # remove ALL non alphanumeric characters including space
        # check if same forwards and backwards
        clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
        if clean_s == clean_s[::-1]:
            return True
        else:
            return False

