# Last updated: 4/28/2025, 10:05:55 AM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Iterate through array
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop()) #order does not matter
            elif c == "-":
                a,b = stack.pop(), stack.pop() #order matters start with older stack value b
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                 a,b = stack.pop(), stack.pop()
                 stack.append(int(b/a)) #truncate towards zero
            else:
                stack .append(int(c)) # add integers into stack
        return stack[0]
        

         # Iterate through array
        # add char --> conver to integers into stack
        # if not integers perform operations --> 4 scenarios + - / *
            #pop twice then perform operation --> the add the final result to stack
            #when - or / I start with value in stack longer/older value. so popped second
            # round to zero int(b/a)

            #Time Big O(n) nof elements iterating through array, insert to stack max n
            #Memory Big O (n) size of stack