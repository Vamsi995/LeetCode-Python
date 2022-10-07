class MyCalendarTwo:

    def __init__(self):
        
        self.bookings = []

    def book(self, start: int, end: int) -> bool:
        
        # self.bookings[start] = 1 + self.bookings.get(start, 0)
        # self.bookings[end] = -1 + self.bookings.get(end, 0)
        self.bookings.append((start, 1))
        self.bookings.append((end, -1))
        count = 0
        # print(start, end, self.bookings[(start, (start, end))])
        self.bookings.sort()
        
        for c, val in self.bookings:
                
            count += val
            
            if count >= 3:
                self.bookings.remove((start, 1))
                self.bookings.remove((end, -1))
                
#                 if self.bookings[start] == 0:
#                     self.bookings.pop(start)
                    # self.bookings.pop(end)
                
                return False
        
        
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)