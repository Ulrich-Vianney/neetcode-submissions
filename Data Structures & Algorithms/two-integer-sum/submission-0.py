class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
            dico={}
            for j in range(len(nums)):
                if nums[j] in dico:
                    return [dico[nums[j]],j]
                else:
                    dico[target-nums[j]]=j