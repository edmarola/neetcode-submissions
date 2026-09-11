class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return sorted(s) == sorted(t)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        outputMap = {}
        for word in strs:
            sortedWord = "".join(sorted(word))
            if sortedWord in outputMap:
                output[outputMap[sortedWord]].append(word)
            else:
                output.append([word])
                outputMap[sortedWord] = len(output) - 1
        return output
                
            
            
        