from Block import Block


class Blockchain:
    def __init__(self, difficulty=4):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty
        self.pending_transactions = []

    def create_genesis_block(self):
        return Block(0, "0", [])

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.pending_transactions.append(transaction)
        if len(self.pending_transactions) == 10:
            self.mine_pending_block()

    def mine_pending_block(self):
        if len(self.pending_transactions) == 0:
            print("No transactions to mine.")
            return

        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, self.pending_transactions[:10])
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = self.pending_transactions[10:]

    def mine_block_now(self):
        if len(self.pending_transactions) == 0:
            print("No transactions to mine.")
            return

        previous_block = self.get_latest_block()
        new_block = Block(len(self.chain), previous_block.hash, self.pending_transactions)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)
        self.pending_transactions = []

    def validate_blockchain(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False

        return True