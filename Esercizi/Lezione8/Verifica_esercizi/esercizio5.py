'''
Given the head of a singly linked list, return true if it is a palindrome. 
Model the Node and Linked List concepts using classes. 
'''

class Node:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = Node(val)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(val)

def is_palindrome(head: Node) -> bool:
    l = []
    current_node = head
    while current_node is not None:
        l.append(current_node.val)
        current_node = current_node.next
    return l == l[::-1]