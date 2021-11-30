3. Add a method to the classic LinkedList class that returns the last element
from the list. Assume you don’t know how many elements are in the list.

4. Here’s a tricky one. Add a method to the classic LinkedList class that
reverses the list. That is, if the original list is A -> B -> C, all of the list’s
links should change so that C -> B -> A.

5. Here’s a brilliant little linked list puzzle for you. Let’s say you have access
to a node from somewhere in the middle of a classic linked list, but not
the linked list itself. That is, you have a variable that points to an instance
of Node , but you don’t have access to the LinkedList instance. In this situation,
if you follow this node’s link, you can find all the items from this middle
node until the end, but you have no way to find the nodes that precede
this node in the list.
Write code that will effectively delete this node from the list. The entire
remaining list should remain complete, with only this node removed.