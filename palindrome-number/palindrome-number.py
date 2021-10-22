class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        else:
            x_str = str(x)
            x_len = len(x_str)
            for i in range(x_len//2):
                if x_str[i] != x_str[x_len-i-1]:
                    return False
            return True
        