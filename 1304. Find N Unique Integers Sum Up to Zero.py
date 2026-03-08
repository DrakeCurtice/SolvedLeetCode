class Solution:
    def sumZero(self, n: int) -> List[int]:
        # to make it easy, for n
        # make array with n+1, n+2, .... n+(n-1) and finally subtract that total value 
        # so with n = 6 example
        # into array do 6, 7, 8, 9, 10, -40
        # keep track of total value in array at each step
        # 6 = 6      7 =13        8 = 21       9= 30         10 =  40        subtract total value = 40-40 = 0

        unique_integers = []
        value_to_subtract = 0
        for i in range(n, n + (n - 1)):
            value_to_subtract -= i
            unique_integers.append(i)

        unique_integers.append(value_to_subtract)

        return(unique_integers)

