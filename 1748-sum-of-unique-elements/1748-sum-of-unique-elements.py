class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        data = []
        for i in nums:
            if nums.count(i) == 1:
                data.append(i)
        return sum(data)