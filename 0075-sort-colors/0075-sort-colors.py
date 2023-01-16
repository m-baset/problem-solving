class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = [0,0,0]
        for i in nums:
            colors[i] += 1        

        for i in range(len(nums)):
            if colors[0] > 0:
                nums[i] = 0
                colors[0] -= 1

            elif colors[1] > 0:
                nums[i] = 1
                colors[1] -= 1

            elif colors[2] > 0:
                nums[i] = 2
                colors[2] -= 1

            