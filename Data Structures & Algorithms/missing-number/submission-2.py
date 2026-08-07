class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        #res = -1
        for i in range(0,len(nums)):
            if i in nums:
                pass
            else:
                return i
        return len(nums)