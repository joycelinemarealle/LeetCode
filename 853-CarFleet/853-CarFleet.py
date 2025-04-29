# Last updated: 4/29/2025, 11:37:09 AM
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
       #Create a 2D array(arrray of pairs) from p and s uing zip
        pair = [[p,s] for p, s in zip(position, speed)]
      
        #initialization fleets , curTime
        fleets = 0
        curTime = 0

        #Iterate through  pair array in sorted in reverse
        #pair.sort(reverse=True)
        for p,s in sorted(pair)[::-1]:
        #compare destination time if curTime < desintatio time then fleet count increase
            destination_time = (target-p)/s
            if curTime < destination_time: #means cars collide and become fleet
                fleets +=1
                curTime = destination_time
       
        #return fleets
        return fleets
       
      

      
        #Create a 2D array from p and s uing zip
        #initialization fleets , curTime

        #Iterate through new pair in sorted in reverse
        #compare destination time if curTime < desintatio time then fleet count increase
        #curTime= destination time
        #return fleets
        