class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node

        self.tail = node

def print_singly_linked_list(list_head):
    while list_head is not None:
        print(list_head.data)
        list_head = list_head.next


def mergeLists(head1, head2):
    if head1 is None:
        return head2.head
    if head2 is None:
        return head1.head

    merged_list = SinglyLinkedList()
    iter1 = head1
    iter2 = head2
    while (iter1 is not None) or (iter2 is not None):
        if (iter1 is not None) and (iter2 is not None):
            if iter1.data <= iter2.data:
                merged_list.insert_node(iter1.data)
                iter1 = iter1.next
            else:
                merged_list.insert_node(iter2.data)
                iter2 = iter2.next
        elif (iter1 is None) and (iter2 is not None):
            merged_list.insert_node(iter2.data)
            iter2 = iter2.next
        else:
            merged_list.insert_node(iter1.data)
            iter1 = iter1.next

    return merged_list.head


if __name__ == '__main__':
    list1 = SinglyLinkedList()
    for i in [1, 2, 3]:
        list1.insert_node(i)

    list2 = SinglyLinkedList()
    for i in [3, 4]:
        list2.insert_node(i)

    print('--- list1')
    print_singly_linked_list(list1.head)

    print('--- list2')
    print_singly_linked_list(list2.head)

    merged_list_head = mergeLists(list1.head, list2.head)
    print('--- merged list')
    print_singly_linked_list(merged_list_head)



