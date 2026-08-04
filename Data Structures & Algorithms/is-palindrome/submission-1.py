class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower() #converting all the characters to lowercase 
        s=''.join(c for c in s if c.isalnum()) #removes all characters that are not digits or numbers
        #finished preprocessing the text
        left=0
        right=len(s)-1 #created two pointers , one starting from the left the other starting from right
        if len(s)==0:
            return True #as empty strings are a palindrome of itself 

        #start the while loop condition untill there is no crossover of the pointers in the traversal
        while left<=right:
            if s[left]==s[right]: #its still a palindrome , keep checking
                left+=1
                right-=1
            
            else:
                return False
        
        return True

        

        

        