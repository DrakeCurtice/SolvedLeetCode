class Solution:
    def climbStairs(self, n: int) -> int:
        
        # if odd, must have at least one 1 step, and must be odd number of 1 steps but can be even or odd number of 2 steps

        # if even, can be groups of two 1 steps, or groups of 2 steps. cannot be odd number of 1 steps. can be odd number of 2 steps

        if n == 1:
            return 1
        if n == 2:
            return 2
        if n == 3:
            return 3


        # ODD CASE
        if (n % 2 == 1 and n > 3):
            # All 2's, and a single 1 at any position
            twos_and_single_one_ways = math.floor(n/2 + 1)
            # All 1's, and a single two at any position
            ones_and_single_two_ways = n -1
            # All 1's is one way
            all_ones_ways = 1
            # Cannot use all two's if odd
            all_twos_ways = 0
            # Case with two or more 2's, but not all two's
            multi_two_ways = 0
            for twos in range(2, n // 2):
                ones = n - 2 * twos
                ways = ones + twos
                multi_two_ways += math.comb(ways, twos)

            # # Return all possible ways to climb up stairs if odd num of steps
            return (twos_and_single_one_ways + ones_and_single_two_ways + all_ones_ways + all_twos_ways + multi_two_ways)
            
            

        # EVEN CASE
        elif (n % 2 == 0):
            # All 1's, and a single two at any position
            ones_and_single_two_ways = n -1
            # All 1's is one way
            all_ones_ways = 1
            # All 2's is one way
            all_twos_ways = 1
            # Case with two or more 2's, but not all two's
            multi_two_ways = 0
            for twos in range(2, n // 2):
                ones = n - 2 * twos
                ways = ones + twos
                multi_two_ways += math.comb(ways, twos)
            
            # Return all possible ways to climb up stairs if even num of steps
            return (ones_and_single_two_ways + all_ones_ways + all_twos_ways + multi_two_ways)

            # Else, num of steps is 0, thus return 0
        else:
             return 0
