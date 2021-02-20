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

   def _print_(self):
    node = self.head
    nodes = []
    while node != None:
        nodes.append(node.data)
        node = node.next
        
    return '->'.join(nodes)
      
  
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

  

  
