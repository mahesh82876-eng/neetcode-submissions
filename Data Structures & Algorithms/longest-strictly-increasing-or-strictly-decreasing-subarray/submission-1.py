class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increasing=1
        decreasing=1
        largest =1
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                increasing=increasing+1
                decreasing=1
            elif nums[i]<nums[i-1]:
                increasing=1
                decreasing=decreasing+1
            else:
                increasing=1
                decreasing=1
            largest=max(largest,increasing,decreasing)
        return largest

