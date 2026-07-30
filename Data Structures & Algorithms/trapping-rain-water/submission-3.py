class Solution:
    def trap(self, height: List[int]) -> int:

        max_left = [height[0]]*len(height)
        max_right = [height[-1]]*len(height)
        for i,val in enumerate(height):
            if i != 0:
                max_left[i] = max(max_left[i-1],val)
        rev = height[::-1]
        for i,val in enumerate(rev):
            if i!=0:
                max_right[i] = max(max_right[i-1],val)
        max_right = max_right[::-1]
        res = 0
        for i,val in enumerate(height):
            res += max(0,min(max_right[i],max_left[i])-height[i])
        return res
