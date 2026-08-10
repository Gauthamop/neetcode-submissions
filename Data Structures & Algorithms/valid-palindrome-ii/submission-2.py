class Solution:
    def validPalindrome(self, s: str) -> bool:
        #valid palindrome question 2
        left=0 #starting at the start of the array
        right=len(s)-1 #starting at the end 
        def is_palindrome(left,right):
            while left<=right: #can be equal but can never cross
                if s[left]==s[right]:
                    left+=1
                    right-=1
                else:
                    return False

            return True              #this function returns if characters from a left index to a right index , form a palindrome


        #now we traverse this string asnormal 
        while left<=right:
            if s[left]!=s[right]: #when its not equal
                return (is_palindrome(left+1,right) or is_palindrome(left,right-1))
            
            left+=1
            right-=1

        return True


                


        

        