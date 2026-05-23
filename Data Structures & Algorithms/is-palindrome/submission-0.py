class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = list(s)
        l = 0
        r = len(a) - 1
        while l < r:
            if a[l].isalnum() and a[r].isalnum():
                if a[l] == a[r]:
                    l += 1
                    r -= 1
                else :
                    return False
            if not a[l].isalnum():
                l += 1
            if not a[r].isalnum():
                r-= 1
        
        return True