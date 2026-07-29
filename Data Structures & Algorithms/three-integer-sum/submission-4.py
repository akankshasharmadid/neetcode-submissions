class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i,tar in enumerate(nums):
            check = set()
            comp = -tar
            for j, val in enumerate(nums):
                if i==j:
                    continue
                if comp - val in check:
                    triplet = sorted([tar, val, comp - val])
                    if triplet not in res:
                        res.append(triplet)
                check.add(val)
              
        return res