class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        ans1=0
        ans2=0
        for i in range(len(nums)):
            if i%2==0:
                ans1+=nums[i]
            else:
                ans2+=nums[i]
        ans=ans1-ans2
        return ans


        