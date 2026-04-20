import math

class TreeNode:
    def __init__(self, val =0, next= None, min = math.inf):
        self.val = val
        self.next = next
        self.min = min

class MinStack:
    def __init__(self):
        self.dummy = TreeNode()

    def push(self, val: int) -> None:
        min_value = math.inf
        if self.dummy.next is not None:
            min_value = self.dummy.next.min
            
        if val < min_value:
            min_value = val

        new_node = TreeNode(val, self.dummy.next, min_value)
        self.dummy.next = new_node
        

    def pop(self) -> None:
        self.dummy.next = self.dummy.next.next

    def top(self) -> int:
        return self.dummy.next.val

    def getMin(self) -> int:
        return self.dummy.next.min


        
