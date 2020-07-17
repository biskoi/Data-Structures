from singly_linked_list import LinkedList 

"""
A queue is a data structure whose primary purpose is to store and
return elements in First In First Out order. 

1. Implement the Queue class using an array as the underlying storage structure.
   Make sure the Queue tests pass.
2. Re-implement the Queue class, this time using the linked list implementation
   as the underlying storage structure.
   Make sure the Queue tests pass.
3. What is the difference between using an array vs. a linked list when 
   implementing a Queue?
   
Stretch: What if you could only use instances of your Stack class to implement the Queue?
         What would that look like? How many Stacks would you need? Try it!
"""
# class Queue:
#     def __init__(self):
#         self.size = 0
#         self.storage = []
    
#     def __len__(self):
#         return len(self.storage)

#     def enqueue(self, value):
#         self.storage.append(value)

#     def dequeue(self):
#         if len(self.storage) != 0:
#             return self.storage.pop(0)
#         else:
#             return None

class Queue:
    def __init__(self):
        self.size = 0
        self.storage = LinkedList()

    def __len__(self):
        if self.storage.head == None:
            return 0
        elif self.storage.head:
            current = self.storage.head
            length = 0
            while current:
                length += 1
                current = current.next_node if current.next_node else False
            return length

    def enqueue(self, val):
        self.storage.add_to_tail(val)
        self.size += 1

    def dequeue(self):
        current_head = self.storage.head
        # if self.storage.head is not None:
        #     self.storage.head = self.storage.head.get_next()
        #     return current_head.get_value()
        # else:
        #     self.storage.head = None
        #     return current_head.get_value()
        self.size -= 1
        return self.storage.remove_head()