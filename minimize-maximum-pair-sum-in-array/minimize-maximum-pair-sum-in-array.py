class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max([value+nums[-index] for index, value in enumerate(nums[:len(nums)//2], 1)])
        