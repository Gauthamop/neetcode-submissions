class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c for c in s if c.isalnum())  #remove all characters that is not a string or digit  (alpha numeric),
        s=s.lower() #convert to all lowercases
        left=0
        right=len(s)-1 #last index #common mistake dont take -1 as the top/end value
        if len(s)==0:
            return True #as empty string is also an palindrome
        while left<=right:
            if s[left]==s[right]:
                left+=1
                right-=1
            else:
                return False
        
        return True


        