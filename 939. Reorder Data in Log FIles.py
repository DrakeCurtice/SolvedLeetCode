class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        # Given array of logs.
        # Each log is space delimited string of words
        # First word is idenftifier

        # 2 types of logs
        # Letter logs (all words are only lower case english letters) (other than identifier)
        # Digit logs (all words are digits) (other than identifier)

        # Reorder the logs such that:
        # Letter logs come before ALL digit logs
        # Letter logs are sorted lexicographically by contents .sort()
        # If contents are same then sort lexicographically by identifiers

        
        digit_logs = []
        letter_logs = []
     
        for log in logs:
            identifier, rest = log.split(" ", 1)

            if rest[0].isdigit():
                digit_logs.append(log)
                
            else:
                letter_logs.append(log)

        letter_logs.sort(key=lambda s: (s.split(" ", 1)[1], s.split(" ", 1)[0]))

        letter_logs.extend(digit_logs)

        return letter_logs


          