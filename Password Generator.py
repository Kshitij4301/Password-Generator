import random
s = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%^&()_-+[]{}:/';.,"
passwordlen = 16
password = "".join(random.sample(s,passwordlen))
print(password)