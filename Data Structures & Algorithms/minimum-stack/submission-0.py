import math

class TreeNode:
    def __init__(self, val =0, next= None):
        self.val = val
        self.next = next

class MinStack:
    def __init__(self):
        self.dummy = TreeNode()

    def push(self, val: int) -> None:
        new_node = TreeNode(val, self.dummy.next)
        self.dummy.next = new_node
        

    def pop(self) -> None:
        self.dummy.next = self.dummy.next.next

    def top(self) -> int:
        return self.dummy.next.val

    def getMin(self) -> int:
        # Need to be O(1)
        current = self.dummy.next
        smallest = math.inf
        while current is not None:
            if current.val < smallest:
                smallest = current.val

            current = current.next

        return smallest


        
