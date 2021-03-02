from my_linked_list import LinkedList, Node, BetterLinkedList
from my_circular_linked_list import CircularLinkedList

llist = LinkedList()
head = Node('0')
llist.head = head

new_node = Node('1')
head.next = new_node

new_node_1 = Node('2')
new_node.next  = new_node_1

llist._print_()

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

bllist._print_()

print('Reverse list')
bllist.reverse_linked_list()
bllist._print_()

print('Remove duplicates from sorted list')
sorted_list = BetterLinkedList(['0', '1', '1', '1', '2', '2', '2', '4', '5', '5', '6'])
sorted_list.delete_duplicates_for_sorted_list()
sorted_list._print_()

print('Remove duplicates from unsorted list')
unsorted_list = BetterLinkedList(['2', '11', '8', '4', '10', '2', '6', '10', '8', '11', '11'])
unsorted_list.delete_duplicates_for_unsorted_list()
unsorted_list._print_()

print('Remove duplicates from unsorted list without buffer')
unsorted_list.delete_duplicates_for_unsorted_list_without_buffer()
unsorted_list._print_()

clist = CircularLinkedList()
head = Node('0')
clist.head = head

new_node = Node('1')
head.next = new_node

new_node_1 = Node('2')
new_node.next  = new_node_1

new_node_1.next = head

print("Circular Linked list")
clist._print_(new_node_1)







  

