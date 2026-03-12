st="73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d"
cp = bytes.fromhex(st)
for i in range(256):
        flg =bytes(a^i for a in cp)
        print(flg)


	
