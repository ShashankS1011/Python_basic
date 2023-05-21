def encrypt(text,s):
	result = ""
	for x in range(len(text)):
		char = text[x]
		if (char.isupper()):
			result+= chr((ord(char)+s-65)%26+65)
		else:
			result+= chr((ord(char)+s-97)%26+97)
	return result
text="Helloworld"
s=4
print("Text: "+text)
print("Shift: "+str(s))
print("Cipher: "+encrypt(text,s))