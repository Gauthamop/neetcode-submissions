class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1=len(word1)-1
        n2=len(word2)-1
        newword=""
        i=0
        if n1>n2:  #here length of n1 is greater than n2
            while i<=n1:  #cause n1 is bigger
                if i<=n2:  #till the smaller n2 is done 
                    newword+=word1[i]
                    newword+=word2[i]
                else:
                    newword+=word1[i]  #after n2 is done

                i+=1


        else: #here legnth of n2 is bigger than n1
            while i<=n2:
                if i<=n1:
                    newword+=word1[i]
                    newword+=word2[i]
                else:
                    newword+=word2[i]

                i+=1
        return newword





        