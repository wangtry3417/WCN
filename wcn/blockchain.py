import hashlib
from requests import get

class NFT(object):
  def __init__(self,crypto_type):
    self.crypto_type = crypto_type
    self.hash_data = []
  def hash(data : list):
    text1 = [data[0],data[1],str(data[2])]
    t1 = ",".join(text1)
    hash1 = hashlib.sha256(t1.encode()).hexdigest()
    return hash1
