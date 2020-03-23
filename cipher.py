import clipboard

def encode(j):
	finStr = ""
	for letter in range(len(j)):
		try:
			finStr += chr(ord(j[letter])-letter)
		except:
			finStr += unichr(ord(j[letter])-letter)
	finStr = finStr[::-1]
	print(finStr + "\n")
	clipboard.copy(finStr)

def decode(i):
	i = i[::-1]
	finStr = ""
	for letter in range(len(i)):
		try:
			finStr += chr(ord(i[letter])+letter)
		except:
			finStr += unichr(ord(i[letter])+letter)
	print(finStr + "\n")
	clipboard.copy(finStr)

try:
	while True:
		i = raw_input("Enter text to encode > ")
		if i == "":
			print(" ")
			clipboard.copy(" ")
		else:
			encode(i)

		i = raw_input("Enter text to decode > ")
		if i == "":
			print(" ")
			clipboard.copy(" ")
		else:
			decode(i)
except:
	print("Python 3 being used, restarting...\n\n")
	while True:
		i = input("Enter text to encode > ")
		if i == "":
			print(" ")
			clipboard.copy(" ")
		else:
			encode(i)

		i = input("Enter text to decode > ")
		if i == "":
			print(" ")
			clipboard.copy(" ")
		else:
			decode(i)
