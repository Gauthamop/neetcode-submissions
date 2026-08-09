
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        n1 = len(word1) - 1
        n2 = len(word2) - 1

        newword = ""
        i = 0

        if n1 < n2:
            while i <= n2:
                if i <= n1:
                    newword += word1[i]
                    newword += word2[i]
                else:
                    newword += word2[i]

                i += 1

        else:
            while i <= n1:
                if i <= n2:
                    newword += word1[i]
                    newword += word2[i]
                else:
                    newword += word1[i]

                i += 1

        return newword
