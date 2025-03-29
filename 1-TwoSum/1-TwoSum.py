# Last updated: 3/29/2025, 10:21:34 AM
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #value:indic3

        #loop through the array and i,num
        for i, num in enumerate(nums):
            diff = target-num

            #check if the complement is in map
            if diff in prevMap:
                return [prevMap[diff],i]
            #if not add pair to map
            prevMap[num] = i
        return [] #if no pair found
      

        #Brute force
        #Loop through nums
        #check for num[i]
         #nested loop to check for nums[j]
          #if nums[i]+ nums[j] == targets:
            #return [i,j]
        #return []
        
        # for i in range (len(nums)):
        #     for j in range (i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]
        # return []

        #time complexity O(n2)
        #memory O(1)


        
        
    #     #Sort array
    #     nums.sort()
        
    #     #pointers
    #     left = 0
    #     right = len(nums)-1

    #     #Loop throught the array
    #     while left < right: 
    #         #Compare sum
    #         sum_ =nums[left] + nums[right]
    #         if  sum_ == target:
    #             return [left, right] #return indice is sum = target
    #         if sum_ > target:
    #             right -=1 #move right pointer to left to descres sum_
    #         else:
    #             left +=1 #move left pointer to right to increase sum_
        
    #    #solution
    #    #store in hashmpa one value
    #    #check if target - num already in hashmap
    #     #if not add
    #     #if yes return [value, value of indice] 


#Solution
#edge case
#Sorted valuesarray 
#Two pointers one starting from the left and another from the right
#add two elements with pointers as indices. Compare the sum to target
      #if sum == target , return [left, right]
    #if sum > target , remove the right pointer to the left
    #else remove the left pointer to the right
#Time complexity sorting O(nlogn) + O(n)
#Memory complexity O(1) return array with 2 incies, 