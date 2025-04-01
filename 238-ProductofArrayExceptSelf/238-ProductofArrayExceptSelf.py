# Last updated: 4/1/2025, 6:59:24 PM
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
        res = [1]*len(nums) #initialize output array
        #define prefix values before current index
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix =1
        #multiply postfix with value in res[]
        for i in range(len(nums)-1,-1,-1): #from end to beginning 
            res[i] *= postfix
            postfix *= nums[i]
        return res

#Use prefix and suffix
        #Loop left -> right
            #continue update the prefix
               #store products before and after current index
        #loop right --> left
            #continue update the prefix
            #in res arr store multiple prefix + suffix @ position
        #return result array
        
# #Use prefix and suffix
#         res = [1]*len(nums)
#         #Prefix
#         #Loop nums to set prefix products

#         #initialize
#         prefix = 1
#         for i in range (lens(nums)+1):
#             res[i]= prefix
#             #update prefix
#             prefix *= nums[i]

#         #Suffix
#         #loop through nums from right to left
#         postfix = 1
#         for i in range (len(nums)-1, -1, -1):
#             #add first product in res array
#              res[i] *= postfix
            
#              postfix *= num[i] #update postfix for next index
         
           
           







        