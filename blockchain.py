from hashlib import sha256

class Block():
  data = None
  # the current block's hash
  hash = None
  # the number which produces a hash that matches the previous block's hash challenge
  # a hash challenge and nonce is based on Proof-of-Work
  nonce = 0
  # 2^256 possible unique hashes, which is equal to...
  # 115,792,089,237,316,195,423,570,985,008,687,907,853,269,984,665,640,564,039,457,584,007,913,129,639,936
  previousHash = "0" * 64

  def __init__(self, data, number):
   self.data = data
   self.number = number

class Blockchain():
  pass

def main():
  block  = Block("hellow world", 1)


if __name__ == '__main__':
  main()