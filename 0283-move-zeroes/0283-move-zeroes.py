class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zero_index = 0

        for num in nums:
            if num != 0:
                nums[non_zero_index] = num
                non_zero_index += 1

        for i in range(non_zero_index, len(nums)):
            nums[i] = 0
