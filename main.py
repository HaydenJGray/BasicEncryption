import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

def Encrypt():
    plain_text = input("Eneter message:")
    key = input("Eneter key:")
    cipher_text = ""

    for letter in plain_text:
        index = key.index(letter)
        cipher_text += chars[index]
        
    # print(f"Original message: {plain_text}")
    print(f"Encrypted message: {cipher_text}")

def Decrypt():
    cipher_text = input("Eneter message:")
    key = input("Eneter key:")
    plain_text = ""

    for letter in cipher_text:
        index = chars.index(letter)
        plain_text += key[index]
        
    # print(f"Encrypted message: {cipher_text}")
    print(f"Original message: {plain_text}")

#MAIN
print("Encrypt or Decript?")
answer = input("Answer(e/d)")

if answer == "e":
    Encrypt()
elif answer == "d":
    Decrypt()
else:
    print("Error")





