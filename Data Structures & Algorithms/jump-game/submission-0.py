class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)
        goal_ptr = n-1

        for i in range(n-1, -1, -1):
            if i+nums[i]>=goal_ptr:
                goal_ptr = i
        
        return True if goal_ptr==0 else False

        