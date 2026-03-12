from  itertools  import cycle 
st="0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"
cp = bytes.fromhex(st)
key1 = "crypto{".encode()
print(cp)
print(key1)
key = bytes(a ^ b for a, b in zip(cp, key1))
print(key)
fkey =b"myXORkey"
flag = bytes([c ^ d for c, d in zip(cycle(fkey),cp)])
print(flag)
