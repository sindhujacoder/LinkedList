class Node:
  def __init__(self, value):
    self.previous = None
    self.next = None
    self.data = value

class CircularLinkedList:
  def __init__(self):
    self.head = None
  
  def traverse(self, starting_point=None):
    if not starting_point:
      starting_point = self.head
    node = starting_point
    while(node != None and node.next != starting_point):
        yield node
        node = node.next
    yield node
  
  def _print_(self, starting_point=None):
    nodes = []
    for node in self.traverse(starting_point):
      nodes.append(node.data)
    
    print('->'.join(nodes))
  

        
