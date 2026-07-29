class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res = 0 
        for i in nums:
            if i-1 not in nums:
                temp = 0
                val = i
                while val in s:
                    temp = temp+1
                    val = val+1

                res = max(res,temp)
        return res