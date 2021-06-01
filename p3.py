import sys

class Node:
    '''
    A hybride linked-list/binary tree node that stores a character
    and the character's frequency
    '''
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
        self.next = None

    def __repr__(self):
        return f"({self.char}, {self.freq})"

class Tree:
    def __init__(self, root):
        self.root = root

    def huffman_code(self):
        h_codes = dict()

        def traverse(code, node):
            if node.char:
                h_codes[node.char] = code
                return

            traverse(code + '0', node.left)
            traverse(code + '1', node.right)

        traverse('', self.root)

        return h_codes

class Queue:
    '''
    A priority queue
    '''
    def __init__(self):
        self.head = None
        self.size = 0

    def enqueue(self, new_node):
        '''
        Appends node ahead of larger frequencies or the end
        '''
        if new_node is None:
            return

        node = self.head
        if node is None:
            self.head = new_node
            self.size += 1
            return

        previous = None
        while node and node.freq <= new_node.freq:
            previous = node
            node = node.next

        new_node.next = node
        previous.next = new_node
        self.size += 1

    def dequeue(self):
        head = self.head

        if head is None:
            return None

        self.head = head.next
        self.size -= 1
        return head

    def __repr__(self):
        node = self.head
        all_nodes = []
        while(node):
            all_nodes.append(str(node))
            node = node.next

        return ', '.join(all_nodes)

def huffman_encoding(data):
    counts = dict()
    #Count frequency
    for char in data:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1

    q = Queue()

    for char in sorted(counts, key=lambda x:counts[x]):
        q.enqueue(Node(char, counts[char]))

    while q.size > 1:
        left = q.dequeue()
        right = q.dequeue()
        merger = Node(None, left.freq + right.freq)
        merger.left = left
        merger.right = right
        q.enqueue(merger)


    tree = Tree(q.head)
    h_codes = tree.huffman_code()
    encoded_data = ''.join([h_codes[char] for char in data])

    return encoded_data, Tree(q.head)

def huffman_decoding(data, tree):
    decoded = []

    node = tree.root

    for bit in data:
        if bit == '0':
            node = node.left
        else:
            node = node.right

        if node.char:
            decoded.append(node.char)
            node = tree.root

    return ''.join(decoded)
