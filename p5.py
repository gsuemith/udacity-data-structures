import hashlib
from datetime import datetime

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp.strftime("%H:%M %m/%d/%Y")
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()
        self.next = None

    def calc_hash(self):
        sha = hashlib.sha256()

        string = self.timestamp + self.data + self.previous_hash
        hash_str = string.encode('utf-8')
        sha.update(hash_str)

        return sha.hexdigest()

class Blockchain:
    '''
    The head of each block chain is the most recent block;
    i.e. blocks get older further down the chain
    '''
    def __init__(self, genesis_block):
        self.head = genesis_block

    def add(self, data):
        block = Block(datetime.utcnow(), data, self.head.hash)
        block.next = self.head
        self.head = block

    def is_valid(self):
        '''
        Checks to see if hashes remain correctly linked to
        previous hashes.  Any changes to the data, timestamp, or hash
        in any block will cause this method to return False
        '''
        curr_node = self.head
        prev_node = curr_node.next
        while prev_node:
            if curr_node.hash != curr_node.calc_hash():
                return False
            if curr_node.previous_hash != prev_node.hash:
                return False

            curr_node = prev_node
            prev_node = prev_node.next

        return True
