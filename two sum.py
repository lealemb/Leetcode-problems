class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict={}
        for index, ele in enumerate(nums):
            if target- ele in dict:
                return dict[target- ele], index
            dict[ele]= index
