class MyCalendarTwo(object):

    def __init__(self):
        self.lst =[]

    
    def book (self, start, end):
        self.lst.append((start, 1))
        self.lst.append((end, -1))
        
        self.lst.sort()
        overlaps = 0
        for b in self.lst:
            overlaps+=b[1]
            if overlaps >2:
                self.lst.remove((start, 1))
                self.lst.remove((end, -1))
                return False
        return True
        

# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)