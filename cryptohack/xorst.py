S = "label"
flag = ""
for i in S:
	flag += chr(ord(i)^13)
print("crypto{",flag,"}")	
		
