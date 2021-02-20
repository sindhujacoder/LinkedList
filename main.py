from my_linked_list import LinkedList, Node, BetterLinkedList


llist = LinkedList()
head = Node('0')
llist.head = head

new_node = Node('1')
head.next = new_node

new_node_1 = Node('2')
new_node.next  = new_node_1

print(llist._print_())

bllist = BetterLinkedList(['0', '1', '2'])
print(bllist._print_())




  

