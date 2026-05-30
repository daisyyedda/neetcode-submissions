class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        l = 0
        r = n - 1
        while l < r:
            while l < r and l < n:
                if s[l].isalnum() == False or s[l] == ' ': 
                    l += 1
                else:
                    break
            while l < r and r > 0:
                if s[r].isalnum() == False or s[r] == ' ': 
                    r -= 1
                else: 
                    break
            if s[l].lower() != s[r].lower(): return False
            l += 1
            r -= 1
        return True