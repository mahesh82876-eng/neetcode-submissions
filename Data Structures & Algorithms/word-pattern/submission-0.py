class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words=s.split(" ")
        if len(pattern) !=len(words):
            return False
        
        chartowords={}
        wordstochar={}

        for c,w in zip(pattern,words):
            if c in chartowords and chartowords[c] !=w:
                return False
            if w in wordstochar and wordstochar[w] !=c:
                return False
            chartowords[c]=w
            wordstochar[w]=c
        return True
