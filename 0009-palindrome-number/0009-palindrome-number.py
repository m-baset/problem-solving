class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if len(x) == 1:
            return True
        is_palindrome = False
        for i in range(int(len(x)/2)):
            if x[i] == x[-(i+1)]:
                is_palindrome = True
            else:
                return False
        if is_palindrome:
            return True
