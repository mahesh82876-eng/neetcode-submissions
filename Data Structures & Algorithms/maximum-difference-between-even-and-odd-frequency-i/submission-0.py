
class Solution:
    def maxDifference(self, s: str) -> int:
        freq = {}

        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        odd = []
        even = []

        for count in freq.values():
            if count % 2 == 1:
                odd.append(count)
            else:
                even.append(count)

        return max(odd) - min(even)

