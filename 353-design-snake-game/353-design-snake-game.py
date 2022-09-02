class Node:
    
    def __init__(self, val, n=None, p=None):
        
        self.val = val
        self.next = n
        self.prev = p

class SnakeGame:

    def __init__(self, width: int, height: int, food: List[List[int]]):
        
        self.head = self.rear = Node([0, 0])
        self.history = set()
        self.history.add((0, 0))
        self.food = food
        self.width = width
        self.height = height
        self.f_counter = 0
        
#         self.history = set()
#         self.width = width
#         self.height = height
        
#         self.position_history = [[0, 0]]
            
#         self.history.add((0, 0))
#         self.food = food
        
#         self.f_counter = 0
    
    def add_node(self, curr):
        
        if self.head == None:
            self.head = self.rear = Node(curr)
        else:
            temp = self.head
            new_node = Node(curr)
            new_node.next = temp
            temp.prev = new_node
            self.head = new_node
    
    def remove_node(self):
        
        if self.rear.prev == None:
            rem_val = self.rear.val
            self.head = self.rear = None
        else:
            rem_val = self.rear.val
            temp = self.rear.prev
            self.rear.prev = None
            self.rear = temp
            self.rear.next = None

           
        
        return rem_val
    
    def move(self, direction: str) -> int:
        
        curr = self.head.val.copy()
        
        if direction == "U":
            curr[0] -= 1
            
        elif direction == "D":
            curr[0] += 1
            
        elif direction == "L":
            curr[1] -= 1
            
        elif direction == "R":
            curr[1] += 1
        
        if curr[0] < 0 or curr[0] > self.height - 1 or curr[1] < 0 or curr[1] > self.width - 1:
            return -1
        
        
        self.add_node(curr)
        
        if len(self.food) > 0:
            if curr == self.food[0]:
                self.f_counter += 1
                self.food = self.food[1:]
                self.history.add((curr[0], curr[1]))
                return self.f_counter
        
        
        rem_val = self.remove_node()
        self.history.remove((rem_val[0], rem_val[1]))
        
        if (curr[0], curr[1]) in self.history:
            return -1
        self.history.add((curr[0], curr[1]))
        
        return self.f_counter
        
                
            
#         curr = self.position_history[0].copy()

#         if direction == "R":
#             curr[1] += 1

#         elif direction == "L":
#             curr[1] -= 1

#         elif direction == "U":
#             curr[0] -= 1

#         elif direction == "D":
#             curr[0] += 1


#         if curr[0] < 0 or curr[0] > self.height - 1 or curr[1] < 0 or curr[1] > self.width - 1:
#             return -1


#         if len(self.food) > 0:
#             if curr == self.food[0]:
#                 self.position_history.insert(0, curr)
#                 self.history.add((curr[0], curr[1]))
#                 self.food = self.food[1:]
#                 self.f_counter += 1
#                 return self.f_counter
        
#         rem = self.position_history[-1]
#         self.history.remove((rem[0], rem[1]))
#         self.position_history = self.position_history[:-1]
#         self.position_history.insert(0, curr)
        
#         if (curr[0], curr[1]) in self.history:
#             return -1
        
#         self.history.add((curr[0], curr[1]))
        
#         return self.f_counter

        
# Your SnakeGame object will be instantiated and called as such:
# obj = SnakeGame(width, height, food)
# param_1 = obj.move(direction)