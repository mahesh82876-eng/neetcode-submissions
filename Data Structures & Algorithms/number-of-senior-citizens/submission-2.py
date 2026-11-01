class Solution:
    def countSeniors(self, details: List[str]) -> int:
        result=0
        for d in details:
            s=d[11] + d[12]
            if int(s)>60:
                result=result+1
            
        return result    