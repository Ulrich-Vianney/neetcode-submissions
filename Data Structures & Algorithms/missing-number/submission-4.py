class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        ens = set(nums)
        total = set([i for i in range(0,len(nums)+1)])
        diff = total.difference(ens)
        return diff.pop()