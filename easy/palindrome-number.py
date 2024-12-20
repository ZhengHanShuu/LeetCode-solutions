class Solution:
    def isPalindrome(self, x: int) -> bool:
        # check if the int is a negative number
        # check if the int is end with 0 but not equal to 0
        # return false if they are the above
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        # create a reverse_half to contain the number that reverse from x
        # initialize with 0
        reverse_half = 0
        # set up a loop to track to see if the reverse half is greater than
        # the first half of x
        # if x = 12321, first_iteration: reverse_half = 0 * 10 + 12321 % 10
        # reverse_half = 0 + 1 = 1
        # x = 12321 / 10 = 1232 // x > reverse_half
        # second_iteration: reverse_half = 1 * 10 + 1232 % 10 = 10 + 2 = 12
        # x = 1232 / 10 = 123 // x > reverse_half .... 123 > 12
        while x > reverse_half:
            reverse_half = reverse_half * 10 + x % 10
            x //= 10

        # once the loop end, we compare if the x == reverse_half
        # reverse_half // 10 is for the odd_length number, the middle number
        # does not affect, for example, 12321 => reverse_half = 123 // 10 = 12

        return x == reverse_half or x == reverse_half // 10


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # return false if the number is negative immediately
        if x < 0:
            return False

        # convert the int into string and convert it using slicing
        # return true if they are the same
        return str(x) == str(x)[::-1]