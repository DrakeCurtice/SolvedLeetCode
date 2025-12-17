class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last_seen = {} 	# last_seen[ch] = index where that char was last seen
        left = 0 	# start of current contiguous substring
        best = 0 	# best length seen so far

        for right in range(len(s)): # right keeps moving index to the right
            ch = s[right]

            # if we have seen this char before AND it is inside current window then move left up one from where we last saw this character

            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1 

            last_seen[ch] = right

            window_len = right - left + 1

            if window_len > best: # make sure we grab the real longest length
                best = window_len

        return best

