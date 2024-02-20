class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_list = list(s)
        t_list = list(t)
        for char in t_list:
            if char in s_list:
                s_list.remove(char)
            else:
                return char
        return " "
