class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count=1
        for i in nums:
            if nums[i] and nums[i+1]==1:
                count+=1
            elif nums[i]==1 and nums[i+1]==0:
                break
            
        return count