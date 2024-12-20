import time
from MerkleTree import MerkleTree
from sha256_hash import sha256_hash

class Block:
    def __init__(self, index, previous_hash, transactions):
        self.index = index
        self.timestamp = int(time.time())
        self.previous_hash = previous_hash
        self.transactions = transactions
        self.merkle_root = MerkleTree.calculate_merkle_root(transactions)
        self.nonce = 0
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.previous_hash}{self.merkle_root}{self.nonce}"
        return sha256_hash(block_string)


    def mine_block(self, difficulty):
        target = '0' * difficulty
        start_time = time.time()
        print(f"Mining block {self.index}...")
        while not self.hash.startswith(target):
            self.nonce += 1
            self.hash = self.calculate_hash()
            if self.nonce % 100000 == 0:  # Log progress every 100,000 iterations
                print(f"Nonce: {self.nonce}, Current Hash: {self.hash}")
        end_time = time.time()
        print(f"Block mined! Nonce: {self.nonce}, Hash: {self.hash}, Time Taken: {end_time - start_time:.2f} seconds")
