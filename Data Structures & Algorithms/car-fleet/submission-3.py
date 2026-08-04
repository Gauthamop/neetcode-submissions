class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #car fleet question
        pairs=[(p,s) for p,s in zip(position,speed)]
        #created an array of position/speed pairs pairs=[(p1,s1),(p2,s2),(p3,s3),...........(pn,sn)]
        #sort the pairs in decreasing order , such that the first car at index 0 , is the car closest to the target
        pairs.sort(reverse=True) #descending order

        #run a loop to go through the entire array 
        benchmarktime=(target-pairs[0][0])/pairs[0][1]
        fleets=1
        for i in range(1,len(pairs)):
            currentime=(target-pairs[i][0])/pairs[i][1]
            if currentime>benchmarktime:
                fleets+=1  # meaning that the car , spends more time than the current leading car , hence forming a new car fleet
                #if the car reaches the target at the same time , its part of the same fleet 
                benchmarktime=currentime
        
        return fleets

            

        