from hashlib import sha256

# 256 bits or 2^256 possible unique hashes, which is equal to...
# 115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,936

# universal update hash function
def updateHash(*args):
    # initialize hash and sha256 algorithm
    hashingText = ""
    h = sha256()
    # each argument is turned into a string object
    for arg in args:
        hashingText += str(arg)

    h.update(hashingText.encode("utf-8"))
    return h.hexdigest()


# a block of data storage
class Block:
    # any data or metadata stored within the block
    data = None
    # the current block's hash
    hash = None
    # the number which produces a hash that matches the previous block's hash challenge/difficulty
    # a hash challenge/difficulty and nonce is based on Proof-of-Work concept
    nonce = 0
    # hash of the previous block in the blockchain
    previousHash = "0" * 64

    # initial constructor
    def __init__(self, data, number):
        self.data = data
        self.number = number

    # hash of the block
    def hash(self):
        return updateHash(self.previousHash, self.number, self.data, self.nonce)

    # default print statement for instantiated block
    def __str__(self):
        return (
            f"Block: {self.number}\n"
            + f"Hash: {self.hash()}\n"
            + f"Previous: {self.previousHash}\n"
            + f"Data: {self.data}\n"
            + f"Nonce: {self.nonce}"
        )


# chain that connects the blocks of data
class Blockchain:
    # initial challenge/difficulty
    difficulty = 4

    def __init__(self, chain=[]):
        # chain for storing stack of blocks
        self.chain = chain

    # method that adds block data to chain
    def add(self, block):
        self.chain.append(
            {
                "hash": block.hash(),
                "previous": block.previousHash,
                "number": block.number,
                "data": block.data,
                "nonce": block.nonce,
            }
        )

    # method for mining blocks
    def mine(self, block):
        # looks for previous block to chain to
        # if none, it is first block and has no previous block
        try:
            block.previousHash = self.chain[-1].get("hash")
        except IndexError:
            pass

        # looks for amount of preceding zeroes in hash
        # based on difficulty (e.g. difficulty of 4 equals 0000)
        while True:
            if block.hash()[:(self.difficulty)] == "0" * self.difficulty:
                self.add(block)
                break
            else:
                # nonce is increased every time produced hash fails
                block.nonce += 1

    def __str__(self):
        return str(self.chain)


# executes upon program start
# test blockchain with random set of data
def main():
    blockchain = Blockchain()
    database = ["hello world", "what's up", "hello", "bye"]

    num = 0
    for data in database:
        num += 1
        blockchain.mine(Block(data, num))

    for block in blockchain.chain:
        print(block)


if __name__ == "__main__":
    main()
