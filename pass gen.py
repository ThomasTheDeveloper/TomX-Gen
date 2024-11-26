import string
import random
import time

s1 = string.ascii_lowercase
s2 = string.ascii_uppercase
s3 = string.digits
s4 = string.punctuation

passlen = int(input("Please Enter The Password Length "))

s = []
s.extend(list(s1))
s.extend(list(s2))
s.extend(list(s3))
s.extend(list(s4))
random.shuffle(s)
print("".join(s[0:passlen]))


print('Please Copy Your New Generated Password, None of your passwords get stored!')

time.sleep(7)