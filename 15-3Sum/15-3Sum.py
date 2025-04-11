# Last updated: 4/11/2025, 8:31:13 AM
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        #loop through
        for i, n in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                 continue
            #Two pointers where target is third num
            l, r =  i+1 , len(nums)-1
    
            #Iterate through array
            while l<r:
                currSum = n + nums[l]+ nums[r]
                if currSum > 0: #decrement right
                    r-=1
                elif currSum <0: #increment left
                    l+=1
                else: 
                    res.append([n ,nums[l], nums[r]])
                    l+=1
                    r-=1
                        #if  pointer  at duplicate incremement
                    while l<r and nums[l]== nums[l-1]:
                        l+=1
                         #if  pointer  at duplicate incremement
                    while l<r and nums[r]== nums[r+1]:
                        r-=1
        return res


        #constraints no duplicates so will need to skip values
        #list to hold result --> multiple set of triplets not just one
        #sort numbers easier to deal with duplicates [-4,-1,-1,0,1,2]
        #Loop through array
            #Loop with in use Two pointers 
                #left ptr make sure not duplicate
                #to check sum == to value at array
                #if == then add triplets in list
                    #increment left pointer if duplicate skip
                    #decrement right pointer if duplicate skip
                #if sum > 0 decrement right pointer
                #else: increment left pointer

    #time comple O(n2) 2 loops outer and one for two pointer
    #memory O(1) storing in list