from my_linked_list import LinkedList, Node, BetterLinkedList


llist = LinkedList()
head = Node('0')
llist.head = head

new_node = Node('1')
head.next = new_node

new_node_1 = Node('2')
new_node.next  = new_node_1

print(llist._print_())

bllist = BetterLinkedList(['0', '1', '2', '4'])

bllist.add_first(Node('-1'))
bllist.add_first(Node('-2'))
bllist.add_last(Node('5'))

bllist.add_after('2', '3')
bllist.add_after('5', '6')
#Uses __iter__ function
for node in bllist:
  print(node.data)
bllist.add_after('20', '6')




  

