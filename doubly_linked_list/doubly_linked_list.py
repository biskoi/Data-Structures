"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #create instance of listnode with val
        new_ln = ListNode(value)
        #increment dll length attr
        if self.length == 0:
            self.head = new_ln
            self.tail = new_ln
        else: 
            old_head = self.head
            self.head = new_ln
            self.head.next = old_head
            old_head.prev = self.head
        # dll is empty
            # head and tail = new ln
        # if not empty
            #set new node's next to current head
            #set head's prev to new node
            #set head to new node
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        #store value of the head
        #decrement length of dll
        #delete head
            #if there is a next
                #set next as new head
                #set next's prev as none
            #if not
                #set current to none
        if self.length == 0:
            return None
        else:
            removed_head = self.head
            if self.head.next:
                self.head = self.head.next
                self.head.prev = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
            return removed_head.value
        

            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        new_tail = ListNode(value, self.tail)
        if self.length == 0:
            self.head = new_tail
            self.tail = new_tail
        else: 
            self.tail.next = new_tail
            self.tail = new_tail
        self.length += 1
            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        if self.length == 0:
            return None
        else:
            removed_tail = self.tail
            if self.tail.prev is not None:
                self.tail = self.tail.prev
                self.tail.next = None
            else:
                self.head = None
                self.tail = None
            self.length -= 1
        return removed_tail.value
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        # current = self.head
        # while current is not node:
        #     current = current.next
        # current.delete()
        self.delete(node) #O(1)
        self.add_to_head(node.value) #O(1)
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        # if self.head == node:
        #     self.add_to_tail(self.remove_from_head())

        # if self.tail == node:
        #     pass
            
        # else:
        #     current = self.head
        #     while current is not node:
        #         current = current.next
        #     current.delete()
        #     self.length -= 1
        #     self.add_to_tail(current.value)
        #     print('cur val', current.value)
        self.delete(node)
        self.add_to_tail(node.value)


    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node): # O(1)
        if node == self.head:
            self.remove_from_head()
        elif node == self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max_val = 0
        while current is not None:
            if current.value > max_val:
                max_val = current.value
            current = current.next
        return max_val


myLL = DoublyLinkedList()
myLL.add_to_tail(1)
myLL.add_to_tail(2)
myLL.add_to_tail(3)
myLL.move_to_end(myLL.head.next)