# Last updated: 3/29/2025, 10:24:22 AM
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #create empty Hashet
        seen = set ()
        #loop through array to insert each num set
        #check if it dexists and if not add to Hashset, if exists return true
        for num in nums:
            if num in seen:
                return True
                #add to set
            seen.add(num)
        #if after looping through all nums,  no duplicate return false
        return False
        
     
    #time complexity O(n) n number of elements
    #memory O(n) using a set worst case scenario all elements seen


     #edge cases if array empty
     #Loop through the array and 
        #check if element in maps if yes return true
    #if adfter loop reutnr false if all numbers distincif not add it return false and add it
       