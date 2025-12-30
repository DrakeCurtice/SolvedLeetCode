class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # We have to loop through s and store the index in t where each character of s is matched, 
        
        # then make sure each next match happens after the previous one (in increasing index order)
        t_index = 0
        matched_indices = []

        for ch in s:
            # look for s's ch in t
            while t_index < len(t) and t[t_index] != ch:
                t_index += 1

            # could not find s's character in t
            if t_index == len(t):
                return False

            # found match at t_index
            matched_indices.append(t_index)

            t_index += 1

        return True

