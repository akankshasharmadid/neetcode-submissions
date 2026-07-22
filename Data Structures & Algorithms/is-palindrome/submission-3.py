import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = re.sub(r'[^a-zA-Z0-9]','',s)
        start = 0
        end = len(t)-1
        while start<=end:
            if t[start]!=t[end]:
                return False
            start+=1
            end-=1

        return True