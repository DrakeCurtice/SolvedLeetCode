class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        # For each character, count # of times it appears in each word
        # For each character that appears in all words, take the minimum count across all words
        # Print those minimum counts (greatest common characters)
        
        # Count letters in first word
        common_counts = {}
        for ch in words[0]:
            if ch in common_counts:
                common_counts[ch] += 1 # If already seen letter than say we saw another (+1 count)
            else:
                common_counts[ch] = 1 # Else, say we saw the number (count is 1)
            

        
        # For each next word, count its letters and take minimums
        for word in words[1:]:  # For each word not first, ...
            current_counts = {}            
            for ch in word:     # Check each character of that word
                if ch in current_counts: # If char already seen, add 1, otherwise if never seen then show it was seen (=1)
                    current_counts[ch] = current_counts[ch] + 1
                else:
                    current_counts[ch] = 1 

            
            # Update common_counts to only keep letters that are shared between all of the words and take minimum count
            new_common = {}
            for ch in common_counts:
                if ch in current_counts:
                    new_common[ch] = min(common_counts[ch], current_counts[ch])
                
            common_counts = new_common

        # Output these letters 
        result = []
        for ch in common_counts:
            
            for k in range(common_counts[ch]):
                result.append(ch)

        return result



            
        