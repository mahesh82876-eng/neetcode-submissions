class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            distaint_flage=True
            for j in range(len(arr)):
                if i==j:
                    continue
                if arr[i]==arr[j]:
                    distaint_flage=False
                    break
            if distaint_flage:
                k -=1
                if k==0:
                    return arr[i]
        return ""
