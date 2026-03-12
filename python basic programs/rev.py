def strreverse():
	F = input("Enter the string:")
	S = " "
	L = len(F)
	for i in range(L,-1,-1):
		if F[i-1].isalpha:
			S = S+F[i-1]
		else:
			S = S+F[i-1]
	print(S)
strreverse()
			
