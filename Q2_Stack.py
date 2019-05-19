#Coding: Java/python/Node: Provide implementation of stack using array and list.
class Stack:
    def __init__(self):
        self._a = []

    def push(self, item):
        self._a.append(item)

    def pop(self):
        return self._a.pop()

    def isEmpty(self):
        return len(self._a) == 0



stack= Stack()
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
while not stack.isEmpty():
	print stack.pop();







