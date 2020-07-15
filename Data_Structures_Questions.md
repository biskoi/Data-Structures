Answer the following questions for each of the data structures you implemented as part of this project.

## Stack

1. What is the runtime complexity of `push` using a list?
O(n) - Memory might be doubled if the list runs out of memory space

2. What is the runtime complexity of `push` using a linked list?
O(1) - We're always only updating the tail and adding a new node to the end

3. What is the runtime complexity of `pop` using a list?
O(1) - No doubling

4. What is the runtime complexity of `pop` using a linked list?
O(1) - We just need to re-set the self.tail, and set the new tail.

5. What is the runtime complexity of `len` using a list?
O(1) - The length is stored as metadata. O(n) if we were to loop through it ourselves and count everything.

6. What is the runtime complexity of `len` using a linked list?
O(1) - we have a size variable that keeps track of this for us.

## Queue

1. What is the runtime complexity of `enqueue` using a list?
O(n) - worst case, we might be doubling again.

2. What is the runtime complexity of `enqueue` using a linked list?
O(1) - We're just adding a new node and changing the tail ref

3. What is the runtime complexity of `dequeue` using a list?
O(n) - popping from the beginning means the rest of the indexes need to be changed 

4. What is the runtime complexity of `dequeue` using a linked list?
O(1) - no doubling, no searching. Just removing the first one.

5. What is the runtime complexity of `len` using a list?
This is the same question as before!

6. What is the runtime complexity of `len` using a linked list?
This is the same question as before!

## Doubly Linked List

1. What is the runtime complexity of `ListNode.insert_after`?

2. What is the runtime complexity of `ListNode.insert_before`?

3. What is the runtime complexity of `ListNode.delete`?
O(1)

4. What is the runtime complexity of `DoublyLinkedList.add_to_head`?
O(1)

5. What is the runtime complexity of `DoublyLinkedList.remove_from_head`?
O(1)

6. What is the runtime complexity of `DoublyLinkedList.add_to_tail`?
O(1)

7. What is the runtime complexity of `DoublyLinkedList.remove_from_tail`?
O(1)

8. What is the runtime complexity of `DoublyLinkedList.move_to_front`?
O(1)

9. What is the runtime complexity of `DoublyLinkedList.move_to_end`?
O(1)

10. What is the runtime complexity of `DoublyLinkedList.delete`?
O(1)

    a. Compare the runtime of the doubly linked list's `delete` method with the worst-case runtime of the JS `Array.splice` method. Which method generally performs better?

    Well, since DLL.delete is constant time, and array.splice is O(n), DLL.delete will always perform better.

## Binary Search Tree

1. What is the runtime complexity of `insert`? 

2. What is the runtime complexity of `contains`?

3. What is the runtime complexity of `get_max`? 

4. What is the runtime complexity of `for_each`?
    
## Heap

1. What is the runtime complexity of `_bubble_up`?

2. What is the runtime complexity of `_sift_down`?

3. What is the runtime complexity of `insert`?

4. What is the runtime complexity of `delete`?

5. What is the runtime complexity of `get_max`?
