class Solution:
    def isPalindrome(self, s: str) -> bool:
        left=0  #at the start of the string #at the end of the string
        s=s.lower()
        s=''.join(c for c in s if c.isalnum())

        if len(s)==0:
            True
        right=len(s)-1
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False

        return True
            
            
