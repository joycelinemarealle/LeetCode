# Last updated: 4/10/2025, 7:21:30 AM
class Solution:
    def isPalindrome(self, s: str) -> bool:

        #Two pointers L, R = 0, len(s)-1
        #while L<R
            #while left not alpnum move left pointer to right
            #while right value not alphanum move right pointer to left
            #Compare left char and right, if not equal return faslse
            #after comparision move Left and right pointer
        #return True meets all checks

        l,r = 0, len(s)-1
        while l<r:
            #skip non alphanumeric char from the left
            while l<r and not s[l].isalnum():
                l+=1
            #skip non alphanumeric char from the right + not going out of bounds
            while r>l and not s[r].isalnum():
                r-=1
            #compare characters
            if s[l].lower()!= s[r].lower():
                return False
            l+=1
            r-=1
        return True
            
        #  l,r = 0, len(s)-1
        #  while l<r:
        #     #skip non alphanumeric char from the left
        #      while l<r and not self.alphaNum((s[l])):
        #         l+=1
        #     #skip non alphanumeric char from the right + not going out of bounds
        #      while r>l and not self.alphaNum(s[r]):
        #         r-=1
        #     #compare characters
        #      if s[l].lower()!= s[r].lower():
        #         return False
        #      l+=1
        #      r-=1
        #  return True

    def alphaNum(self,c):
    #returns true or false check if alpnuim
        return (ord('A') <= ord(c) <= ord('Z') or
         ord('a')<= ord(c) <= ord('z') or
        ord('0') <= ord(c) <= ord('9'))













        # #FIRST METHOD if can use built in
        #  newString = ""  #empty string
        # #Loop through string copy alpha numeric to new string. make sure in lowercase
        #  for c in s:
        #     if c.isalnum(): 
        #         newString += c.lower()
        #  return newString == newString[::-1] #returns true if forward == reverse

