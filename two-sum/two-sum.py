class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num = {}
        for i,numy in enumerate(nums):
            Match = target - numy
            if Match in num : return[num[Match], i]
            #else:
            num[numy] = i
        return[]
        