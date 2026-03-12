def anagra():
	str1 = input("Enter the string1:").lower()
	str2 = input("Enter the string2:").lower()
	if len(str1) != len(str2):
		print("it is not an anagram")
	if sorted(str1) == sorted(str2):
		print("It is an anagram")
	else:
		print("it is not an anagram")
anagra()
				
			
			
