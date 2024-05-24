'''
Implement a last-in-first-out (LIFO) stack using only two queues. The implemented stack should support all the functions of a normal stack (push, top, pop, and empty).

Implement the MyStack class:

- push(x: int) -> None: Pushes element x to the top of the stack.
- pop() -> None Removes the element on the top of the stack and returns it.
- pop() -> None Returns the element on the top of the stack.
- empty() -> None Returns true if the stack is empty, false otherwise.
'''

class Queue:
    l = []

class MyStack:
    def push(self, x: int):
        Queue.l.append(x)
    def pop(self):
        return Queue.l.pop()
    def top(self):
        return Queue.l[-1]
    def empty(self):
        if Queue.l == []:
            return True
        else:
            return False


# Test        
mystack = MyStack()
mystack.push(1)
mystack.push(2)
print(mystack.top())    # Output: 2
print(mystack.pop())    # Output: 2
print(mystack.empty())  # Output: False
print(mystack.pop())    # Output: 1
print(mystack.empty())  # Output: True