# Last updated: 4/11/2025, 7:45:12 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #pointer
        left = 0
        right = len(numbers)-1

        #loop through array
        while left < right: 
            print (left,right)
            _sum = numbers[left] + numbers[right]
            #compare the sum to target
            if _sum == target:
                return [left+1,right+1] 
            elif _sum > target:
                right -=1
            else:
                left +=1
        return [] #if there will no indexes 
        
         #constraints index >=1 <= length of array
        #Two pointer left from index1 and right from length of array
        #Loop through array l<r
        #check sum of two value if  equal to target return the index
        #if sum < target, increment my left pointer
        #else: decrement right pointer
        #time complexity Big O(n) number of elemenet
        #memory constant space O(1) storing indexes in an array
        
       
        