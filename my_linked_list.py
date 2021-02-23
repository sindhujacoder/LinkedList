#https://realpython.com/linked-lists-python/

#LinkedList and list 
# They can be used to implement  queues or stacks as well as graphs. They’re also useful for much more complex tasks, such as lifecycle management for an operating system application.

#When you know which element you want to access, lists can perform this operation in O(1) time. Trying to do the same with a linked list would take O(n) because you need to traverse the whole list to find the element.

#search - O(n) = lists `n` linkedlists

#With all this in mind, even though inserting elements at the end of a list using .append() or .insert() will have constant time, O(1), when you try inserting an element closer to or at the beginning of the list, the average time complexity will grow along with the size of the list: O(n).

#With all this in mind, even though inserting elements at the end of a list using .append() or .insert() will have constant time, O(1), when you try inserting an element closer to or at the beginning of the list, the average time complexity will grow along with the size of the list: O(n).

#linked lists have a performance advantage over normal lists when implementing a queue (FIFO), in which elements are continuously inserted and removed at the beginning of the list

#LL perform similarly to a list when implementing a stack (LIFO), in which elements are inserted and removed at the end of the list.


class LinkedList:
  def __init__(self):
    self.head = None

  def _print_(self):
    node = self.head
    nodes = []
    while node != None:
        nodes.append(node.data)
        node = node.next
        
    return '->'.join(nodes)

class BetterLinkedList:
   def __init__(self, nodes=None):
    self.head = None
    if nodes is not None:
      node = Node(nodes.pop(0))
      self.head = node
      for elem in nodes:
        node.next = Node(elem)
        node = node.next

   def __iter__(self):
    node = self.head
    while node != None:
        yield node
        node = node.next
    
   def add_first(self, node):
     #insert node at the beginning
      node.next = self.head
      self.head = node
  
   def add_last(self, node):
       temp = self.head
       if not self.head:
         self.head = node
         return
       while temp.next != None:
         temp = temp.next
       
       temp.next  = node

   def add_after(self, node_data, value):
      if not self.head:
        raise Exception("Empty list")

      new_node = Node(value)
      temp = self.head

      while(temp.data != node_data and temp.next !=None):
        temp = temp.next

      if temp.data != node_data:
          raise Exception("No node with data")

      new_node.next = temp.next
      temp.next = new_node

      
  
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  

  
