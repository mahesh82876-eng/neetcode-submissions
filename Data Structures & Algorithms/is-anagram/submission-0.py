class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first_name=sorted(s)
        second_name=sorted(t)
        if first_name==second_name:
            return True
        else:
            return False