from sha256_hash import sha256_hash

class MerkleTree:
    @staticmethod
    def calculate_merkle_root(transactions):
        if not transactions:
            return ''

        def hash_pair(left, right):
            return sha256_hash(left + right)

        hashes = [sha256_hash(f"{t.sender}{t.receiver}{t.amount}") for t in transactions]

        while len(hashes) > 1:
            if len(hashes) % 2 == 1:
                hashes.append(hashes[-1])
            hashes = [hash_pair(hashes[i], hashes[i + 1]) for i in range(0, len(hashes), 2)]

        return hashes[0]