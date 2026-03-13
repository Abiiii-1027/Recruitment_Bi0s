def strreverse():
    F = input("Enter the string: ")
    letters = [F[i] for i in range(len(F)) if F[i].isalpha()]
    result = []
    letter_idx = len(letters) - 1
	for ch in F:
	     if ch.isalpha():
            result.append(letters[letter_idx])
            letter_idx -= 1
        else:
            result.append(ch)  
	print(''.join(result))
strreverse()
			
