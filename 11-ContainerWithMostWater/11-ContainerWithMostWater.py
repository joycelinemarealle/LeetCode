# Last updated: 4/12/2025, 9:27:11 AM
class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0 #cannot have negative

        #pointer
        l,r = 0, len(height) -1

        #loop through array
        while l < r:
            area = (r-l)* min(height[l],height[r])
            max_area = max(max_area, area)

            #move pointer
            if height[l]< height[r]:
                l+=1
            else: #if r>=l
                r-=1

        return max_area





        #Two pointer algo
        #Left and right moving through height array max width
        #Loop through array
            #calcul area of rec ( width and min (h) and update max area
            #if l < r incrrement l pointer
            #else decrement r pointer (r>=l)
        #return res
        
        #time cople Big O(n) n is size of array
        #memory complexity big O(1) storing result int