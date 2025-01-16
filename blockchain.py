import hashlib
import time


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        
        return Block(0, time.time(), "genesis block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, new_data):
        
        latest_block = self.get_latest_block()
        new_block = Block(len(self.chain), time.time(), new_data, latest_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

        
            if current_block.hash != current_block.calculate_hash():
                return False

            if current_block.previous_hash != previous_block.hash:
                return False

        return True


if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block("Transaction 1")
    my_blockchain.add_block("Transaction 2")

    for block in my_blockchain.chain:
        print(f"Block {block.index}:")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print(f"Previous Hash: {block.previous_hash}\n")

    print("is blockchain valid?", my_blockchain.is_chain_valid())
