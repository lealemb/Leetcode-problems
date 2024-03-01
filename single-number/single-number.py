class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        i = 0
        for num in nums:
            i ^= num
        
        return i