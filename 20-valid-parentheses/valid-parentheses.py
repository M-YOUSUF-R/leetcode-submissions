class Stack:
    def __init__(self):
        self.list = []
        self.top = -1
    def push(self,val):
        self.list.append(val)
        self.top += 1
    def pop(self):
        self.top -= 1

        return self.list.pop()

class Solution:
    def isValid(self, s: str) -> bool:
        stack = Stack()
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:
                top_element = stack.pop() if stack.top != -1 else '#'
                if mapping[char] != top_element :
                    return False
            else:
                stack.push(char)
        return len(stack.list) == 0
            
                
        