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
  
   def _print_(self):
    node = self.head
    nodes = []
    for node in self:
        nodes.append(node.data)
        node = node.next
        
    print('->'.join(nodes))

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

      while(temp.data != node_data and temp.next != None):
        temp = temp.next

      if temp.data != node_data:
          raise Exception("No match found")

      new_node.next = temp.next
      temp.next = new_node

   def add_before(self, node_data, value):
      if not self.head:
        raise Exception("Empty list")
      
      new_node = Node(value)

      if self.head.data == node_data:
        return self.add_first(new_node)

      prev_node = self.head

      for node in self:
          if node.data == node_data:
              prev_node.next = new_node
              new_node.next = node
              return 
        
          prev_node = node
  
      raise Exception("No match found")

   def remove_node(self, node_data):
      temp = self.head
      while(temp.data != node_data):
          prev_node = temp  
          temp = temp.next
      
      if temp.data != node_data:
        raise Exception("No match found")

      prev_node.next = temp.next;
      temp.next = None
  
   def reverse_linked_list(self):
      current = self.head
      previous = None
      while(current):
          next = current.next
          current.next = previous
          previous = current
          current = next
      self.head = previous

   def delete_duplicates_for_sorted_list(self):
       temp = self.head
       prev = None
       while(temp != None):
           if prev and temp.data == prev.data:
               prev.next = temp.next
               temp = prev.next
           else:
               prev = temp
               temp = temp.next
   
   def delete_duplicates_for_unsorted_list(self):
       #O(n) time, o(n) space
       #using buffer
       #or sort using merge sort and call delete_duplicates_for_sorted_list - o(nlogn)
       #or use two pointers - outer loop/inner loop
       temp = self.head
       prev = None
       buffer = []
       while(temp != None):
          if temp.data in buffer:
              prev.next = temp.next
              temp =  prev.next
          else:
              buffer.append(temp.data)
              prev = temp
              temp = temp.next
   
   def delete_duplicates_for_unsorted_list_without_buffer(self):
     #O(n^2) time
      one_runner = self.head
      
      while(one_runner != None):
          two_runner = one_runner

          while(two_runner.next != None):
              if one_runner.data == two_runner.next.data:
                  two_runner.next = two_runner.next.next
              else:
                  two_runner = two_runner.next
        
          one_runner = one_runner.next

   def get_kth_to_last_element(self, k):
      one_runner = self.head
      two_runner = self.head

      count = 0
      while(count<k-1):
          two_runner = two_runner.next
          count += 1

      while(two_runner != None):
          data = one_runner.data
          one_runner = one_runner.next
          two_runner = two_runner.next
      
      return data
   
   def detect_cycle(self):
      slow = self.head
      fast = self.head

      while(fast != None):
          if slow == fast.next:
            print('Cycle exists')
            return
          else:
            slow = slow.next
            fast = fast.next.next
      print('No cycle found')





class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  

  
