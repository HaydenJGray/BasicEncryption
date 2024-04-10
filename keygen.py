import random
import string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()
random.shuffle(key)
key = ''.join(key)


print(f"key : {key}")