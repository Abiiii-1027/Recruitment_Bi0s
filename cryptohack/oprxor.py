KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"
K1=bytes.fromhex(KEY1)
K1K2 = "37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e"
KR=bytes.fromhex(K1K2)
K2 = bytes(a^b for a,b in zip(K1 ,KR))
print("KEY2:",K2)
K2K3 = "c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1"
KR1 = bytes.fromhex(K2K3)
K3 = bytes(c^d for c,d in zip(K2,KR1))
print("KEY3:",K3)
flg = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf")
flag = bytes(e^f^g^h for e,f,g,h in zip(flg,K1,K2,K3))
print(flag)
