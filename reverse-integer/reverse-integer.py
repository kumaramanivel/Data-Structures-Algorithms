class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if x == INT_MIN:
            return 0
        
        rev = 0
        sign = 1 if x >= 0 else -1
        x = abs(x)
        while x != 0:
            digit = x % 10
            if rev > (INT_MAX - digit)//10:
                return 0
            rev = rev * 10 + digit
            x = x // 10
        return rev * sign

#Time Complexity - O(n)
#Space Complexity - O(n)

# 123 % 10 = 3
# 123 / 10 = 12
# 12 % 10 = 2
# 12/10 = 1
# 1 % 10 = 1
# 1 / 10 = -

#Time Complexity - O(log x)
#Space Complexity - O(1)