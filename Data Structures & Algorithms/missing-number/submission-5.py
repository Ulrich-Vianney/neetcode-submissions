class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        total = [i for i in range(0,len(nums)+1)]
        sum_tot=sum(total)
        sum_par=sum(nums)
        return sum_tot-sum_par