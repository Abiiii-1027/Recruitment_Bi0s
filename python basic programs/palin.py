def palindrome():
	S = input()
	if  S == S[::-1]:
		print("It is a plaindrome")
	else:
		print("Not a palindrome")

palindrome()
