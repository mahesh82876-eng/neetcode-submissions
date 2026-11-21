
class Solution:
    def findLucky(self, arr):
        for num in sorted(set(arr), reverse=True):
            if arr.count(num) == num:
                return num

        return -1
