class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):
        '''
        Modified from sample code to keep runtime to O(1)
        '''
        if self.head is None:
            self.head = Node(value)
            return

        node = Node(value)
        node.next = self.head
        self.head = node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

    def __iter__(self):
    '''
    Added to sample code to make traversal easier
    '''
        node = self.head
        while node:
            yield node
            node = node.next

def union(llist_1, llist_2):
    '''
    Taking advantage of the set class to
    ensure there are no repeat items

    Repeated items in a list are ignored to keep strictly
    to the definition of a set
    '''
    union = set()

    for node in llist_1:
        union.add(node.value)

    for node in llist_2:
        union.add(node.value)

    llist_union = LinkedList()

    for value in union:
        llist_union.append(value)

    return llist_union



def intersection(llist_1, llist_2):
    llist_1_set = set()
    intersection = set()

    for node in llist_1:
        llist_1_set.add(node.value)

    # Checks if item in list 2 is already in list one
    # then adds it to the intersection set
    for node in llist_2:
        if node.value in llist_1_set:
            intersection.add(node.value)

    llist_intersection = LinkedList()
    for value in intersection:
        llist_intersection.append(value)
    return llist_intersection
