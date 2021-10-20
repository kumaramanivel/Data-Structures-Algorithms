class Solution:
    def reverseWords(self, s: str) -> str:
        t = s.split()
        right = len(t) - 1
        left = 0
        while left < right:
            t[left], t[right] = t[right], t[left]
            left += 1
            right -= 1
        return ' '.join(t)        