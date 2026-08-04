class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
         #as there are 26 letters in the alphabet
        #traverse every word , in the list of different words
        wordinfohashmap=defaultdict(list)
        for word in strs:
            count=[0]*26 #for every word initilize a new count array
            for characters in word:
                count[ord(characters)-ord('a')]+=1  #saving the entire word , in an count array to have its info

            
            wordinfohashmap[tuple(count)].append(word)
            #then moves onto the next word 

        return list(wordinfohashmap.values())