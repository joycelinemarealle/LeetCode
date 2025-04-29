# Last updated: 4/29/2025, 10:12:42 AM
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0]* len(temperatures) #stores the # of days
        stack = [] #pair [[t,i], [t,i]....]

        #iterate through my temp array
        for i,t in enumerate(temperatures):
            #if stack not empty and t > than top stack value temp
            while stack and t > stack[-1][0]:
                #pop top value in stack then add  days = diff length to res array
                stackT, stackI = stack.pop()
                res[stackI] = (i - stackI)
            #if t < then top stack temp, then add t, i to stack
            stack.append([t,i])
        return res

        