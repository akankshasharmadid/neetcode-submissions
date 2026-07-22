import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        t = re.sub(r'[^a-zA-Z0-9]','',s)
        print(s)
        print(t)
        if t == t[::-1]:
            return True
        return False