from Transaction import Transaction
from Blockchain import Blockchain

if __name__ == "__main__":
    blockchain = Blockchain()

    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 25))
    blockchain.add_transaction(Transaction("Charlie", "Dave", 40))
    blockchain.add_transaction(Transaction("Dave", "Eve", 30))
    blockchain.add_transaction(Transaction("Eve", "Frank", 20))
    blockchain.add_transaction(Transaction("Frank", "Grace", 15))

    blockchain.mine_block_now()

    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 25))
    blockchain.add_transaction(Transaction("Charlie", "Dave", 40))
    blockchain.add_transaction(Transaction("Dave", "Eve", 30))
    blockchain.add_transaction(Transaction("Eve", "Frank", 20))
    blockchain.add_transaction(Transaction("Frank", "Grace", 15))

    blockchain.mine_block_now()

    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 25))
    blockchain.add_transaction(Transaction("Charlie", "Dave", 40))
    blockchain.add_transaction(Transaction("Dave", "Eve", 30))
    blockchain.add_transaction(Transaction("Eve", "Frank", 20))
    blockchain.add_transaction(Transaction("Frank", "Grace", 15))
    blockchain.add_transaction(Transaction("Alice", "Bob", 50))
    blockchain.add_transaction(Transaction("Bob", "Charlie", 25))
    blockchain.add_transaction(Transaction("Charlie", "Dave", 40))
    blockchain.add_transaction(Transaction("Dave", "Eve", 30))
    blockchain.add_transaction(Transaction("Eve", "Frank", 20))
    blockchain.add_transaction(Transaction("Frank", "Grace", 15))


    print("Is blockchain valid?", blockchain.validate_blockchain())

    for block in blockchain.chain:
        print(
            f"Block {block.index}: Hash = {block.hash}, Previous Hash = {block.previous_hash}, Merkle Root = {block.merkle_root}")
        print(f'Transactions = {block.transactions}')