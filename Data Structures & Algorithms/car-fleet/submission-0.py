class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #we create a pair first
        pair=[(p,s) for p,s in zip(position,speed)]
        pair.sort(reverse=True)

        fleets=1 #default number of fleets is set to 1 , now we iterate over the pairs 
        #the starting pair , will always be in front , making it the first fleet by default
        previoustime=(target-pair[0][0])/pair[0][1]
        for i in range(1,len(pair)):
            currCar=pair[i]  # start with the index 1 pair , 1-ith car
            currTime=(target-currCar[0])/currCar[1]   #time = distance/speeeed

            if previoustime<currTime:   #previosu time is car 0 the closest , if the car behind is taking more time , than itself , it wont reach at the same time , hence belonging to a different fleet
                fleets+=1
                previoustime=currTime
        
        return fleets

