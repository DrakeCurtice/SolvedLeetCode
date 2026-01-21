class Solution:
    def hammingWeight(self, n: int) -> int:
        # Thought process
        # positive integer n
        # return number of SET BITS in its binary representation
        # A set bit refers to a bit in the binary representation of a number that has a value of 1
        # So figure out its binary number
        # then loop through to count the occurences of 1's

        # Find binary representation of integer value
        binary_value = bin(n)[2:] # Skip past the prefix 0b

        # Calculate occurences of 1's
        hamming_weight = 0
        for i in binary_value:
            if i == '1':
                hamming_weight += 1
            else:
                continue


        return hamming_weight

