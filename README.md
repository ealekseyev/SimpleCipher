# SimpleCipher
A simple python ciphering/deciphering program - Caesar Cipher with a couple of twists
* One file works with both Python 2 and Python 3.

# How it works
First, the inputted text is reversed.
Second, the reversed text's individual characters are shifted up depending on the counter - the first character of the reversed string is shifted up one, the second character is shifted up 2, the third is shifted up 3, etc.
* This is good enough for secret chats with a friend, but is by no means even close to full-blown AES encryption.
