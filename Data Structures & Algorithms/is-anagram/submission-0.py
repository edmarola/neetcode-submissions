class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        n = len(s)
        m = len(t)
        if n != m:
            return False
        letters = {}
        for l in s:
            if l in letters:
                letters[l] = letters[l] + 1
            else:
                letters[l] = 1
        for l in t:
            if l in letters:
                if letters[l] == 1:
                    letters.pop(l)
                else:
                    letters[l] = letters[l] - 1
            else:
                return False
        return len(letters) == 0



        
        