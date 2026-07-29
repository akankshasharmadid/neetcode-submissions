class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        for i,tar in enumerate(nums):
            temp = [tar]
            check = set()
            add = 0
            comp = -tar
            for r, val in enumerate(nums):
                if i == r:
                    continue

                if comp - val in check:
                    triplet = sorted([tar, val, comp - val])
                    if triplet not in res:
                        res.append(triplet)

                check.add(val)
        return res
                
                

