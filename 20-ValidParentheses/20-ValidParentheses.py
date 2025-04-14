# Last updated: 4/14/2025, 7:20:29 AM
class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] #to store open brackets
        closeToOpen = {")" : "(" , "]" : "[" , "}" : "{" } #map close to open brackets

        #Iterate through string check if char is key in hashmap and perform actions ->pop from stack
        # if not add to stack because it is opening bracket
        for c in s:
            if c in closeToOpen:
                if stack and stack [-1] == closeToOpen[c]:
                    stack.pop() 
                else:
                    return False #{ instead of ( not matching with )
            else:
                stack.append(c)
        return True if not stack else False


        #Use a stack + hashmap
        #empty stack
        #Add to hash map my k;v ):(
        #Iterate through string
            #check if char in hashmap
                #if stack not empty and last element == map[key]:
                        #stack.pop()
                #else return False
            #if not key in map then add to stack ( meaning opening brack { (
        #return true if stack empty meaning all popped else false
                        
        