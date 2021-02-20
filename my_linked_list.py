class LinkedList:
  def __init_(self):
    self.head = None
  
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

  

  
