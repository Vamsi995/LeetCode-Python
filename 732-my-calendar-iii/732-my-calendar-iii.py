from sortedcontainers import SortedDict

class MyCalendarThree:

    def __init__(self):
        
        self.bookings = SortedDict()

    def book(self, start: int, end: int) -> int:
        
        self.bookings[start] = 1 + self.bookings.get(start, 0)
        self.bookings[end] = -1 + self.bookings.get(end, 0)
        
        # k = sorted(self.bookings.items())
        
        count = 0
        res = 0
        
        for val in self.bookings.values():
            
            count += val
            res = max(count, res)    
            
        return res

# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)