from my_linked_list import LinkedList, Node

llist = LinkedList()
head = Node('0')
llist.head = head

new_node = Node('1')
head.next = new_node

print(llist._print_())



  

