class TimeMap:

    def __init__(self):
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            self.map[key] = []
        self.map[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        
        
        if key not in self.map:
            return ""
        
        else:
            
            nums = self.map[key]
            
            l, r = 0, len(nums)-1
            
            while l <= r:
                
                mid = (l+r)//2
                
                if nums[mid][1] == timestamp:
                    return nums[mid][0]
                
                if nums[mid][1] > timestamp:
                    r = mid - 1
                
                if nums[mid][1] < timestamp:
                    l = mid+1
            
            return nums[l-1][0] if l >= 1 else ""
            
# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)