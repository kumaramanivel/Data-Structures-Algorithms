class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nummap = set(nums)
        n = len (nums) + 1
        for number in range (n) :
            if number not in nummap:
                return number
        