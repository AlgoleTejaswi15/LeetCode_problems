class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        ans=0
        l=set(allowed)
        for i in words:
            for j in i:
                if j not in l:
                    break
            else :
                ans+=1
        return ans



        