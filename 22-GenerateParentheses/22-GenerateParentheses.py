# Last updated: 4/28/2025, 2:04:43 PM
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        #global
        stack = [] #hold ()
        res = [] #list of valid combi
        def backTracking (openN, closeN):
            #if open count and close count = n , then return the combinations of valid parenthisi
            #base case
            if openN == closeN == n:
                res.append("".join(stack)) #take every character in stack in a empty string
            # only add open parenthisis if openN < n ->backtrack and increase open count
            if openN < n:
                stack.append("(")
                backTracking(openN+1, closeN)
                stack.pop()
            #only add close parenthisis if closeN < open> -> backtrack + incrwase close count
            if closeN < openN:
                stack.append(")")     
                backTracking(openN, closeN+1)
                stack.pop() #clean up stack , update by popping what we just added. we have single stack var
        backTracking(0,0)
        return res






        #Backtracking and recursion
        #if open count and close count = n , then return the combinations of valid parenthisi
        # only add open parenthisis if openN < n ->backtrack and increase open count
         #only add close parenthisis if closeN < open> -> backtrack + incrwase close count
     
        #Only allwoed to add open parenthesis if 
        # 1)Can start with open ( if open limit not reached
        # 2)close count  < open count
        #if open count and close count = n , then return the combinations of valid parenthisi
            # if openN < n backtrack and incease opencount
            #if closeN < open> add close parenthis      