class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        f_pro = [1] * len(nums)
        b_pro = [1] * len(nums)
        for i,val in enumerate(nums):
            # [1  ,1  ,2 ,8]
            # [48 ,24 ,6 ,1]
            # [48 ,24 ,12 ,8]
            if i == 0:
                continue
            else:
                f_pro[i] = f_pro[i-1]*nums[i-1]
        n = nums[::-1]
        for i,val in enumerate(n):
            # [1  ,1  ,2 ,8]
            # [48 ,24 ,6 ,1]
            # [48 ,24 ,12 ,8]
            if i == 0:
                continue
            else:
                b_pro[i] = b_pro[i-1]*n[i-1]
 
        b_pro = b_pro[::-1]
        res = []
        for i in range(len(b_pro)):
            res.append(f_pro[i]*b_pro[i])
        return res