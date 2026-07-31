class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        left = 0
        right = 0
        current = set()
        while left <= right and right<len(s):
            while right<len(s) and s[right] not in current:
                current.add(s[right])
                right+=1
                
                l = max(right-left,l)
            current.remove(s[left])
            left+=1
        return l

                