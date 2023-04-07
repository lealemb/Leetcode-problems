class Solution:
    def hammingWeight(self, n: int):
       return bin(n).count('1')
