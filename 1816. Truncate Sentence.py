class Solution:
    def truncateSentence(self, s: str, k: int) -> str:

        kept = []
        words = s.split()
        count = 0
        for w in words:
            if count == k:
                break
            kept.append(w)
            count += 1

        return " ".join(kept)
        
        
