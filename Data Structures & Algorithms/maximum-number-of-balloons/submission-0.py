class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counttext=Counter(text)
        balloon=Counter("balloon")
        res=len(text)
        for c in balloon:
            res=min(res,counttext[c]//balloon[c])
        return res