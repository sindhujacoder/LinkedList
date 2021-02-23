from my_linked_list import LinkedList, Node, BetterLinkedList


llist = LinkedList()
head = Node('0')
llist.head = head

new_node = Node('1')
head.next = new_node

new_node_1 = Node('2')
new_node.next  = new_node_1

print(llist._print_())

bllist = BetterLinkedList(['0', '1', '2', '4', '5'])

print('Adding -1 to head')
bllist.add_first(Node('-1'))
print('Adding -2 to head')
bllist.add_first(Node('-2'))

print('Adding 6 to end')
bllist.add_last(Node('6'))
print('Adding 7 to end')
bllist.add_last(Node('7'))

print('Adding 3 after 2')
bllist.add_after('2', '3')

#Uses __iter__ function
print('Adding -3 before 1')
bllist.add_before('1', '-3')
print('Adding -1.5 before -2')
bllist.add_before('-2', '-1.5')
print('remove node 5')
bllist.remove_node('5')
#add after a non existent node
#bllist.add_after('20', '6')

for node in bllist:
  print(node.data)

print('Reverse list')
bllist.reverse_linked_list()
for node in bllist:
  print(node.data)






  

