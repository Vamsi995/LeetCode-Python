class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        ans = collections.defaultdict(list)
        
        for st in strs:
            
            ans[''.join(sorted(st))].append(st)
        
        return ans.values()
        