import hashlib

m = hashlib.sha256()
m.update(b"Nobody inspects")
m.update(b" the spammish repetition")
#print(m.hexdigest())
#print(m.digest_size)
#print(m.block_size)

#print(hashlib.sha224(b"Nobody inspects the spammish repetition").hexdigest())

h = hashlib.new('ripemd160')
h.update(b"Nobody inspects the spammish repetition")
#print(h.hexdigest())

H1 = hashlib.md5()
with open('sample.txt', 'rb') as afile:
    buf = afile.read()
    H1.update(buf)
print(H1.hexdigest())
H1= H1.hexdigest()
H2= hashlib.md5()
print(H2.hexdigest())
H2= H2.hexdigest()


def hammingdistance(hex1,hex2):
    x =hex1  ^ hex2
    setBits = 0
  
    while (x > 0) : 
        setBits += x & 1
        x >>= 1
    return setBits  
H2= 9
H1=14
print(hammingdistance(H2, H1))

