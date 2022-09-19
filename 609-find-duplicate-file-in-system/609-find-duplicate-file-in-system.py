class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        
        ans = []
        arr = []
        hash_map = {}

        for string in paths:
            arr = string.split(" ")
            directory = arr[0]
        
            files = []
        
            for string in arr[1:]:
                temp = string.split("(")
                file_name = temp[0]
                file_content = temp[1]
            
                hash_map[file_content] = [directory + "/" + file_name] + hash_map.get(file_content, [])
        
        for content, files in hash_map.items():
            
            if len(files) > 1:
                ans.append(files)
        
        
        
        return ans
                
        
        
        
        
        
        